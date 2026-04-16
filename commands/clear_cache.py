import os
import shutil

async def execute(event, args, client, db):
    await event.edit("🧹 Очистка кэша...")
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
    for root, dirs, files in os.walk("commands"):
        if "__pycache__" in dirs:
            shutil.rmtree(os.path.join(root, "__pycache__"))
    if os.path.exists("data/__pycache__"):
        shutil.rmtree("data/__pycache__")
    return "✅ Кэш очищен!"