import math


def solution(fees, records):
    parking_dic = {}
    fee_dic = {}
    for record in records:

        h_s, car_num, in_out = record.split()
        if in_out == "IN":
            parking_dic[str(car_num)] = h_s
            if car_num not in fee_dic:
                fee_dic[str(car_num)] = 0
        else:
            charge_h_s = parking_dic[str(car_num)].split(':')
            start_time = int(charge_h_s[0]) * 60 + int(charge_h_s[1])
            end_time_split = h_s.split(':')
            end_time = int(end_time_split[0]) * 60 + int(end_time_split[1])
            fee_dic[str(car_num)] += (end_time - start_time)
            del parking_dic[str(car_num)]

    if parking_dic:
        for car_num in parking_dic.keys():
            charge_h_s = parking_dic[car_num].split(':')
            start_time = int(charge_h_s[0]) * 60 + int(charge_h_s[1])
            end_time = 23 * 60 + 59
            fee_dic[str(car_num)] += (end_time - start_time)
        del parking_dic[str(car_num)]

    cal_fee = []
    for car_num in sorted(fee_dic):
        if fee_dic[car_num] <= fees[0]:
            cal_fee.append(fees[1])
        else:
            cal_fee.append(fees[1] + (math.ceil((fee_dic[car_num] - fees[0]) / fees[2])) * fees[3])
    print(cal_fee)


solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
