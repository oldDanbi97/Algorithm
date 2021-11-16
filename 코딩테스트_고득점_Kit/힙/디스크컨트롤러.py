import heapq
def solution(jobs):
    answer = 0
    jobs_len = len(jobs)
    cur_time = 0
    start_time = 0
    heap = []
    finished = 0
    while finished < jobs_len:
        for st, rt in jobs:
            if start_time <= st < cur_time:
                heapq.heappush(heap, [rt, st])
        if heap:
            rt, st = heapq.heappop(heap)
            start_time = cur_time
            cur_time += rt
            answer += cur_time - st - 1
            finished += 1
        else: 
            cur_time += 1
    return answer // jobs_len
#print(solution([[0, 10], [4, 10], [15, 2], [5, 11]]))
print(solution([[0, 3], [1, 9], [2, 6]]))