def solution(priorities, location):
    order = [i for i in range(len(priorities))]
    idx = 0
    while True:
        target = priorities[idx]
        back_arr = [i for i in priorities[idx + 1:] if i > target]
        if len(back_arr) > 0:
            priorities.pop(0)
            priorities.append(target)
            pop_order = order.pop(idx)
            order.append(pop_order)
        elif idx < len(priorities) -1:
            idx += 1
        else:
            break
    return order.index(location) + 1