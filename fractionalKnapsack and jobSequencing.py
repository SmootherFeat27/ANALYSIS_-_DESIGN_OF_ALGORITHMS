def knapsackProb(w,v,cap):
    items=[]
    for i in range(len(w)):
        items.append((w[i],v[i],v[i]/w[i]))
    items.sort(reverse=True)
    total=0
    for i,j,k in items:
        if cap>=i:
            total+=j
            cap-=i
        else:
            total+=k*cap
            break
    return total

def jobScheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    c=1
    end=jobs[0][1]
    for i in range(1,len(jobs)):
        if jobs[i][0]>=end:
            c+=1
            end=jobs[i][1]
    return c
