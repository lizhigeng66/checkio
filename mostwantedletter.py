def search(str1):
    s = str1.lower()
    worddict={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for i in s:
        if i in worddict:
            worddict[i]=worddict[i]+1
    return max(worddict.items(),key=lambda x:x[1])[0]

if __name__=='__main__':
    assert search("Hello World!") == "l", "Hello test"
    assert search("How do you do?") == "o", "O is most wanted"
    assert search("One") == "e", "All letter only once."
    assert search("Oops!") == "o", "Don't forget about lower case."
    assert search("AAaooo!!!!") == "a", "Only letters."
    assert search("abe") == "a", "The First."
    print("Start the long test")
    assert search("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")