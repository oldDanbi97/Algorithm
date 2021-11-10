def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing_truck = [0 for i in range(bridge_length)]
    truck_num = len(truck_weights)
    passed_count = 0
    again = True
    while again:
        weigth_sum = sum(crossing_truck)
        truck_num_in_bridge = len([i for i in crossing_truck if i != 0])
        for i in range(bridge_length):
            answer += 1
            tmp = crossing_truck.pop(0)
            if tmp != 0:
                weigth_sum = sum(crossing_truck)
                truck_num_in_bridge = len([i for i in crossing_truck if i != 0])
                passed_count += 1
            crossing_truck.append(0)
            if truck_weights and truck_num_in_bridge < bridge_length and weigth_sum + truck_weights[0] <= weight:
                if truck_weights:
                    crossing_truck[-1] = truck_weights.pop(0)
                    truck_num_in_bridge = len([i for i in crossing_truck if i != 0])
                    weigth_sum = sum(crossing_truck)
            if not truck_weights and passed_count == truck_num:
                again = False
                break
    return answer