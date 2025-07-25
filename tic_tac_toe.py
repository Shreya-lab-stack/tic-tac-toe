# Tic-Tac-Toe with Unbeatable AI using Minimax Algorithm
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_board_full(board):
    return ' ' not in board

def check_winner(board, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Enter a valid number (1-9).")

def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def main():
    board = [' ' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe (You: X, AI: O)")
    print_board(board)

    while True:
        player_move(board)
        print("\nYour move:")
        print_board(board)
        if check_winner(board, 'X'):
            print("🎉 You win!")
            break
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

        print("\nAI's move:")
        ai_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("💻 AI wins!")
            break
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    main()