def GreedyKnapSack(p,w,m,n):
    index = list(range(n))
    PWratio = [p[i]/w[i] for i in index]
    # print(PWratio)
    index.sort(key=lambda i:PWratio[i],reverse=True)
    # print(index)
    # print(PWratio)
    maxVal = 0
    x=[0]*n
    u=m
    for i in index:
        if w[i]>u : 
            break
        x[i] = 1
        maxVal += p[i]*x[i]
        u=u-w[i]
        print(x,maxVal)
    if i<=n:
        x[i] = u/w[i]
    maxVal += p[i]*x[i]
    print(x,maxVal)
    
    return maxVal,x

# weight of the knapsack 
m= int(input("Enter m (knapsack max weight) :"))

print("Enter the profits : ",end=" ")
profits = [int(x) for x in input().split()]

print("Enter the weights : ",end=" ")
weights = [int(x) for x in input().split()]

print(GreedyKnapSack(profits,weights,m,len(profits)))