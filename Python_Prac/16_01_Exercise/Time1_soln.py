class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """
def print_time(ti):
    print('%.2d:%.2d:%.2d' % (ti.hour, ti.minute, ti.second))

def is_after(ti1, ti2):
    if ti1.hour > ti2.hour:
        return True
    elif ti1.hour < ti2.hour:
        return False
    else:
        if ti1.minute > ti2.minute:
            return True
        elif ti1.minute < ti2.minute:
            return False
        else:
            if ti1.second > ti2.second:
                return True
            elif ti1.second < ti2.second:
                return False
            else:
                return False

#def add_time(ti1, ti2):
    #sum_ti = Time()
    #sum_ti.hour = ti1.hour + ti2.hour
    #sum_ti.minute = ti1.minute + ti2.minute
    #sum_ti.second = ti1.second + ti2.second
    #if sum_ti.second >= 60:
        #sum_ti.second -= 60
        #sum_ti.minute += 1
    #if sum_ti.minute >= 60:
        #sum_ti.minute -= 60
        #sum_ti.hour += 1

    #return sum_ti

def increment(time, seconds):
    time.second += seconds

    #if time.second >= 60:
    #while time.second >= 60:
        #time.second -= 60
        #time.minute += 1

    #if time.minute >= 60:
    #while time.minute >= 60:
        #time.minute -= 60
        #time.hour += 1
    time.minute += time.second / 60
    time.second = time.second % 60
    time.hour += time.minute / 60
    time.minute = time.minute % 60

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_time(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueErro('invalid Time object in add_time')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

increment(time, 130)

print_time(time)

t1 = Time()
t2 = Time()
t1.hour = 11
t1.minute = 59
t1.second = 30
t2.hour = 10
t2.minute = 59
t2.second = 30

print_time(t1)
print_time(t2)
print(is_after(t1, t2))

start = Time()
duration = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)



