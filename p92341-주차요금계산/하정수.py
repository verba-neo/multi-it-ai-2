def solution(fees, records, n=None):
    d_time = fees[0]
    d_charge = fees[1]
    u_time = fees[2]
    u_charge = fees[3]
    cars = [record.split() for record in records]
    for n in range(len(cars)):
        if cars[n][2] == "IN":
            park_cars = {cars[n][1]: cars[n][0] for n in range(len(cars))}
    print(park_cars)
    answer = []

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
