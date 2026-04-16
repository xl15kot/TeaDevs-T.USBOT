"""
Команда .md5 — MD5 хэш
"""
import hashlib
async def execute(event, args, client, db):
    if not args:
        return "❌ .md5 <текст>"
    return f"🔐 MD5: `{hashlib.md5(' '.join(args).encode()).hexdigest()}`"
