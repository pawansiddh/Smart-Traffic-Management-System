                                                             # Algorithm 1: Shortest Path Algorithm using Dynamic Programming
#Pseudocode:$$

function shortestPath(start, dest, traffic):
dist = array of distances from start to other nodes
prev = array of previous nodes in shortest path
set dist[start] = 0 and all other distances to infinity
for each node in graph:
calculate minimum distance using Dynamic Programming technique
update dist[] with minimum distance
update prev[] with previous node in shortest path
// Determine shortest path using prev[] array
path = []
current = dest
while current != start:
path.insert(0, current)
6
current = prev[current]
path.insert(0, start)
return path
