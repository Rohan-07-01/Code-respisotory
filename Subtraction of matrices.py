M =input('Enter the number of rows of the matrix A:')
N =input('Enter the number of columns of the matrix A:')

M =int(M)
N =int(N)

print("The order of the matrix is", M, 'X', N);


if (M<=0 or N<=0):
    print("The matrix is not defined");
else:
    print("The matrix is defined");


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

P =input('Enter the number of rows of the matrix B:')
Q =input('Enter the number of columns of the matrix B:')

P =int(P)
Q =int(Q)

print("The order of the matrix is", P, 'X', Q);

if (P<=0 or Q<=0):
    print("The matrix is not defined");
else:
    print("The matrix is defined");


    from array import *
    B = [[0] * Q for x in range(P)]
    print(B)

    k=0
    l=0
            
    for k in list(range(P)):
        print("k = ", k);
        for l in list(range(Q)):
            print( "l = ", l);
            ROS =input('Enter the element of the kth row and lth column:')
            B[k][l] = int(ROS)
        print (B)

    from array import *
    C = [[0] * Q for x in range(P)]
    print("Matrix C is", C)

    for i in list(range(M)):
           for j in list(range(N)):
               C[i][j] =A[i][j]-B[i][j]

    print("The sum of the matrices is", C);
        
