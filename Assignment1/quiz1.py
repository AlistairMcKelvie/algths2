from random import randint
def makeRequests(time_start, time_stop, num_of_requests):
    requests = []
    distict_values = []
    loop_count = 0
    while len(requests) < num_of_requests:
        start = randint(time_start, time_stop - 1)
        stop = randint(start + 1, time_stop)
        if start not in distict_values and stop not in distict_values:
            distict_values.append(stop)
            distict_values.append(start)
            requests.append((start, stop))
        loop_count += 1
        if loop_count == 100000:
            raise RuntimeError('looped 100000 times without making valid request list')
    return requests

def byStartTime(req_list, print_list = False):
    requests = req_list[:]
    requests.sort(key=lambda x: x[0])
    chosen_requests = []
    while requests:
        chosen_request = requests.pop(0)
        chosen_requests.append(chosen_request)
        for i in range(len(requests) - 1, -1, -1):
            if requestsConfict(chosen_request, requests[i]):
                del requests[i]
    chosen_requests.sort(key=lambda x: x[0])
    if  print_list:
        print chosen_requests
    return len(chosen_requests)

def byLength(req_list, print_list = False):
    requests = req_list[:]
    requests.sort(key=lambda x: (x[1] - x[0]))
    chosen_requests = []
    while requests:
        chosen_request = requests.pop(0)
        chosen_requests.append(chosen_request)
        for i in range(len(requests) - 1, -1, -1):
            if requestsConfict(chosen_request, requests[i]):
                del requests[i]
    chosen_requests.sort(key=lambda x: x[0])
    if  print_list:
        print chosen_requests
    return len(chosen_requests)

def byFinishTime(req_list, print_list = False):
    requests = req_list[:]
    requests.sort(key=lambda x: (x[1]))
    chosen_requests = []
    while requests:
        chosen_request = requests.pop(0)
        chosen_requests.append(chosen_request)
        for i in range(len(requests) - 1, -1, -1):
            if requestsConfict(chosen_request, requests[i]):
                del requests[i]
    chosen_requests.sort(key=lambda x: x[0])
    if  print_list:
        print chosen_requests
    return len(chosen_requests)

def byMinConflicts(req_list, print_list = False):
    requests = req_list[:]
    for i in range(len(requests)):
        requests[i] = (requests[i][0], requests[i][1], countConflicts(requests, i))
    requests.sort(key=lambda x: (x[2]))
    chosen_requests = []
    while requests:
        chosen_request = requests.pop(0)
        chosen_requests.append(chosen_request)
        for i in range(len(requests) - 1, -1, -1):
            if requestsConfict(chosen_request, requests[i]):
                del requests[i]
    chosen_requests.sort(key=lambda x: x[0])
    if  print_list:
        print chosen_requests
    return len(chosen_requests)

def requestsConfict(req1, req2):
    if ((req1[0] >= req2[0] and req1[0] < req2[1]) or 
       (req2[0] >= req1[0] and req2[0] < req1[1])):
        return True
    else:
        return False

def countConflicts(requests, req_index):
    conf_count = 0
    for i in range(len(requests)):
        if i != req_index:
            if requestsConfict(requests[req_index], requests[i]):
                conf_count += 1
    return conf_count

def generateAndRunAll(time_start, time_stop, num_of_requests):
    requests = makeRequests(time_start, time_stop, num_of_requests)
    print requests
    print 'byStartTime', byStartTime(requests)
    print 'byLength', byLength(requests)
    print 'byFinishTime', byFinishTime(requests)
    print 'byMinConflicts', byMinConflicts(requests)

def loopUntilDiff(time_start, time_stop, num_of_requests):
    loop_count = 0
    bl = 0
    bft = 0
    bmc = 0
    while bft == bmc and loop_count < 100000:
        requests = makeRequests(time_start, time_stop, num_of_requests)
        bst = byStartTime(requests)
        bl = byLength(requests)
        bft = byFinishTime(requests)
        bmc = byMinConflicts(requests)
        loop_count += 1
    print 'byStartTime', byStartTime(requests, print_list = True)
    print 'byLength', byLength(requests, print_list = True)
    print 'byFinishTime', byFinishTime(requests, print_list = True)
    print 'byMinConflicts', byMinConflicts(requests, print_list = True)
    print 'loop_count', loop_count
    return requests