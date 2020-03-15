# finding max in a list

def get_max(A):
    m = A[0]
    for i in range(len(A)):
        if A[i] >= m:
            m = A[i]
    print(m)

get_max([4,3,2,1])
