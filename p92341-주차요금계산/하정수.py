def solution(fees, records):
    split_records = [0] * len(records)
    parking_list = {}
    default_time = fees[0]
    default_fee = fees[1]
    use_time = fees[2]
    use_fee = fees[3]
    charges = {}
    for i in range(len(records)):
        split_records[i] = records[i].split()
    for n in range(len(records)):
        if split_records[n][2] == 'OUT':
            out_hour, out_minute = split_records[n][0].split(':')
            car_in = split_records[n][1]
            in_hour, in_minute = parking_list[car_in].split(':')
            total_time = (int(out_hour) - int(in_hour)) * 60 + int(out_minute) - int(in_minute)
            del parking_list[car_in]
            charge = default_fee
            minus_default = total_time - default_time
            if minus_default <= 0:
                charges[split_records[n][1]] += charge
                break
            else:
                charge += charge + [minus_default/use_time] * use_fee
            charges[split_records[n][1]] += charge
        elif split_records[n][2] == 'IN':
            parking_list[split_records[n][1]] = split_records[n][0]
            if split_records[n][1] not in charges:
                charges[split_records[n][1]] = 0
    print(charges)
    answer = []
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
