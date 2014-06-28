TCC batch jobs (to be run using the Queue command).

Each job is implemented as one python module.
Each module defines either one subclass of twistedActor.ScriptRunner named ScriptClass,
or else a run function and optional init and end functions.

To send a command to the TCC use:
    sr.startCmd(...)
or
    yield sr.waitCmd(...)

The end function must not ever call wait methods or yield.