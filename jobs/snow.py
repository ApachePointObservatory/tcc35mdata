Alt=75
WaitSec = 900
WarnSec = 10

def run(sr):
    """Snow program batch job
    """
    yield sr.waitCmd('broadcast/type=warning "snow program starting up"')
    while True:
        for az in (135, 270, 45, 180, 315, 90, 225, 0):
            yield sr.waitCmd("track %s, %s mount" % (az, Alt))
            yield sr.waitSec(WaitSec)
            yield sr.waitCmd('broadcast/type=warning "snow program moving to next position"')
            # make a small warning move, first
            yield sr.waitCmd("track %s, %s mount" % (az - 0.1, Alt))
            yield sr.waitSec(WarnSec)

def end(sr):
    sr.startCmd("axis stop")
