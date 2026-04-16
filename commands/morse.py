"""
Команда .morse — азбука Морзе
"""
async def execute(event, args, client, db):
    if not args:
        return "❌ .morse <текст>"
    m = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
    text = " ".join(args).lower()
    result = " ".join(m.get(c,"?") for c in text if c != " ")
    return f"📡 `{result}`"
