"""
Команда .qr — QR код
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .qr <текст>"
    text = "+".join(args)
    return f"📱 QR: https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
