queries = [3,2,1,2,6]
# output should be 17

def minimumWaitingTime(queries):
    queries.sort()
    waitTime = 0
    for idx, i in enumerate(queries):
        if idx == 0:
            count = 0
        else:
            count += queries[idx - 1]
        waitTime += count 
    return waitTime

print(minimumWaitingTime(queries))