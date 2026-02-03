box = {
    1: 860,
    2: 15,
    3: 1,
    4: 1,
    5: 3
}

line =1
answer_A = None
answer_B = None

## DOUBLE-JUMP X on LINEY   คือ เปลี่ยนเลขใน BOX X *2   then ไป LINE Y+X  แล้วไปคำสั่งถัดไป
while True:
    # LINE 1
    if line == 1:
        box[5] *= 2
        line = 1 + 5

    # LINE 2
    elif line == 2:
        box[3] *= 2
        line = 2 + 3

    # LINE 3
    elif line == 3:
        box[2] += box[5]
        line = 7

    # LINE 4
    elif line == 4:
        answer_A = box[3]
        line = 1

    # LINE 5
    elif line == 5:
        box[4] += box[3]
        line = 3

    # LINE 6
    elif line == 6:
        box[3] += box[4]
        line = 2

    # LINE 7
    elif line == 7:
        if box[2] > 100:
            line = 9
        else:
            line = 8

    # LINE 8
    elif line == 8:
        if box[2] > 50:
            line = 4
        else:
            line = 1

    # LINE 9
    elif line == 9:
        answer_B = box[3]
        line = 10

    # LINE 10
    elif line == 10:
        break


print(answer_A)
print(answer_B)