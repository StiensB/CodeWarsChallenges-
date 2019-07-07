#Bray Stiens
#Sqaure the indiviual digits within a given integer
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
def square_digits(num):
    temp = 0
    arr = []
    numStr = str(num)
    for i in numStr:
       temp = int(i)
       temp = temp * temp
       arr.append(temp)
    str1 = ''.join(str(e) for e in arr)
    num = int(str1)
    return num
    pass
