import math

# --- Cấu hình trò chơi ---
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Biến đếm số lần duyệt để so sánh hiệu năng
nodes_visited = 0

def print_board(board):
    print("-" * 13)
    for row in board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("-" * 13)

def check_winner(board):
    # Kiểm tra hàng ngang và dọc
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # Kiểm tra đường chéo
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # Kiểm tra hòa
    is_full = True
    for row in board:
        if EMPTY in row:
            is_full = False
            break
    if is_full:
        return 'Draw'
    return None

def minimax_alpha_beta(board, depth, is_maximizing, alpha, beta):
    global nodes_visited
    nodes_visited += 1 # Đếm số node đã duyệt
    
    result = check_winner(board)
    if result == AI: return 10 - depth
    elif result == HUMAN: return depth - 10
    elif result == 'Draw': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    # Gọi đệ quy với alpha và beta
                    score = minimax_alpha_beta(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
                    
                    # Cập nhật Alpha
                    alpha = max(alpha, best_score)
                    
                    # Cắt tỉa (Pruning)
                    if beta <= alpha:
                        return best_score
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax_alpha_beta(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
                    
                    # Cập nhật Beta
                    beta = min(beta, best_score)
                    
                    # Cắt tỉa (Pruning)
                    if beta <= alpha:
                        return best_score
        return best_score

def get_best_move(board):
    global nodes_visited
    nodes_visited = 0 # Reset bộ đếm
    best_score = -math.inf
    move = (-1, -1)
    
    # Khởi tạo Alpha = -vô cùng, Beta = +vô cùng
    alpha = -math.inf
    beta = math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax_alpha_beta(board, 0, False, alpha, beta)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
                # Cập nhật alpha ngay tại root để cắt tỉa sớm hơn
                alpha = max(alpha, best_score)
                
    print(f"Số trạng thái đã duyệt (Nodes visited): {nodes_visited}")
    return move

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe (Alpha-Beta Pruning): Bạn là X, AI là O")
    print_board(board)

    while True:
        # --- Lượt người chơi ---
        while True:
            try:
                row = int(input("Nhập hàng (0, 1, 2): "))
                col = int(input("Nhập cột (0, 1, 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("Ô không hợp lệ. Thử lại!")
            except ValueError:
                print("Vui lòng nhập số!")

        print_board(board)
        
        result = check_winner(board)
        if result:
            if result == 'Draw': print("Hòa!")
            else: print(f"Người chơi ({result}) thắng!")
            break

        # --- Lượt AI ---
        print("AI đang tính toán...")
        ai_move = get_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI
        print(f"AI chọn ô: {ai_move}")
        print_board(board)

        result = check_winner(board)
        if result:
            if result == 'Draw': print("Hòa!")
            else: print(f"AI ({result}) thắng!")
            break

if __name__ == "__main__":
    play_game()  c[i] = a[i] + b[i]
print(c)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

class Sach:
  dic_sach = {"masach": [],
              "tensach": [],
              "dongia": [],
              "soluong": [],
              }
  def __init__(self, n):
    for i in range(n):
      ma = input("Nhap ma sach: ")
      ten = input("Nhap ten sach: ")
      dg = float(input("Nhap don gia: "))
      sl = int(input("Nhap so luong: "))
      self.dic_sach['masach'].append(ma)
      self.dic_sach['tensach'].append(ten)
      self.dic_sach['dongia'].append(dg)
      self.dic_sach['soluong'].append(sl)
Sach(3)
print(Sach.dic_sach)
print("Tong so luong sach: " + str(sum(Sach.dic_sach["soluong"])))
for i in range(len(Sach.dic_sach["masach"])):
  if Sach.dic_sach["soluong"][i] > 10:
    print(Sach.dic_sach["tensach"][i])
