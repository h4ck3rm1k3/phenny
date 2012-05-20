# job scheduler for phenny

# low ^\.(hire)(?: +(.*))?$ <function hire at 0x7fefc9dbdd70>
# register worker
def hire (phenny, sinput):
    phenny.say("Hire")
    phenny.say(sinput)
hire.commands = ['hire']
hire.priority = 'low'

# low ^\.(task)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# register task to do
#    describe task details
def task (phenny, sinput):
    phenny.say("Task")
    phenny.say(sinput)
task.commands = ['task']
task.priority = 'low'

# low ^\.(offer)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# offer job to worker
#   split/send jobs to all online workers
def offer (phenny, sinput):
    phenny.say("Offer")
    phenny.say(sinput)
offer.commands = ['offer']
offer.priority = 'low'

# low ^\.(claim)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# claim task by worker
def claim (phenny, sinput):
    phenny.say("Claim")
    phenny.say(sinput)
claim.commands = ['claim']
claim.priority = 'low'

# low ^\.(start)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# start task by worker
#    estimate time needed
def start (phenny, sinput):
    phenny.say("Start")
    phenny.say(sinput)
start.commands = ['start']
start.priority = 'low'

# low ^\.(progress)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# progress on task by worker
#    log message 
def progress (phenny, sinput):
    phenny.say("Progress")
    phenny.say(sinput)
progress.commands = ['progress']
progress.priority = 'low'

# low ^\.(stop)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# finish task by worker
#    upload result links
def stop (phenny, sinput):
    phenny.say("Stop")
    phenny.say(sinput)
stop.commands = ['stop']
stop.priority = 'low'

# low ^\.(timeout)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# timeout worker, rollback all work
def timeout (phenny, sinput):
    phenny.say("Timeout")
    phenny.say(sinput)
timeout.commands = ['timeout']
timeout.priority = 'low'

# low ^\.(abort)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
# abort task by worker
def abort (phenny, sinput):
    phenny.say("Abort")
    phenny.say(sinput)
abort.commands = ['abort']
abort.priority = 'low'

# remove worker, close all jobs
# low ^\.(fire)(?: +(.*))?$ <function scheduler at 0x7fefc9dbdde8>
def fire (phenny, sinput):
    phenny.say("Fire")
    phenny.say(sinput)
fire.commands = ['fire']
fire.priority = 'low'

# create a project so we can assign tasks to it
def project (phenny, sinput):
    phenny.say("Project")
    phenny.say(sinput)
project.commands = ['project']
project.priority = 'low'


# define an input or output file (url)
def file (phenny, sinput):
    phenny.say("File")
    phenny.say(sinput)
file.commands = ['file']
file.priority = 'low'


## general scheduler (help)  function
# it could make a help page
def scheduler (phenny, sinput):
    phenny.say("Hello schedule")
    phenny.say(sinput)
scheduler.commands = ['scheduler']
scheduler.priority = 'low'








