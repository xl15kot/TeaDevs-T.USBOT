async def execute(event, args, client, db):
    from main import log_messages
    logs = "\n".join(log_messages[-30:])
    return f"📋 **ПОСЛЕДНИЕ ЛОГИ**\n```\n{logs}\n```"