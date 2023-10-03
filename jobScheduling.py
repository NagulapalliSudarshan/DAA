# def JS(d,j,n):
#     d[0] = j[0] = 0
#     j[1]=1
#     k=1

#     for i in range(2,n):
#         r = k
#         while d[j[r]] > d[i] and d[j[r]] != r : r-=1
#         if d[j[r]] <= d[i] and d[i]>r:
#             for q in range(k,r+1,-1):
#                 j[q+1]=j[q]
#             j[r+1] = i
#             k+=1
    
#     return k

def JS(p,d,n):
    index = list(range(n))
    index.sort(key=lambda i : p[i],reverse=True)

    ganttChart = [0]*n
    print(index)
    for i in index:
        if i!=0:
            if ganttChart[d[i]-1]!=0:
                j=d[i]-1
                while j>0:
                    if ganttChart[d[j]-1] == 0 :
                        ganttChart[d[j]-1]=p[d[i]]
                        break
                    j-=1
            else:
                ganttChart[d[i]-1] = p[d[i]]
        else:
            if ganttChart[d[i+1]-1]!=0:
                j=d[i+1]-1
                while j>0:
                    if ganttChart[d[j]-1] == 0 :
                        ganttChart[d[j]-1]=p[d[i+1]]
                        break
                    j-=1
            else:
                ganttChart[d[i+1]-1] = p[d[i+1]]

        print(ganttChart)
    
    print(*ganttChart)
    return sum(ganttChart)
    
print("Enter the dealines : ")
dealines=[int(x)for x in input().split()]

print("Enter the profits : ")
profits=[int(x)for x in input().split()]

n= len(dealines)

# jobs = list(range(1,n+1))

print(JS(profits,dealines,n))
 
