Text = [222212,  2134, 11230]

if len(Text) > 0:
    A =Text[0]
    Text[0] = Text[-1]
    Text[-1] = A
    print(Text)
