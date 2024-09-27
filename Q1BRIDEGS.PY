from collections import defaultdict
import heapq

n,m,k = map(int,input().split())
t =[0] + list(map(int,input().split()))
b = [list(map(int,input.split())) for _ in range(k)]
se = list(map(int,input().split()))
def iskland(n,m,k,t,b,se):
    g = defaultdict(list)
    for u,v,w in b:
        g[u].append((v,w))
        g[v].append((u,w))
        
    #dikstra
    def maxpath(start,end):
        pq=(-t[start],0,start)
        max_t = [-float("inf")]*(n+1)
        max_t[start] = t[start]
        min_time=[float("inf")]*(n+1)
        min_time[start]=0
        
        while pq:
            curr_t,curr_time ,island=heapq.heappop()
            curr-t = -curr_t
            
            if island == end:
                return curr_t,curr_time   

            for nei , travel in g[island]:
                next_t= curr_t+t[nei]
                next_time= curr_time+ travel
                
                if next_t > max_t[nei] or (next_t==max_t[nei]) and next_time<min_time[nei]:
                    max_t[nei]=next_t
                    min_time[nei]=next_time
                    heapq.heappush(pq,(-next_t,next_time,nei))
        return 0, float("inf")
    res=[]
    for start, end in se:
        tres ,time = maxpath(start,end)
        res.append((tres,time))
    
    return res
