MSPerSec = 1000

_WaitMS = 900 * MSPerSec
_WarnDelayMS = 10 * MSPerSec

def run(sr):
    """Snow program batch job
    """
    while True:
        yield sr.waitCmd('broadcast/type=warning "snow program starting up"')
        for az in (135, 270, 45, 180, 315, 90, 225, 0):
            yield sr.waitCmd("track %s, 65 mount" % (az,))
            yield sr.waitMS(_WaitMS)
            yield sr.waitCmd('broadcast/type=warning "snow program moving to next position"')
            # make a small warning move, first
            yield sr.waitCmd("track %s, 65 mount" % (az - 0.1,))
            yield sr.waitMS(_WarnDelayMS)

def end(sr):
    sr.startCmd("axis init")
