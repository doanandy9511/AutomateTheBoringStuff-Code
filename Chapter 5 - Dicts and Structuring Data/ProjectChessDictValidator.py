from pprint import pprint

def isValidChessBoard(board):
    sides = ['w', 'b']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    coords = []
    for r in rows:
        for c in cols:
            coords.append(f'{r}{c}')
    w_pawns = 0
    b_pawns = 0
    w_pieces = 0
    b_pieces = 0
    for k,v in board.items():
        if k not in coords:
            return False
        side = v[0]
        piece = v[1:]
        # check if each value is either white or black
        if side in sides:
            # increment cnt for each player
            if side == 'w':
                w_pieces += 1
            else:
                b_pieces += 1
            if w_pieces > 16 or b_pawns > 16:
                return False
            # increment pawn cnt
            if piece in pieces:
                if piece == 'pawn':
                    if side == 'w':
                        w_pawns += 1
                    else:
                        b_pawns += 1
                    if w_pawns > 8 or b_pawns > 8:
                        return False
                print(v)
        else:
            return False
    return True

def main():
    chessBoard = {'1h': 'bking', 
                  '6c': 'wqueen', 
                  '2g': 'bbishop', 
                  '5h': 'bqueen', 
                  '3e': 'wking'}
    print(f'Chessboard valid: {isValidChessBoard(chessBoard)}')

if __name__ == '__main__':
    main()