import threading
import math

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True

def check_prime(start,end,result):
    primes=[]
    for i in range(start,end+1):
        if is_prime(i):
            primes.append(i)
    result.extend(primes)

result=[]
n=int(input("enter no of threads"))
data=int(1e6)  #10^6
chunk=data//n   #// is for integer division

thread=[]
for i in range(n):
    start= chunk*i +1
    end=(i+1)*chunk
    t=threading.Thread(target=check_prime,args=(start,end,result))
    thread.append(t)
    t.start()

for i in thread:
    t.join()

print(len(result))