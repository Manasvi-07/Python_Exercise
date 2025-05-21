from datetime import datetime, timedelta, time

def remove_night_hours(start, end):
    if end <= start:
        return timedelta(0)

    total = timedelta(0)
    current = start

    while current < end:
        start_day = datetime.combine(current.date(), time(6, 0))  
        end_day = datetime.combine(current.date() + timedelta(days=1), time(0, 0))

        interval_start = max(current, start_day)
        interval_end = min(end, end_day)

        if interval_start < interval_end:
            total += interval_end - interval_start

        current = datetime.combine(current.date() + timedelta(days=1), time(0, 0))

    return total

start_input = input("Enter Start time : ")
start_time1 = datetime.strptime(start_input, "%Y-%m-%d %H:%M:%S") 
end_input = input("Enter End time : ")
end_time1 = datetime.strptime(end_input, "%Y-%m-%d %H:%M:%S")

diff = remove_night_hours(start_time1, end_time1)
print(diff)
