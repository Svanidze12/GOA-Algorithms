def hw1(num1,num2,num3):
    if num1 % num3 == 0 and num2 % num3 != 0:
        return int(num2 - num1) // num3 + 1
    else:
        return int(num2 - num1) // num3
    

print(hw1(12,19,3))
print(hw1(1,20,2))