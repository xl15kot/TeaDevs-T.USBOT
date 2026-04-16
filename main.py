import os
import sys
import json
import time
import asyncio
import threading
import sqlite3
import platform
import importlib.util
from tkinter import *
from tkinter import ttk, messagebox, scrolledtext
from telethon import TelegramClient, events
VERSION = "v0.2 Beta"
TEAM = "TeaDevs"
LANGUAGES = {
    "ru": {
        "app_title": f"T.UserBot Reborn {VERSION}",
        "start": "▶ СТАРТ",
        "stop": "■ СТОП",
        "api_settings": "🔑 API",
        "settings": "⚙️ Настройки",
        "exit": "✖ Выход",
        "online": "● ОНЛАЙН",
        "offline": "● ОФФЛАЙН",
        "ready": "Готов",
        "bot_started": "Бот запущен",
        "bot_stopped": "Бот остановлен",
        "api_saved": "API сохранён",
        "settings_saved": "Настройки сохранены",
        "commands_loaded": "команд загружено",
        "no_api": "Нет API данных",
        "unknown_cmd": "Неизвестная команда",
        "tab_general": "Основные",
        "tab_appearance": "Внешний вид",
        "tab_bot": "Бот",
        "tab_console": "Консоль",
        "tab_about": "О программе",
        "language": "Язык",
        "russian": "Русский",
        "english": "English",
        "autostart": "Автозапуск бота",
        "minimize_to_tray": "Сворачивать в трей",
        "check_updates": "Проверять обновления",
        "theme": "Тема",
        "dark": "Тёмная",
        "light": "Светлая",
        "blue": "Синяя",
        "green": "Зелёная",
        "purple": "Фиолетовая",
        "font_size": "Размер шрифта",
        "small": "Маленький",
        "medium": "Средний",
        "large": "Большой",
        "show_icons": "Показывать иконки",
        "animation": "Анимация интерфейса",
        "command_prefix": "Префикс команд",
        "default_prefix": "Точка (.)",
        "auto_reconnect": "Автопереподключение",
        "save_logs": "Сохранять логи",
        "max_commands_per_minute": "Макс. команд в минуту",
        "unlimited": "Безлимит",
        "blacklist": "Чёрный список чатов",
        "whitelist": "Белый список",
        "console_lines": "Строк в консоли",
        "console_font": "Шрифт консоли",
        "timestamps": "Показывать время",
        "colored_output": "Цветной вывод",
        "auto_clear": "Автоочистка при старте",
        "export_logs": "Экспорт логов",
        "about_text": f"""T.UserBot Reborn {VERSION}

Разработчики: AveBas, LimuxMintREAL
Студия: TeaDevs

Лицензия: Proprietary
© 2026 TeaDevs""",
        "save": "Сохранить",
        "cancel": "Отмена",
        "apply": "Применить",
        "reset": "Сбросить",
        "telegram_api": "TELEGRAM API",
        "api_id": "API ID",
        "api_hash": "API HASH",
        "phone": "НОМЕР ТЕЛЕФОНА",
        "phone_format": "Формат: +79001234567",
        "first_run_title": "ПЕРВЫЙ ЗАПУСК",
        "api_instruction": "Получите API на my.telegram.org",
        "commands_list": "Список команд",
        "total_commands": "Всего команд",
        "status": "Статус",
    },
    "en": {
        "app_title": f"T.UserBot Reborn {VERSION}",
        "start": "▶ START",
        "stop": "■ STOP",
        "api_settings": "🔑 API",
        "settings": "⚙️ Settings",
        "exit": "✖ Exit",
        "online": "● ONLINE",
        "offline": "● OFFLINE",
        "ready": "Ready",
        "bot_started": "Bot started",
        "bot_stopped": "Bot stopped",
        "api_saved": "API saved",
        "settings_saved": "Settings saved",
        "commands_loaded": "commands loaded",
        "no_api": "No API data",
        "unknown_cmd": "Unknown command",
        "tab_general": "General",
        "tab_appearance": "Appearance",
        "tab_bot": "Bot",
        "tab_console": "Console",
        "tab_about": "About",
        "language": "Language",
        "russian": "Russian",
        "english": "English",
        "autostart": "Auto-start bot",
        "minimize_to_tray": "Minimize to tray",
        "check_updates": "Check for updates",
        "theme": "Theme",
        "dark": "Dark",
        "light": "Light",
        "blue": "Blue",
        "green": "Green",
        "purple": "Purple",
        "font_size": "Font size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
        "show_icons": "Show icons",
        "animation": "UI animation",
        "command_prefix": "Command prefix",
        "default_prefix": "Dot (.)",
        "auto_reconnect": "Auto reconnect",
        "save_logs": "Save logs",
        "max_commands_per_minute": "Max commands per minute",
        "unlimited": "Unlimited",
        "blacklist": "Chat blacklist",
        "whitelist": "Whitelist",
        "console_lines": "Console lines",
        "console_font": "Console font",
        "timestamps": "Show timestamps",
        "colored_output": "Colored output",
        "auto_clear": "Auto clear on start",
        "export_logs": "Export logs",
        "about_text": f"""T.UserBot Reborn {VERSION}

Developers: AveBas, LimuxMintREAL
Studio: TeaDevs

Features:
• 280+ real commands
• Modular system
• Multi-language
• 6 themes
• Flexible settings

License: Proprietary
© 2025 TeaDevs Studio""",
        "save": "Save",
        "cancel": "Cancel",
        "apply": "Apply",
        "reset": "Reset",
        "telegram_api": "TELEGRAM API",
        "api_id": "API ID",
        "api_hash": "API HASH",
        "phone": "PHONE NUMBER",
        "phone_format": "Format: +79001234567",
        "first_run_title": "FIRST RUN",
        "api_instruction": "Get API at my.telegram.org",
        "commands_list": "Commands list",
        "total_commands": "Total commands",
        "status": "Status",
    }
}
THEMES = {
    "dark": {
        "name": "🌙 Dark",
        "bg": "#0D1117",
        "bg2": "#161B22",
        "bg3": "#21262D",
        "fg": "#C9D1D9",
        "fg2": "#8B949E",
        "accent": "#238636",
        "accent_hover": "#2EA043",
        "danger": "#DA3633",
        "border": "#30363D",
        "console_bg": "#0D1117",
        "console_fg": "#C9D1D9",
    },
    "light": {
        "name": "☀️ Light",
        "bg": "#FFFFFF",
        "bg2": "#F6F8FA",
        "bg3": "#E9ECEF",
        "fg": "#1F2328",
        "fg2": "#656D76",
        "accent": "#0969DA",
        "accent_hover": "#1F883D",
        "danger": "#CF222E",
        "border": "#D0D7DE",
        "console_bg": "#F6F8FA",
        "console_fg": "#1F2328",
    },
}
default_settings = {
    "language": "ru",
    "theme": "dark",
    "autostart": False,
    "minimize_to_tray": False,
    "check_updates": True,
    "font_size": "medium",
    "show_icons": True,
    "animation": True,
    "command_prefix": ".",
    "auto_reconnect": True,
    "save_logs": True,
    "max_commands_per_minute": 0,
    "blacklist": [],
    "whitelist": [],
    "console_lines": 100,
    "console_font": "Consolas",
    "timestamps": True,
    "colored_output": True,
    "auto_clear": False,
}
settings = default_settings.copy()
def load_settings():
    global settings
    if os.path.exists("data/settings.json"):
        try:
            with open("data/settings.json", "r") as f:
                saved = json.load(f)
                settings.update(saved)
        except:
            pass
def save_settings():
    with open("data/settings.json", "w") as f:
        json.dump(settings, f, indent=2)
load_settings()
LANG = LANGUAGES[settings["language"]]
THEME = THEMES[settings["theme"]]
os.makedirs("data", exist_ok=True)
os.makedirs("commands", exist_ok=True)
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("data/userbot.db", check_same_thread=False)
        self.c = self.conn.cursor()
        self._init()
    def _init(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS economy 
                         (user_id INTEGER PRIMARY KEY, balance INTEGER DEFAULT 100, 
                          bank INTEGER DEFAULT 0, job TEXT DEFAULT 'Безработный', 
                          xp INTEGER DEFAULT 0, level INTEGER DEFAULT 1,
                          last_work TEXT, last_daily TEXT)""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS cmd_stats 
                         (cmd TEXT PRIMARY KEY, count INTEGER DEFAULT 0)""")
        self.conn.commit()
    def get_balance(self, uid):
        self.c.execute("INSERT OR IGNORE INTO economy (user_id) VALUES (?)", (uid,))
        self.conn.commit()
        self.c.execute("SELECT balance, bank, job FROM economy WHERE user_id=?", (uid,))
        return self.c.fetchone()
    def add_balance(self, uid, amount):
        self.c.execute("UPDATE economy SET balance=balance+? WHERE user_id=?", (amount, uid))
        self.conn.commit()
    def stat(self, cmd):
        self.c.execute("INSERT INTO cmd_stats(cmd,count) VALUES(?,1) ON CONFLICT(cmd) DO UPDATE SET count=count+1", (cmd,))
        self.conn.commit()
db = Database()
def load_api():
    if os.path.exists("data/api_data.json"):
        with open("data/api_data.json", "r") as f:
            d = json.load(f)
            return d.get("api_id"), d.get("api_hash"), d.get("phone")
    return None, None, None
def save_api(api_id, api_hash, phone):
    with open("data/api_data.json", "w") as f:
        json.dump({"api_id": api_id, "api_hash": api_hash, "phone": phone}, f, indent=2)
def first_run():
    print("\n" + "="*50)
    print(f"T.UserBot Reborn {VERSION} | {TEAM}")
    print("="*50 + "\n")
    print("Для работы нужны API ключи Telegram")
    print("Получить: https://my.telegram.org/apps\n")
    while True:
        try:
            api_id = int(input("API ID: ").strip())
            break
        except:
            print("Ошибка! Введите число")
    api_hash = input("API Hash: ").strip()
    phone = input("Номер телефона (+79001234567): ").strip()
    save_api(api_id, api_hash, phone)
    print("\n✅ API сохранён!")
    input("Нажмите Enter для запуска...")
bot_client = None
bot_running = False
log_messages = []
def add_log(msg):
    timestamp = time.strftime('%H:%M:%S') if settings["timestamps"] else ""
    prefix = f"[{timestamp}] " if timestamp else ""
    log_messages.append(f"{prefix}{msg}")
    if len(log_messages) > settings["console_lines"]:
        log_messages.pop(0)
def load_commands():
    commands = {}
    if not os.path.exists("commands"):
        return commands
    for file in os.listdir("commands"):
        if file.endswith(".py") and file != "__init__.py":
            cmd_name = file[:-3]
            file_path = os.path.join("commands", file)
            try:
                spec = importlib.util.spec_from_file_location(cmd_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "execute"):
                    commands[cmd_name] = module.execute
                    add_log(f"✅ .{cmd_name}")
            except Exception as e:
                add_log(f"❌ {file}: {e}")
    return commands
def run_bot_thread(commands):
    asyncio.run(run_bot(commands))
async def run_bot(commands):
    global bot_client, bot_running
    api_id, api_hash, phone = load_api()
    if not api_id:
        add_log(f"❌ {LANG['no_api']}")
        return
    bot_client = TelegramClient("data/userbot", int(api_id), api_hash)
    try:
        await bot_client.start(phone=phone)
        bot_running = True
        me = await bot_client.get_me()
        add_log(f"✅ {LANG['bot_started']}: {me.first_name}")
        add_log(f"📦 {len(commands)} {LANG['commands_loaded']}")
        @bot_client.on(events.NewMessage(outgoing=True))
        async def handler(event):
            if not event.text or not event.text.startswith(settings["command_prefix"]):
                return
            parts = event.text[1:].split()
            cmd = parts[0].lower()
            args = parts[1:]
            db.stat(cmd)
            add_log(f"CMD: .{cmd}")
            if cmd in commands:
                try:
                    result = await commands[cmd](event, args, bot_client, db)
                    if result:
                        await event.edit(str(result))
                except Exception as e:
                    await event.edit(f"❌ {e}")
            else:
                await event.edit(f"❌ {LANG['unknown_cmd']}")
        await bot_client.run_until_disconnected()
    except Exception as e:
        add_log(f"❌ {e}")
        bot_running = False
class TUserBotGUI:
    def __init__(self, commands):
        self.commands = commands
        self.root = Tk()
        self.root.title(f"{LANG['app_title']} | {TEAM}")
        self.root.geometry("520x680")
        self.root.resizable(False, False)
        self.root.configure(bg=THEME["bg"])
        self.center_window()
        self.running = False
        self._build_ui()
        self._update_console()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        add_log(f"{LANG['app_title']} | {TEAM}")
        add_log(f"📦 {len(commands)} {LANG['commands_loaded']}")
        if settings["autostart"]:
            self.root.after(1000, self._toggle)
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - 520) // 2
        y = (self.root.winfo_screenheight() - 680) // 2
        self.root.geometry(f"+{x}+{y}")
    def _build_ui(self):
        header = Frame(self.root, bg=THEME["bg2"], height=50)
        header.pack(fill="x")
        header.pack_propagate(False)
        logo = Label(header, text="🍵", font=("Segoe UI", 20), bg=THEME["bg2"], fg=THEME["accent"])
        logo.pack(side="left", padx=15)
        title = Label(header, text="T.UserBot", font=("Segoe UI", 12, "bold"), bg=THEME["bg2"], fg=THEME["fg"])
        title.pack(side="left")
        version = Label(header, text=VERSION, font=("Segoe UI", 8), bg=THEME["bg2"], fg=THEME["fg2"])
        version.pack(side="left", padx=5)
        self.status_dot = Label(header, text="●", font=("Segoe UI", 10), bg=THEME["bg2"], fg=THEME["fg2"])
        self.status_dot.pack(side="right", padx=5)
        self.status_text = Label(header, text=LANG["offline"], font=("Segoe UI", 8), bg=THEME["bg2"], fg=THEME["fg2"])
        self.status_text.pack(side="right")
        btn_frame = Frame(self.root, bg=THEME["bg"])
        btn_frame.pack(pady=15)
        self.start_btn = self._btn(btn_frame, LANG["start"], self._toggle, THEME["accent"])
        self.start_btn.pack(side="left", padx=5)
        self._btn(btn_frame, LANG["api_settings"], self._api_win, THEME["bg3"]).pack(side="left", padx=5)
        self._btn(btn_frame, LANG["settings"], self._settings_win, THEME["bg3"]).pack(side="left", padx=5)
        stats_frame = Frame(self.root, bg=THEME["bg2"])
        stats_frame.pack(fill="x", padx=15, pady=5)
        self.cmds_label = Label(stats_frame, text=f"📦 {len(self.commands)}", font=("Segoe UI", 10, "bold"), 
                                 bg=THEME["bg2"], fg=THEME["accent"])
        self.cmds_label.pack(side="left", padx=10, pady=8)
        Label(stats_frame, text=LANG["total_commands"], font=("Segoe UI", 8), 
              bg=THEME["bg2"], fg=THEME["fg2"]).pack(side="left", padx=5)
        console_frame = Frame(self.root, bg=THEME["bg"])
        console_frame.pack(fill="both", expand=True, padx=15, pady=5)
        self.console = scrolledtext.ScrolledText(console_frame, bg=THEME["console_bg"], fg=THEME["console_fg"],
                                                  font=(settings["console_font"], 9), relief="flat", borderwidth=0,
                                                  height=20)
        self.console.pack(fill="both", expand=True)
        footer = Frame(self.root, bg=THEME["bg2"], height=25)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)
        Label(footer, text=f"{TEAM} • {VERSION}", font=("Segoe UI", 7), 
              bg=THEME["bg2"], fg=THEME["fg2"]).pack(side="left", padx=10)
        Label(footer, text="code with tea 🍵", font=("Segoe UI", 7), 
              bg=THEME["bg2"], fg=THEME["fg2"]).pack(side="right", padx=10)
    def _btn(self, parent, text, cmd, bg_color):
        btn = Button(parent, text=text, command=cmd, bg=bg_color, fg=THEME["fg"],
                     font=("Segoe UI", 9), relief="flat", padx=15, pady=5,
                     activebackground=THEME["accent_hover"], activeforeground="white",
                     cursor="hand2")
        return btn
    def _update_console(self):
        self.console.delete(1.0, END)
        for msg in log_messages[-settings["console_lines"]:]:
            if settings["colored_output"]:
                if "✅" in msg or "✓" in msg:
                    self.console.insert(END, msg + "\n", "success")
                elif "❌" in msg or "✗" in msg:
                    self.console.insert(END, msg + "\n", "error")
                elif "⚠️" in msg:
                    self.console.insert(END, msg + "\n", "warning")
                else:
                    self.console.insert(END, msg + "\n", "info")
            else:
                self.console.insert(END, msg + "\n")
        if settings["colored_output"]:
            self.console.tag_config("success", foreground=THEME["accent"])
            self.console.tag_config("error", foreground=THEME["danger"])
            self.console.tag_config("warning", foreground="#E3B341")
            self.console.tag_config("info", foreground=THEME["fg"])
        self.console.see(END)
        self.root.after(500, self._update_console)
    def _toggle(self):
        global bot_running
        if not load_api()[0]:
            messagebox.showerror(LANG["api_settings"], LANG["no_api"])
            return
        if not self.running:
            self.running = True
            self.start_btn.config(text=LANG["stop"], bg=THEME["danger"])
            self.status_dot.config(fg=THEME["accent"])
            self.status_text.config(text=LANG["online"], fg=THEME["accent"])
            add_log("🚀 " + LANG["bot_started"])
            commands = load_commands()
            threading.Thread(target=run_bot_thread, args=(commands,), daemon=True).start()
        else:
            self.running = False
            self.start_btn.config(text=LANG["start"], bg=THEME["accent"])
            self.status_dot.config(fg=THEME["fg2"])
            self.status_text.config(text=LANG["offline"], fg=THEME["fg2"])
            add_log("⏹ " + LANG["bot_stopped"])
    def _api_win(self):
        win = Toplevel(self.root)
        win.title(LANG["telegram_api"])
        win.geometry("400x380")
        win.configure(bg=THEME["bg"])
        win.resizable(False, False)
        Label(win, text=LANG["telegram_api"], font=("Segoe UI", 11, "bold"), 
              bg=THEME["bg"], fg=THEME["fg"]).pack(pady=15)
        frame = Frame(win, bg=THEME["bg"])
        frame.pack(padx=20, pady=10)
        api_id, api_hash, phone = load_api()
        Label(frame, text=LANG["api_id"], bg=THEME["bg"], fg=THEME["fg2"]).pack(anchor="w")
        api_id_e = Entry(frame, bg=THEME["bg2"], fg=THEME["fg"], relief="flat")
        api_id_e.pack(fill="x", pady=(0,10))
        if api_id: api_id_e.insert(0, api_id)
        Label(frame, text=LANG["api_hash"], bg=THEME["bg"], fg=THEME["fg2"]).pack(anchor="w")
        api_hash_e = Entry(frame, bg=THEME["bg2"], fg=THEME["fg"], relief="flat", show="*")
        api_hash_e.pack(fill="x", pady=(0,10))
        if api_hash: api_hash_e.insert(0, api_hash)
        Label(frame, text=LANG["phone"], bg=THEME["bg"], fg=THEME["fg2"]).pack(anchor="w")
        phone_e = Entry(frame, bg=THEME["bg2"], fg=THEME["fg"], relief="flat")
        phone_e.pack(fill="x", pady=(0,5))
        if phone: phone_e.insert(0, phone)
        Label(frame, text=LANG["phone_format"], font=("Segoe UI", 7), 
              bg=THEME["bg"], fg=THEME["fg2"]).pack(anchor="w")
        def save():
            save_api(api_id_e.get(), api_hash_e.get(), phone_e.get())
            add_log(f"✅ {LANG['api_saved']}")
            messagebox.showinfo(LANG["api_saved"], LANG["api_saved"])
            win.destroy()
        btn_frame = Frame(win, bg=THEME["bg"])
        btn_frame.pack(pady=20)
        Button(btn_frame, text=LANG["save"], command=save, bg=THEME["accent"], fg="white",
               relief="flat", padx=20, cursor="hand2").pack(side="left", padx=5)
        Button(btn_frame, text=LANG["cancel"], command=win.destroy, bg=THEME["bg3"], fg=THEME["fg"],
               relief="flat", padx=20, cursor="hand2").pack(side="left", padx=5)
    def _settings_win(self):
        win = Toplevel(self.root)
        win.title(LANG["settings"])
        win.geometry("500x550")
        win.configure(bg=THEME["bg"])
        win.resizable(False, False)
        notebook = ttk.Notebook(win)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        tab_general = Frame(notebook, bg=THEME["bg"])
        notebook.add(tab_general, text=LANG["tab_general"])
        self._build_general_tab(tab_general)
        tab_appearance = Frame(notebook, bg=THEME["bg"])
        notebook.add(tab_appearance, text=LANG["tab_appearance"])
        self._build_appearance_tab(tab_appearance)
        tab_bot = Frame(notebook, bg=THEME["bg"])
        notebook.add(tab_bot, text=LANG["tab_bot"])
        self._build_bot_tab(tab_bot)
        tab_console = Frame(notebook, bg=THEME["bg"])
        notebook.add(tab_console, text=LANG["tab_console"])
        self._build_console_tab(tab_console)
        tab_about = Frame(notebook, bg=THEME["bg"])
        notebook.add(tab_about, text=LANG["tab_about"])
        self._build_about_tab(tab_about)
        btn_frame = Frame(win, bg=THEME["bg"])
        btn_frame.pack(pady=15)
        Button(btn_frame, text=LANG["save"], command=lambda: self._save_settings(win), 
               bg=THEME["accent"], fg="white", relief="flat", padx=25, cursor="hand2").pack(side="left", padx=5)
        Button(btn_frame, text=LANG["cancel"], command=win.destroy, 
               bg=THEME["bg3"], fg=THEME["fg"], relief="flat", padx=25, cursor="hand2").pack(side="left", padx=5)
        Button(btn_frame, text=LANG["reset"], command=self._reset_settings, 
               bg=THEME["danger"], fg="white", relief="flat", padx=25, cursor="hand2").pack(side="left", padx=5)
    def _build_general_tab(self, parent):
        frame = Frame(parent, bg=THEME["bg"])
        frame.pack(padx=20, pady=15, fill="both", expand=True)
        Label(frame, text=LANG["language"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0,5))
        self.lang_var = StringVar(value=settings["language"])
        lang_frame = Frame(frame, bg=THEME["bg"])
        lang_frame.pack(anchor="w", pady=(0,15))
        Radiobutton(lang_frame, text=LANGUAGES["ru"]["language"], variable=self.lang_var, value="ru",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        Radiobutton(lang_frame, text=LANGUAGES["en"]["language"], variable=self.lang_var, value="en",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        self.autostart_var = BooleanVar(value=settings["autostart"])
        Checkbutton(frame, text=LANG["autostart"], variable=self.autostart_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        self.minimize_var = BooleanVar(value=settings["minimize_to_tray"])
        Checkbutton(frame, text=LANG["minimize_to_tray"], variable=self.minimize_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        self.updates_var = BooleanVar(value=settings["check_updates"])
        Checkbutton(frame, text=LANG["check_updates"], variable=self.updates_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
    def _build_appearance_tab(self, parent):
        frame = Frame(parent, bg=THEME["bg"])
        frame.pack(padx=20, pady=15, fill="both", expand=True)
        Label(frame, text=LANG["theme"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0,5))
        self.theme_var = StringVar(value=settings["theme"])
        theme_frame = Frame(frame, bg=THEME["bg"])
        theme_frame.pack(anchor="w", pady=(0,15))
        for theme_key, theme_data in THEMES.items():
            Radiobutton(theme_frame, text=theme_data["name"], variable=self.theme_var, value=theme_key,
                        bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        Label(frame, text=LANG["font_size"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(10,5))
        self.font_var = StringVar(value=settings["font_size"])
        font_frame = Frame(frame, bg=THEME["bg"])
        font_frame.pack(anchor="w", pady=(0,15))
        Radiobutton(font_frame, text=LANG["small"], variable=self.font_var, value="small",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        Radiobutton(font_frame, text=LANG["medium"], variable=self.font_var, value="medium",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        Radiobutton(font_frame, text=LANG["large"], variable=self.font_var, value="large",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        self.icons_var = BooleanVar(value=settings["show_icons"])
        Checkbutton(frame, text=LANG["show_icons"], variable=self.icons_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        self.animation_var = BooleanVar(value=settings["animation"])
        Checkbutton(frame, text=LANG["animation"], variable=self.animation_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
    def _build_bot_tab(self, parent):
        frame = Frame(parent, bg=THEME["bg"])
        frame.pack(padx=20, pady=15, fill="both", expand=True)
        Label(frame, text=LANG["command_prefix"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0,5))
        self.prefix_var = StringVar(value=settings["command_prefix"])
        prefix_frame = Frame(frame, bg=THEME["bg"])
        prefix_frame.pack(anchor="w", pady=(0,15))
        Entry(prefix_frame, textvariable=self.prefix_var, bg=THEME["bg2"], fg=THEME["fg"], relief="flat", width=10).pack(side="left")
        Label(prefix_frame, text=f" ({LANG['default_prefix']})", bg=THEME["bg"], fg=THEME["fg2"]).pack(side="left", padx=5)
        self.reconnect_var = BooleanVar(value=settings["auto_reconnect"])
        Checkbutton(frame, text=LANG["auto_reconnect"], variable=self.reconnect_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        self.savelogs_var = BooleanVar(value=settings["save_logs"])
        Checkbutton(frame, text=LANG["save_logs"], variable=self.savelogs_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        Label(frame, text=LANG["max_commands_per_minute"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(10,5))
        self.max_cmd_var = StringVar(value=settings["max_commands_per_minute"] if settings["max_commands_per_minute"] > 0 else LANG["unlimited"])
        Entry(frame, textvariable=self.max_cmd_var, bg=THEME["bg2"], fg=THEME["fg"], relief="flat", width=15).pack(anchor="w")
    def _build_console_tab(self, parent):
        frame = Frame(parent, bg=THEME["bg"])
        frame.pack(padx=20, pady=15, fill="both", expand=True)
        Label(frame, text=LANG["console_lines"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0,5))
        self.lines_var = StringVar(value=settings["console_lines"])
        Entry(frame, textvariable=self.lines_var, bg=THEME["bg2"], fg=THEME["fg"], relief="flat", width=10).pack(anchor="w", pady=(0,15))
        Label(frame, text=LANG["console_font"], bg=THEME["bg"], fg=THEME["fg2"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0,5))
        self.font_var2 = StringVar(value=settings["console_font"])
        font_frame = Frame(frame, bg=THEME["bg"])
        font_frame.pack(anchor="w", pady=(0,15))
        Radiobutton(font_frame, text="Consolas", variable=self.font_var2, value="Consolas",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        Radiobutton(font_frame, text="Courier New", variable=self.font_var2, value="Courier New",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        Radiobutton(font_frame, text="Monospace", variable=self.font_var2, value="Monospace",
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(side="left", padx=10)
        self.timestamps_var = BooleanVar(value=settings["timestamps"])
        Checkbutton(frame, text=LANG["timestamps"], variable=self.timestamps_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        self.colors_var = BooleanVar(value=settings["colored_output"])
        Checkbutton(frame, text=LANG["colored_output"], variable=self.colors_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        self.autoclear_var = BooleanVar(value=settings["auto_clear"])
        Checkbutton(frame, text=LANG["auto_clear"], variable=self.autoclear_var,
                    bg=THEME["bg"], fg=THEME["fg"], selectcolor=THEME["bg"]).pack(anchor="w", pady=5)
        Button(frame, text=LANG["export_logs"], command=self._export_logs,
               bg=THEME["bg3"], fg=THEME["fg"], relief="flat", padx=20, cursor="hand2").pack(anchor="w", pady=10)
    def _build_about_tab(self, parent):
        frame = Frame(parent, bg=THEME["bg"])
        frame.pack(padx=20, pady=15, fill="both", expand=True)
        text = Text(frame, bg=THEME["bg"], fg=THEME["fg"], font=("Segoe UI", 10), 
                    relief="flat", wrap=WORD, height=15)
        text.pack(fill="both", expand=True)
        text.insert("1.0", LANG["about_text"])
        text.configure(state="disabled")
        link_frame = Frame(frame, bg=THEME["bg"])
        link_frame.pack(pady=10)
        Label(link_frame, text="GitHub: github.com/TeaDevs", bg=THEME["bg"], fg=THEME["accent"], cursor="hand2").pack()
    def _export_logs(self):
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("\n".join(log_messages))
            add_log("✅ Логи экспортированы")
            messagebox.showinfo("Успех", f"Логи сохранены в {file_path}")
    def _save_settings(self, win):
        global LANG, THEME
        settings["language"] = self.lang_var.get()
        settings["theme"] = self.theme_var.get()
        settings["autostart"] = self.autostart_var.get()
        settings["minimize_to_tray"] = self.minimize_var.get()
        settings["check_updates"] = self.updates_var.get()
        settings["font_size"] = self.font_var.get()
        settings["show_icons"] = self.icons_var.get()
        settings["animation"] = self.animation_var.get()
        settings["command_prefix"] = self.prefix_var.get()
        settings["auto_reconnect"] = self.reconnect_var.get()
        settings["save_logs"] = self.savelogs_var.get()
        max_cmd = self.max_cmd_var.get()
        settings["max_commands_per_minute"] = int(max_cmd) if max_cmd.isdigit() else 0
        settings["console_lines"] = int(self.lines_var.get()) if self.lines_var.get().isdigit() else 100
        settings["console_font"] = self.font_var2.get()
        settings["timestamps"] = self.timestamps_var.get()
        settings["colored_output"] = self.colors_var.get()
        settings["auto_clear"] = self.autoclear_var.get()
        save_settings()
        LANG = LANGUAGES[settings["language"]]
        THEME = THEMES[settings["theme"]]
        add_log(f"✅ {LANG['settings_saved']}")
        messagebox.showinfo(LANG["settings_saved"], LANG["settings_saved"])
        if settings["auto_clear"]:
            log_messages.clear()
        win.destroy()
        self.root.destroy()
        os.execv(sys.executable, [sys.executable] + sys.argv)
    def _reset_settings(self):
        if messagebox.askyesno(LANG["reset"], "Сбросить все настройки?"):
            global settings
            settings = default_settings.copy()
            save_settings()
            add_log("✅ Настройки сброшены")
            messagebox.showinfo(LANG["reset"], "Настройки сброшены. Перезапустите программу.")
            self.root.destroy()
            os.execv(sys.executable, [sys.executable] + sys.argv)
    def _on_close(self):
        if self.running:
            if messagebox.askokcancel(LANG["exit"], "Бот запущен. Остановить и выйти?"):
                self.running = False
                self.root.destroy()
        else:
            self.root.destroy()
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    if not os.path.exists("data/api_data.json"):
        first_run()
    commands = load_commands()
    app = TUserBotGUI(commands)
    app.run()