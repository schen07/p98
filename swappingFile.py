def swap():
    file1=input("enter the name of sample1")
    file2=input("enter the name of sample2")
    with open(sample1, 'r')as a:
        dataA=a.read()
    with open(sample2, 'r')as b:
        dataB=b.read()
    with open (sample1, 'w')as a:
        a.write(dataB)
    with open(sample2, 'w')as b:
        b.write(dataA)
swap()