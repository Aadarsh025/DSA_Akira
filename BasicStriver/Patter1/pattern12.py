a=int(input())
for i in range(a):
    for j in range(i+1):
        print(j+1,end=" ")
    for j in range((2*a-2*i-1)):
        print(" ",end=" ")
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print("\n")