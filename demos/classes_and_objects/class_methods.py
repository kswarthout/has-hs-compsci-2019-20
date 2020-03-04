##'{'property_name': 'value', 'another_property': 'value'}'

class Time:
    '''
    Represents the time of day.
    attributes: hour, minute, second
    '''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __str__(self):
        return '{:02d}:{:02d}:{:02d}'.format(int(self.hour), int(self.minute), int(self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
t1 = Time()
t2 = Time(2, 20, 20)
print(t1 + t2)
##print(t1)
