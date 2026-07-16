a=int(input())
for i in range(a):
    for j in range(a-i):
        print("*",end="")
    print("\n",end="")


#second way :-
# a=int(input())
# for i in range(a):
#    for j in range(a,i,-1):
#        print("*",end="")
#    print("\n",end="")