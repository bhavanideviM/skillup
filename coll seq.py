n=int(input())
i=3
while True:
    print(n, end=" ")
    if n==1:
        break
    if n%2:
       n=(n*i)+1
    else:
        n=n//2
   

