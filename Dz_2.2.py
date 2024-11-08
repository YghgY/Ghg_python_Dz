print("Please enter four number:")
Numbers =input()
num1 = int(Numbers) // 1000
num2 = ((int(Numbers) - num1*1000) // 100)
num3 = ((int(Numbers)- (num1*1000 + num2*100)) // 10 )
num4 = (int(Numbers)- (num1*1000 + num2*100 + num3*10) )
print((num4*1000)+(num3*100)+(num2*10)+num1)