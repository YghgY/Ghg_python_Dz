
#[3, 4, 2, 5, 2, 3, 23, 13, 89, 2]
Text = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 5]

Num = 0
NumNeed = int()
TextAmount = len(Text)

while Num < TextAmount:
    NumNeed = (int(NumNeed) + int(Text[Num]))
    Num += 2
NumNeed =NumNeed * Text[-1]
print(NumNeed)