class Time:
    '''
    Represents the time of day.
    attributes: hour, minute, second
    '''
    
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.hour >= 24 or time.minute >= 60 or time.seconds >= 60:
        return False
    return True

def add_time(t1, t2):
    ## Note: you only want one or the other
    
    ## call at beginning of function
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    
    ## using assert to validate a Time object
    assert valid_time(t1) and valid_time(t2)
    

