index = 0

def PrintInfo(n,sFrom,sTo):
    global index
    index +=1
    print('第%d步，移动第%d号盘子，%s==>%s' % (index,n,sFrom,sTo))

def HanNuoTa(n,sFrom,sTo,sDepend):
    if n == 1:
        return PrintInfo(n,sFrom,sTo)
        
    HanNuoTa(n-1,sFrom,sDepend,sTo)

    PrintInfo(n,sFrom,sTo)
    
    HanNuoTa(n-1,sDepend,sTo,sFrom)

PanNum = int(input('请输出盘子数量：'))
HanNuoTa(PanNum,'A','C','B')
