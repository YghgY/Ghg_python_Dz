
Text = [0, -1, 0, 12, 0, 3, 0, 0]

TextAmount = len(Text)
Num = 0

Text.sort(key=bool)

while 1 == 1:
    if Text[Num] == 0:
        A = Text.pop(Text[Num])
        Text.append(A)
    else:
        print(Text)
        break