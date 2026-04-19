def changeRate(a,b): # 1盈利 -1亏损 后为绝对值
    res = round(b/a-1,4)
    if res>0 :
        return [1,res]
    else:
        return [-1,-res]

def win(a,b,wr):
    if changeRate(a,b)[0]>0 and changeRate(a,b)[1]>=wr:
        return True
    else:
        return False


def lose(a,b,lr):
    if changeRate(a,b)[0]<0 and changeRate(a,b)[1]>=lr:
        return True
    else:
        return False

def finalRate(w,l,wr,lr):
    return ((1+wr)**w*(1-lr)**l)-1

if __name__=='__main__':
    print(changeRate(5,4)[0])
    print(win(1,1.91,0.1))
    print(finalRate(31,46))
    print(finalRate(344,545))
    print(finalRate(332,665))
