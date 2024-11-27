Text = [1, 21, 3,]
List1 = []
List2 = []
ListAmount = len(Text)
ListNum1 = int(ListAmount / 2)
if (ListAmount % 2) == 0:
    while ListNum1 > 0:
        List1.append(Text[ListNum1-1])
        List2.append(Text[-ListNum1])
        ListNum1 -= 1
else:
    while ListNum1 > 0:
        List2.append(Text[-ListNum1])
        ListNum1 -= 1

    while ListNum1 < (int(ListAmount / 2) +1):
        List1.append(Text[(ListNum1)])
        ListNum1 += 1

print(List1)
print(List2)