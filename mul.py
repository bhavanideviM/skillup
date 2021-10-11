num,r1,r2=map(int,input('enter a number').split())
while r1!=r2:
    print(num,"x",r1,"=",num*r1)
    if r2>r1:
        r1+=1
    else:
        r1-=1
if r1==r2:
    print(num,"x",r1,"=",num*r1)
