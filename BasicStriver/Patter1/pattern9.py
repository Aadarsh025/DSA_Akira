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

a = int(input())

for i in range(a):
    print(" "*(a-i)+"*"*(2*i+1))
for i in range(a):
    print(" "*(i+1)+"*"*(2*(a-i-1)+1))