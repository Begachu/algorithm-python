def hannoi(src, dst, other, index):
    if index == 1 :
        #print(src, " ", dst)
        return 1, str(src)+" "+str(dst)
    else :
        intro = hannoi(src, other, dst, index-1)
        outro = hannoi(other, dst, src, index-1)
        result = intro[0]
        #print(src, " ", dst)
        result += outro[0]
        return 1 + result, intro[1]+"\n"+str(src)+" "+str(dst)+"\n"+outro[1]



if __name__=='__main__':
    index = int(input())
    result = hannoi(1, 3, 2, index)
    print(result[0])
    print(result[1])