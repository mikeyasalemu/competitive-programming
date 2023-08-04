from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        # que = deque([0])
        
        vis = set()
        cycle = False
        
        
        for i in range(len(adj)):
            
            if i not in vis:
                que = deque([(i,None)])
                vis.add(i)
                
                while que:
                    node,par = que.popleft()
                    
                     
                    for val in adj[node]:
                        if val not in vis:
                            que.append((val,node))
                            vis.add(val)
                        elif val != par:
                            cycle = True
                            return cycle
                        
                    
                
                            
        return cycle
            

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends