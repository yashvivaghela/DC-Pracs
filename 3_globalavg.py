import numpy as np

num_nodes = 5   #5 nodes
data_size = 10   #10 elements in it 

learning_rate = 0.1
iterations = 1000  #for accuracy

data = [np.random.rand(data_size) for i in range(num_nodes)]   #getting data of random values

print(data)

global_avg = [0]*data_size #array of zeros

for i in range(iterations):
    for j in range(num_nodes):
        local_avg = data[j]
        local_avg -= (local_avg - global_avg) * learning_rate   #it ensures that each node's local model is influenced by the global model, but not too much. The learning rate controls how much influence the global model has on the local model.
        data[j] = local_avg
    
    global_avg = np.mean(data , axis=0)

print(global_avg)