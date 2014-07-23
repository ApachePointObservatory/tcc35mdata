"""Example batch job
"""

WaitSec = 1

def run(sr):
    """Simple test batch job
    """
    yield sr.waitCmd('broadcast "example batch job showing time"')
    yield sr.waitCmd("show time")
    yield sr.waitCmd('broadcast "example batch job waiting %s seconds"' % (WaitSec,))
    yield sr.waitSec(WaitSec)
    yield sr.waitCmd('broadcast "example batch job showing focus"')
    yield sr.waitCmd("show focus")


def end(sr):
    """Called after the job ends (whether it ends normally, or stopped, or fails)

    Do NOT yield or call sr.wait... methods in the end function!
    """
    sr.startCmd('broadcast "example batch job end function called"')
