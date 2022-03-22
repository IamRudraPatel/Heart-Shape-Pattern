a = int(input("Enter: "))
temp1 = a
temp2 = a-1
for i in range(1,a+1):
    print(" "*temp1+"*"*(2*i)+" "*(2*temp2)+"*"*(2*i))
    temp1-=1
    temp2-=1
temp3 = a*2
temp4 = temp3
for i in range(1,temp3+1):
    print(" "*i +"*"*(2*temp4))
    temp4-=1
