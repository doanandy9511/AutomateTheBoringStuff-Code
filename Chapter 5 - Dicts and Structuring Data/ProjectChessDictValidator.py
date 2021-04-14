
def isValidChessBoard(board):
    sides = ['w', 'b']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    w_pawns = 0
    b_pawns = 0
    w_pieces = 0
    b_pieces = 0
    for k,v in board.items():
        side = v[0]
        piece = v[1:]
        # check if each value is either white or black
        if side in sides:
            if side == 'w':
                w_pieces += 1
            else:
                b_pieces += 1
            if piece in pieces:
                if piece == 'pawn':
                    if side == 'w':
                        w_pawns += 1
                    else:
                        b_pawns += 1
                print(v)
        else:
            return false


def main():
    chessBoard = {'1h': 'bking', 
                  '6c': 'wqueen', 
                  '2g': 'bbishop', 
                  '5h': 'bqueen', 
                  '3e': 'wking'}
    isValidChessBoard(chessBoard)

if __name__ == '__main__':
    main()