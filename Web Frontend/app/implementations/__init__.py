from inspect import getframeinfo

def whoami(frame): 
#    frame = inspect.currentframe()
    return getframeinfo(frame).function


