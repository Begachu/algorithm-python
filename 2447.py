default_star = [["*","*","*"],["*"," ","*"],["*","*","*"]]

def star_array(index):
    if index == 1:
        return default_star
    else:
        _temp_star = star_array(index-1)
        size = len(_temp_star)
        
        _star = []
        for i in range(size*3):
            _star.append([])
        
        for r in range(3):
            for c in range(3):
                if r==1 and c==1:
                    blank = ''.join(_temp_star[0]).replace("*", " ")
                    for i in range(size):
                        _star[size*r+i].append(blank)
                        
                else:
                    for i in range(size):
                        _star[size*r+i].append(''.join(_temp_star[i]))
        return _star

if __name__ == "__main__":
    N = int(input())
    k = 0
    while N > 1:
        N /= 3
        k += 1

    result = star_array(k)
    for line in result:
        print(''.join(line))