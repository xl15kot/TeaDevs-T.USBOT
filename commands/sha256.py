"""
Команда .sha256 — SHA256 хэш
"""
import hashlib
async def execute(event, args, client, db):
    if not args:
        return "❌ .sha256 <текст>"
    return f"🔐 SHA256: `{hashlib.sha256(' '.join(args).encode()).hexdigest()}`"
