_WaitSec = 900
_WarnDelaySec = 10

def run(sr):
    """Snow program batch job
    """
    yield sr.waitCmd('broadcast/type=warning "snow program starting up"')
    while True:
        for az in (135, 270, 45, 180, 315, 90, 225, 0):
            yield sr.waitCmd("track %s, 65 mount" % (az,))
            yield sr.waitSec(_WaitSec)
            yield sr.waitCmd('broadcast/type=warning "snow program moving to next position"')
            # make a small warning move, first
            yield sr.waitCmd("track %s, 75 mount" % (az - 0.1,))
            yield sr.waitSec(_WarnDelaySec)

def end(sr):
    sr.startCmd("axis init")
