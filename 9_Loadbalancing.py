class RoundRobin():
    def __init__ (self):
        self.servers =[]
        self.current_index=0
    def add_servers(self, server_name) :
        self.servers.append(server_name)

    def nextserver(self):
        if not self.servers:
            return None
        server=self.servers[self.current_index]
        self.current_index = (self.current_index+1)% len(self.servers)
        return server

loadbalance=RoundRobin()
loadbalance.add_servers("Server 1")
loadbalance.add_servers("Server 2")
loadbalance.add_servers("Server 3")
print("Enter Number of requests")
n=int(input())
for i in range(n):
    server=loadbalance.nextserver()
    print(i+1, ":" , server)




        