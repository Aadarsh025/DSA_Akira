a=int(input())
start=1
for i in range (a):
    for j in range(i+1):
        print(start,end=" ")
        start+=1
    print("\n")