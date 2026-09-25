def checkmate(board):
    # ตรวจสอบเบื้องต้น: ข้อมูลต้องเป็น string และไม่เป็น None หรือว่างเปล่า
    if not isinstance(board, str) or not board.strip():
        print("Error")
        return

    # แยกข้อความออกเป็นแถวๆ
    lines = board.strip().split("\n")
    size = len(lines)

    # 1. ตรวจสอบว่าตารางเป็นสี่เหลี่ยมจัตุรัสหรือไม่ (จำนวนคอลัมน์ต้องเท่ากับจำนวนแถว)
    for row in lines:
        if len(row) != size:
            print("Error")
            return

    # 2. ค้นหาตำแหน่งและนับจำนวน King (K)
    king_row = -1
    king_col = -1
    king_count = 0

    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_row = r
                king_col = c
                king_count += 1

    # ตรวจสอบว่าต้องมี King เพียง 1 ตัวเท่านั้น (ห้าม 0 ตัว และห้ามมากกว่า 1 ตัว)
    if king_count != 1:
        print("Error")
        return

    # 3. ตรวจสอบ Pawn (P): เล็งแทงขึ้นบน ดังนั้นจาก King ต้องมองลงล่าง (r + 1)
    pawn_row = king_row + 1
    for pawn_col in [king_col - 1, king_col + 1]:
        if 0 <= pawn_row < size and 0 <= pawn_col < size:
            if lines[pawn_row][pawn_col] == 'P':
                print("Success")
                return

    # 4. ตรวจสอบ 4 ทิศตรง (บน, ล่าง, ซ้าย, ขวา) -> R หรือ Q
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_dirs:
        r = king_row + dr
        c = king_col + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ['P', 'B', 'R', 'Q']:
                if piece == 'R' or piece == 'Q':
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc

    # 5. ตรวจสอบ 4 ทิศทแยง -> B หรือ Q
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_dirs:
        r = king_row + dr
        c = king_col + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ['P', 'B', 'R', 'Q']:
                if piece == 'B' or piece == 'Q':
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc

    # ถ้าตรวจครบหมดแล้ว King ปลอดภัย
    print("Fail")
