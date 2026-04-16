import platform

async def execute(event, args, client, db):
    # Получаем информацию об ОС
    os_name = platform.system()
    os_version = platform.release()
    os_full = platform.platform()
    
    # Определяем дополнительные детали
    if os_name == "Windows":
        os_icon = "🪟"
        os_type = "Windows"
    elif os_name == "Linux":
        os_icon = "🐧"
        os_type = "Linux"
    elif os_name == "Darwin":
        os_icon = "🍎"
        os_type = "macOS"
    else:
        os_icon = "💻"
        os_type = os_name
    
    # Формируем ответ
    response = (
        f"{os_icon} **Операционная система**: {os_type}\n"
        f"📀 **Версия**: {os_version}\n"
        f"🔧 **Платформа**: {os_full}\n"
        f"🐍 **Python**: {platform.python_version()}"
    )
    
    return response