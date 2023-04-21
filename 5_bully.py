n = 0
pro = [0]*100  # priority number of each process
state = [0]*100  # state of each process
cr = 0  # current co-ordinator


def election(elec):
    global cr
    elec = elec-1
    cr = elec+1
    for i in range(n):
        if pro[elec] < pro[i]:
            print("the election message is sent from", elec+1, "to", i+1)
            if state[i] == 1:
                print(i+1, "send an ok message to", elec+1)
            if state[i] == 1:
                election(i+1)


print("Enter number of processes")
n = int(input())
for i in range(n):
    state[i] = 1
    pro[i] = i


choice = True
while choice:
    print("Enter a number")
    print("1. crash process")
    print("2. recover process")
    print("3. exit")
    ch = int(input())
    if ch == 1:
        print("ENter a process number")
        c = int(input())
        state[c-1] = 0
        cl = 1  # initate an election
    elif ch == 2:
        print("ENter a process number")
        c = int(input())
        state[c-1] = 1
        cl = 1
    elif ch == 3:
        choice = False
        cl = 0

    if cl == 1:
        print("Enter the process who will start the election")
        elec = int(input())
        election(elec)

print("Final coordinator is", cr)
