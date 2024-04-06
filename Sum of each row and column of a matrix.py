M = input('Enter the number of rows of the matrix:')
N = input('Enter the number of columns of the matrix:')

M = int(M)
N = int(N)

if (M<=0 or N<=0):
    print("The matrix is not defined");
else:
    print("The matrix is defined");

    print("The order of the matrix is", M,'X',N);

    from array import *
    A = [[0] * N for x in range(M)]
    print(A)

    i=0
    j=0
        
    for i in list(range(M)):
        print("i = ", i);
        for j in list(range(N)):
            print( "j = ", j);
            COS =input('Enter the element of the ith row and jth column:')
            A[i][j] = int(COS)
        print (A)

    for i in list(range(M)):
        RSUM=0
        for j in list(range(N)):
            RSUM = RSUM + A[i][j]

        print("The sum of the rows are", RSUM);
    
    for i in list(range(N)):
        CSUM=0
        for j in list(range(M)):
            CSUM =CSUM + A[j][i]
        print("The sum of the columns are", CSUM);

    
        
