n = int(input())

while n != 0:
    l = list()
    x = str(input())
    for i in x:
        if i == "(":
            l.append("(")
        elif i == ")":
            if len(l) == 0:
                l.append(")") 
            elif l[-1] == "(":
                l.pop()
            else:
                l.append(")")
                
    if len(l) == 0:
        print("YES")
    else:
        print("NO")
    n-=1