#a=int(input())
#for i in range(a):
    #for j in range(a-i):
        #print(" ",end="")
    #for j in range(2*i+1):
        #print("*",end="") 
    #print("\n",end="")
#for i in range(a):
    #for j in range(i+1):
        #print(" ",end="")
    #for j in range(2*(a-i-1)+1):
        #print("*",end="") 
    #print("\n",end="")

n = int(input())
# Upper half
for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + 1))

# Lower half
for i in range(n):
    print(" " * (i + 1) + "*" * (2 * (n - i - 1) + 1))