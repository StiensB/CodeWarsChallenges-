#Bray Stiens
#Find the shortest word in a given string
def find_short(s):
    lst = s.split()
    lStr = min(lst, key=len)
    l = len(lStr)
    return l # l: shortest word length
