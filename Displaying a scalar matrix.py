M =input('Enter the number of rows of the matrix:')
N =input('Enter the number of columns of the matrix:')

M =int(M)
N =int(N)

print("The order of the matrix is", M, 'X', N);

if (M<=0 or N<=0):
    print("The matrix is not defined");
else:
    print("The matrix is defined");

if (M!=N):
    print("The matrix is not a square matrix");
else:
    print("The matrix is a square matrix");

    from array import *
    A = [[0] * M for x in range(N)]
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

    A11 = A[0][0]
    Scalar =True
    for i in list(range(M)):
        for j in list(range(N)):
            if (i==j):
                if (A[i][j]!=A[0][0]):
                    Scalar=False

    print(Scalar)

    if Scalar==True:
        for i in list(range(M)):
            for j in list(range(N)):
                if (i!=j and A[i][j]!=0):
                    print (A[i][j])
                    Scalar=False
    print(Scalar)
    if Scalar==True:
        print("It is scalar");
    else:
        print("Not a scalar");
        
    
