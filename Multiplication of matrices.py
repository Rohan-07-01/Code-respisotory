M = input('Enter the rows of matrix A:')
N = input('Ente the columns of matrix A:')

M = int(M)
N = int(N)

print("The order of matrix is", M, 'X', N);

if (M<=0 or N<=0):
    print("The order of the matrix is not defined");
else:
    print("The order of the matrix is defined");

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

P = input('Enter the rows of matrix B:')
Q = input('Enter the columns of matrix B:')

P = int(P)
Q = int(Q)

print("The order of the matrix is", P, 'X', Q);

if (P<=0 or Q<=0):
    print("The order of the matrix is not defined");
else:
    print("The order of the matrix is defined");


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


if (N!=P):
    print("We CANNOT multiply the two matrices");
else:
    print("We CAN multiply the two matrices");

    print("The order of the NEW matrix is", M, 'X', Q);
