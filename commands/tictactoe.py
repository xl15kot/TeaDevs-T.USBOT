"""
Команда .tictactoe — крестики-нолики
"""
ttt_games = {}
def ttt_render(board):
    rows = []
    for row in board:
        rows.append(" ".join("❌" if c=="X" else "⭕" if c=="O" else "⬜" for c in row))
    return "\n".join(rows)
def ttt_check(board):
    lines = [[(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
             [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
             [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]]
    for l in lines:
        v = [board[r][c] for r,c in l]
        if v[0] != " " and v[0] == v[1] == v[2]:
            return v[0]
    if all(board[r][c] != " " for r in range(3) for c in range(3)):
        return "draw"
    return None
async def execute(event, args, client, db):
    cid = event.chat_id
    if not args:
        ttt_games[cid] = {"board": [[" "]*3 for _ in range(3)], "turn": "X"}
        return f"❌⭕ **КРЕСТИКИ-НОЛИКИ**\n{ttt_render(ttt_games[cid]['board'])}\n.ttt <строка 1-3> <колонка 1-3>"
    if len(args) >= 2:
        if cid not in ttt_games:
            return "❌ .tictactoe — начать"
        try:
            row, col = int(args[0])-1, int(args[1])-1
            g = ttt_games[cid]
            board = g["board"]
            if board[row][col] != " ":
                return "❌ Клетка занята"
            board[row][col] = "X"
            w = ttt_check(board)
            if w == "X":
                del ttt_games[cid]
                return f"{ttt_render(board)}\n\n🎉 **Вы победили!**"
            elif w == "draw":
                del ttt_games[cid]
                return f"{ttt_render(board)}\n\n🤝 **Ничья!**"
            empty = [(r,c) for r in range(3) for c in range(3) if board[r][c] == " "]
            if empty:
                if (1,1) in empty:
                    board[1][1] = "O"
                else:
                    r2,c2 = random.choice(empty)
                    board[r2][c2] = "O"
            w = ttt_check(board)
            if w == "O":
                del ttt_games[cid]
                return f"{ttt_render(board)}\n\n💀 **Я победил!**"
            elif w == "draw":
                del ttt_games[cid]
                return f"{ttt_render(board)}\n\n🤝 **Ничья!**"
            return f"{ttt_render(board)}\n\nВаш ход ✏️"
        except:
            return "❌ .ttt <строка 1-3> <колонка 1-3>"
    return "❌ .tictactoe | .ttt <строка> <колонка>"
