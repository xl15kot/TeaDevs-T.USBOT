"""
Команда .neofetch — информация о системе
Arch/Manjaro/etc → fastfetch, всё остальное → neofetch
Если ничего нет — собирает сам
"""
import subprocess
import platform
import asyncio
import re
import os


def _detect_distro():
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"').lower()
    except FileNotFoundError:
        pass
    return platform.system().lower()


def _is_arch():
    return _detect_distro() in (
        "arch", "manjaro", "endeavouros", "garuda",
        "artix", "cachyos", "arcolinux"
    )


async def _run_tool():
    if _is_arch():
        tool, cmd = "fastfetch", ["fastfetch", "--pipe"]
    else:
        tool, cmd = "neofetch", ["neofetch", "--stdout"]

    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=15)
        output = stdout.decode("utf-8", errors="replace").strip()
        # Убираем ANSI-коды
        output = re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", output)
        return f"🖥 **{tool}**\n\n```\n{output}\n```"
    except FileNotFoundError:
        return None  # инструмент не установлен
    except asyncio.TimeoutError:
        return "❌ Таймаут (15с)"
    except Exception as e:
        return f"❌ Ошибка: {e}"


async def _manual_info():
    try:
        import psutil
        import time
        import socket

        lines = []
        distro = _detect_distro()
        u = platform.uname()

        lines.append(f"OS:       {u.system} [{distro}]")
        lines.append(f"Kernel:   {u.release}")
        lines.append(f"Arch:     {u.machine}")
        lines.append(f"Host:     {socket.gethostname()}")

        cpu_cores   = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        cpu_freq    = psutil.cpu_freq()
        freq_str    = f" @ {cpu_freq.current:.0f} MHz" if cpu_freq else ""
        cpu_name    = u.processor or platform.processor() or "Unknown"
        lines.append(f"CPU:      {cpu_name} ({cpu_cores}C/{cpu_threads}T{freq_str})")
        lines.append(f"CPU Load: {psutil.cpu_percent(interval=0.5)}%")

        ram = psutil.virtual_memory()
        lines.append(f"RAM:      {ram.used//1024**2} MB / {ram.total//1024**2} MB ({ram.percent}%)")

        swap = psutil.swap_memory()
        if swap.total:
            lines.append(f"Swap:     {swap.used//1024**2} MB / {swap.total//1024**2} MB ({swap.percent}%)")

        for p in psutil.disk_partitions():
            try:
                d = psutil.disk_usage(p.mountpoint)
                lines.append(f"Disk [{p.mountpoint}]: {d.used/1024**3:.1f} / {d.total/1024**3:.1f} GB ({d.percent}%)")
            except PermissionError:
                pass

        up = int(time.time() - psutil.boot_time())
        lines.append(f"Uptime:   {up//3600}h {(up%3600)//60}m")

        try:
            r = subprocess.run(["lspci"], capture_output=True, text=True, timeout=5)
            for line in r.stdout.splitlines():
                if any(x in line.lower() for x in ("vga", "3d", "display", "nvidia", "amd", "radeon")):
                    lines.append(f"GPU:      {line.split(':', 2)[-1].strip()}")
                    break
        except Exception:
            pass

        lines.append(f"Shell:    {os.environ.get('SHELL', 'unknown')}")
        de = os.environ.get("XDG_CURRENT_DESKTOP") or os.environ.get("DESKTOP_SESSION") or "N/A"
        lines.append(f"DE/WM:    {de}")

        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for chip, entries in temps.items():
                    for e in entries:
                        if e.current and e.current > 0:
                            lines.append(f"Temp:     {e.current}°C ({chip}/{e.label or 'N/A'})")
                            break
                    break
        except Exception:
            pass

        return "🖥 **System Info**\n\n```\n" + "\n".join(lines) + "\n```"

    except ImportError:
        return "❌ Нет psutil. Установи: pip install psutil"


async def execute(event, args, client, db):
    if platform.system() == "Linux":
        result = await _run_tool()
        if result is None:
            tool = "fastfetch" if _is_arch() else "neofetch"
            result = await _manual_info()
            result = f"⚠️ {tool} не найден\n\n" + result
    elif platform.system() == "Darwin":
        try:
            proc = await asyncio.create_subprocess_exec(
                "system_profiler", "SPHardwareDataType",
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=10)
            result = "🍎 **macOS**\n\n```\n" + stdout.decode(errors="replace").strip() + "\n```"
        except Exception:
            result = await _manual_info()
    else:
        result = await _manual_info()

    # Telegram лимит 4096 символов
    if len(result) > 4090:
        result = result[:4087] + "..."

    return result
