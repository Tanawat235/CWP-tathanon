from checkmate import checkmate

def main():
    # ตัวอย่างกระดานขนาด 4x4
    # ในตัวอย่างนี้ R อยู่แนวเดียวกับ K ทางขวา จึงเล็งถึง K
    board = """\
....
.K.. 
..P. 
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
