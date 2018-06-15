def long_repeat(str):
    tmp = []
    num = []
    if(str==""):
        return 0
    for i in str:
        tmp.append(i)
    k=0
    j=1
    while k<len(tmp)-1:
        if tmp[k]==tmp[k+1]:
            j=j+1
            k=k+1
        else:
            num.append(j)
            j=1
            k=k+1
    num.append(j)
    return max(num)
if __name__=='__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')