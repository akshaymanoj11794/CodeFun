import math

def solve(g, h, p):
    count = pow(2,20)
    dic = {}
    # Baby step.
    for value in range(count):
        key = pow(g,value,p)
        dic[key]=value
    c = pow(g, count * (p - 2), p)
    for j in range(count):
        powe = pow(c,j,p)
        h_p =  h * powe
        y = h_p % p
        print dic
        if y in dic:
            return j * count + dic[y]
    return None

p = int(17)

h=pow(2,8,p)
print h
print(solve(2,h,p))