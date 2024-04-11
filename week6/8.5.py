for i in range(1,9):
    if i<8:
        print(f"{i}*n",end='\t')
    else:
        print(f"{i}*n")
for n in range(1,11):
    for i in range(1,9):
        if i<8:
            print(i*n,end='\t')
        else:
            print(i*n)