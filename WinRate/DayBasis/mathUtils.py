def changeRate(a,b): # 1盈利 -1亏损 后为绝对值
    res = round(b/a-1,4)
    if res>0 :
        return [1,res]
    else:
        return [-1,-res]

def win(a,b,standard):
    if changeRate(a,b)[0]>0 and changeRate(a,b)[1]>=standard:
        return True
    else:
        return False


def lose(a,b,standard):
    if changeRate(a,b)[0]<0 and changeRate(a,b)[1]>=standard:
        return True
    else:
        return False

def finalRate(w,l):
    return ((1+0.1)**w*(1-0.05)**l)-1

if __name__=='__main__':
    print(changeRate(5,4)[0])
    print(win(1,1.91,0.1))
    print(finalRate(31,46))
    print(finalRate(344,545))
