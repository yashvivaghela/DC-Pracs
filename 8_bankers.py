# this is to check if the process in in safe state of not
def check(i, need, available, allocated, r):  
    for j in range(r):
        if need[i][j]>available[j]:
            return False
    return True

#Initialize variables
p=5
r=4
sequence=[0]*p
visited=[0]*p
allocated = [[4,0,0,1],[1,1,0,0],[1,2,5,4],[0,6,3,3],[0,2,1,2]]
maximum = [[6,0,1,2],[1,7,5,0],[2,3,5,6],[1,6,5,3],[1,6,5,6]]
need=[[0 for j in range(r)]for i in range(p)]
for i in range(p):
    for j in range(r):
        need[i][j]= maximum[i][j]- allocated[i][j]

available = [3,2,1,1]

count=0  #count of processes that executed successfully
while count < p:
    temp=0
    for i in range(p):
        if not visited[i] and check(i, need, available, allocated, r):
            sequence[count]=i
            count=count+1
            visited[i]=1
            temp=1
            for j in range(r):
                available[j] += allocated[i][j]
    if temp==0:
        break

if count<p:
    print('The system is unsafe')
else:
    print("This system is safe")
    print("The safe sequence is", sequence)
    print("The available resources are", available)

            