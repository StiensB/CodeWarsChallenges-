#Bray Stiens
#Sqaure the indiviual digits within a given integer
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
