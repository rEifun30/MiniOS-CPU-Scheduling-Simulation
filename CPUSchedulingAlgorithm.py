def fcfs(process_list):
    time = 0
    gantt = []
    completed = {}
    totalWaitingTime = 0
    totalTurnaroundTime = 0
    process_list.sort()
    while process_list != []:
        if process_list[0][0] > time:
            time += 1
            continue
        else:
            process = process_list.pop(0)
            gantt.append(process[2])
            time += process[1]
            processID = process[2]
            completionTime = time
            turnaroundTime = completionTime - process[0]
            waitingTime = turnaroundTime - process[1]
            totalWaitingTime += waitingTime
            totalTurnaroundTime += turnaroundTime
            completed[processID] = [completionTime,turnaroundTime,waitingTime]
    
    print(f"Gantt Chart\n{gantt}")
    print(f"Completion Time - Turnaround Time - Waiting Time\n{completed}")
    print(f"Average Waiting Time: {totalWaitingTime/len(gantt):.2f}")
    print(f"Average Turnaround Time: {totalTurnaroundTime/len(gantt):.2f}")

def sjf(process_list):
    time = 0
    totalWaitingTime = 0
    totalTurnaroundTime = 0
    gantt = []
    completed ={}

    while process_list != []:
        available = []
        for p in process_list:
            if p[0] <= time:
                available.append(p)
        #No processes available
        if available == []:
            time += 1
            continue
        else:
            sortedproc = sorted(available, key=lambda x: x[1])
            process = sortedproc[0]
            #Service the process
            burst_time = process[1]
            processID = process[2]
            arrival_time = process[0]
            time += burst_time
            gantt.append(processID)
            completionTime = time
            turnaroundTime = completionTime - arrival_time
            waitingTime = turnaroundTime - burst_time
            totalWaitingTime += waitingTime
            totalTurnaroundTime += turnaroundTime
            process_list.remove(process)
            completed[processID] = [completionTime,turnaroundTime,waitingTime]

    print(f"Gantt Chart\n{gantt}")
    print(f"Completion Time - Turnaround Time - Waiting Time\n{completed}")
    print(f"Average Waiting Time: {totalWaitingTime/len(gantt):.2f}")
    print(f"Average Turnaround Time: {totalTurnaroundTime/len(gantt):.2f}")

def round_robin(process_list,time_quanta):
    time = 0
    totalWaitingTime = 0
    totalTurnaroundTime = 0
    processnum = 0
    gantt = []
    completed = {}
    #sort the processes wrt at
    process_list.sort()
    burst_times = {}
    for p in process_list:
        processID = p[2]
        burst_time = p[1]
        burst_times[processID] = burst_time
        processnum += 1
    while process_list != []:
        available = []
        for p in process_list:
            if p[0] <= time:
                available.append(p)
        #boundary condition 1
        if available == []:
            time += 1
            continue
        else:
            process = available[0] 
            #Service this process now
            gantt.append(process[2])
            #remove the process
            process_list.remove(process)
            #Update the burst time
            rem_burst = process[1]
            if rem_burst <= time_quanta:
                time += rem_burst
                completionTime = time
                processID = process[2]
                arrival_time = process[0]
                burst_time = burst_times[processID]
                turnaroundTime = completionTime - arrival_time
                waitingTime = turnaroundTime - burst_time
                totalWaitingTime += waitingTime
                totalTurnaroundTime += turnaroundTime
                completed[process[2]] = [completionTime,turnaroundTime,waitingTime]
                continue
            else:
                time += time_quanta
                process[1] -= time_quanta
                process_list.append(process)

    print(f"Gantt Chart\n{gantt}")
    print(f"Completion Time - Turnaround Time - Waiting Time\n{completed}")
    print(f"Average Waiting Time: {totalWaitingTime/processnum:.2f}")
    print(f"Average Turnaround Time: {totalTurnaroundTime/processnum:.2f}")



if __name__ == "__main__":
    process_list = []
    n = int(input("Enter the number of processes: "))

    for i in range(n):
        print(f"Enter the input for Process {i+1}: ")
        processID = f"P{i + 1}"
        arrivalTime = int(input("Enter Arrival Time: "))
        bursturnaroundTimeime = int(input("Enter Burst Time: "))

        a = [arrivalTime,bursturnaroundTimeime,processID]
        process_list.append(a)
    
    algorithm = int(input("1. FCFS\n2.SJN/SJF\n3.Round Robin\n>>> "))

if (algorithm == 1):
    fcfs(process_list)
elif (algorithm == 2):
    sjf(process_list)
elif (algorithm == 3):
    tq = int(input("Enter time quantum: "))
    round_robin(process_list,tq)

    
print("\nGoodbye!")  

