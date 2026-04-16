"""
Команда .sysinfo — информация о системе и железе
"""
import platform
import socket
import time


async def execute(event, args, client, db):
    os_name = platform.system()

    if os_name == "Windows":
        icon, os_type = "🪟", "Windows"
    elif os_name == "Linux":
        icon, os_type = "🐧", "Linux"
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        os_type = line.split("=", 1)[1].strip().strip('"')
                        break
        except Exception:
            pass
    elif os_name == "Darwin":
        icon, os_type = "🍎", "macOS"
    else:
        icon, os_type = "💻", os_name

    lines = [f"{icon} **{os_type}**\n"]

    # OS
    lines.append(f"🖥 **OS:** {os_type}")
    lines.append(f"📀 **Kernel:** {platform.release()}")
    lines.append(f"⚙️ **Arch:** {platform.machine()}")
    lines.append(f"🌐 **Host:** {socket.gethostname()}")
    lines.append(f"🐍 **Python:** {platform.python_version()}")

    # CPU + RAM через psutil если есть
    try:
        import psutil

        # CPU
        cpu_freq = psutil.cpu_freq()
        freq_str = f" @ {cpu_freq.current:.0f} MHz" if cpu_freq else ""
        cores   = psutil.cpu_count(logical=False)
        threads = psutil.cpu_count(logical=True)
        cpu_load = psutil.cpu_percent(interval=0.3)
        lines.append(f"🔲 **CPU:** {cores}C/{threads}T{freq_str} | Load: {cpu_load}%")

        # RAM
        ram = psutil.virtual_memory()
        lines.append(f"💾 **RAM:** {ram.used//1024**2} / {ram.total//1024**2} MB ({ram.percent}%)")

        # Uptime
        up = int(time.time() - psutil.boot_time())
        lines.append(f"⏱ **Uptime:** {up//3600}h {(up%3600)//60}m")

        # Disk (только root / C:\)
        mount = "C:\\" if os_name == "Windows" else "/"
        try:
            d = psutil.disk_usage(mount)
            lines.append(f"💿 **Disk [{mount}]:** {d.used/1024**3:.1f} / {d.total/1024**3:.1f} GB ({d.percent}%)")
        except Exception:
            pass

    except ImportError:
        lines.append("_(установи psutil для CPU/RAM: pip install psutil)_")

    return "\n".join(lines)
