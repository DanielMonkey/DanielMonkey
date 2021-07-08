class Time:
    """Represents the time of day. """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    #def int_to_time(seconds):
        #time = Time()
        #minutes, time.second = divmod(seconds, 60)
        #time.hour, time.minute = divmod(minutes, 60)
        #return time

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()
print(start.time_to_int())
end = start.increment(1337)
end.print_time()
print(end.is_after(start))

time = Time()
#time.print_time()
print(time)
time = Time(9)
#time.print_time()
print(time)
time = Time(9, 45)
#time.print_time()
print(time)
time = Time(9, 45, 30)
time.print_time()
print(time)
start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start)



