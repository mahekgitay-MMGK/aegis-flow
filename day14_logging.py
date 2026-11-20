"""A brief introduction to logging.

Logging records events that occur while a program runs. These records help
developers understand program behavior, troubleshoot problems, and monitor
applications. Unlike temporary ``print`` statements, logs can be filtered by
severity and sent to destinations such as the console or a file.

Python's standard ``logging`` module provides levels to describe the
importance of an event:

* ``DEBUG``: detailed information useful during development.
* ``INFO``: confirmation that normal operations are working.
* ``WARNING``: an unexpected situation that does not prevent the program from
	continuing.
* ``ERROR``: a problem that caused an operation to fail.
* ``CRITICAL``: a serious problem that may stop the application.

A logger creates messages, handlers route them to destinations, and
formatters control their appearance. Levels can be configured to hide less
important messages, allowing the same application to be quiet in normal use
and more detailed during troubleshooting. Useful log messages include enough
context to explain what happened, but should never expose secrets such as
passwords or access tokens.
"""
# Example
"""def log(massage):
    f=open("log.txt","a")
    f.write(massage +"\n")
    f.close()

log("resume.pdf - cost 0.03 - ok")
log("notes.pdf - cost 0.10 - Too costly - stop")

f=open("log.txt","r")
print(f.read())
f.close()"""

def log(massage):
    f=open("log.txt","a")
    f.write(massage + "\n")
    f.close()
log("a.pdf - cost 0.02 - ok")
log("b.pdf - cost 0.08 - stop")

f=open("log.txt","r")
print(f.read())
f.close()