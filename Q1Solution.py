def findRent(start_time, end_time):

 # my code goes here 

    if start_time >= end_time or start_time < 0 or end_time > 24 or start_time > 24 or end_time < 0:
        print("Invalid input")
        return

    total_cost = 0

    for hour in range(start_time, end_time):
        if 0 <= hour < 7 or 21 <= hour <= 23:
            total_cost += 500
        elif 7 <= hour < 10 or 19 <= hour < 21:
            total_cost += 1000
        elif 10 <= hour < 19:
            total_cost += 1500

    print(f"The total amount to be paid is: RWF {total_cost}")
    return 0
start_time=int(input("Enter start time"))
end_time=int(input("Enter end time"))
print(findRent(start_time,end_time))
