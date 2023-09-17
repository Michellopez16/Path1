
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

mapa = np.array([   [0,1,1,1,1],
                    [1,1,0,1,1],
                    [1,0,0,0,1],
                    [1,0,1,1,1],
                    [1,0,0,1,1]
                ])

mapa = np.array([   [0,1,1,1,1,1],
                    [1,1,0,1,1,0],
                    [1,0,0,0,1,1],
                    [1,0,1,1,1,1],
                    [1,0,0,1,1,1]
                ])

start= (1,1)
goal = (4,4)
xlim,ylim = mapa.shape

visited = np.zeros (mapa.shape)
visited[start] +=1 
queue = deque([start])
path_visited = deque([start])
path = deque([start])

def stepprint(): 
    print(f"Visited:\n{visited}")
    print(f"Nodos por visitar: {queue}")
    print(f"Path Recorrido: {path_visited}")
    print(f"Mapa:\n{mapa}")
    
    
def validar (x,y):  
    if (x < xlim and y < ylim and x >=0 and y >= 0):
        if mapa[x,y] == 1 and not (x,y) in path_visited:            
            return True
    return False


def moverto(cur_node):
    x,y = cur_node
    
    if validar(x,y+1):
        return x,y+1
    if validar(x+1,y):
        return x+1,y
    if validar(x,y-1):
        return x,y-1
    if validar(x-1,y):
        return x-1,y
    
    return -1,-1    

stepprint()


cur_node = start
while cur_node != goal:
    print("-"*20)  
    #cur_node = queue.popleft()
    x,y = moverto(cur_node)
    print("Nuevo movimiento: ", x,y )

    if x == -1 and y == -1: # regresar
        
        #regresar 
        while path:
            x,y = path.pop()
            visited[x,y] += 1   
            print(x,y)
            
    else:            
        path_visited.append((x,y))
        path.append((x,y))
        visited[x,y] += 1
        #queue.append((x,y))
    cur_node = (x,y)
    
    #stepprint()

    
print("Fin")
print(path)
plt.imshow(visited,cmap='jet')
plt.show()