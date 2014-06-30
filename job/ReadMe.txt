TCC batch jobs (to be run using the Queue command).

Each job is implemented as one python module.
Each module must do one of the following:
- define a subclass of twistedActor.ScriptRunner named "ScriptClass", with "run" and optional "init" and "end" methods
- define a function named "run" and optional functions named "init" and "end".

To send a command to the TCC use:
    sr.startCmd(...)
or
    yield sr.waitCmd(...)

init and end (if present) must not yield or call wait methods.
