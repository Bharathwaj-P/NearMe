N=int(input())
X=int(input())
sum=0
for i in range(1,N+1):
    if i%2!=0:
        sum+=pow(X,i)
        sum+=i
    print(sum)
