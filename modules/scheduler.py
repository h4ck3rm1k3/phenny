# job scheduler for phenny

# register worker
def hire (phenny, sinput):
    phenny.say("Hire")
    phenny.say(sinput)

hire.commands = ['hire']
hire.priority = 'low'

# register task to do
#    describe task details
def task (phenny, sinput):
    phenny.say("Task")
    phenny.say(sinput)

task.commands = ['task']
task.priority = 'low'

# offer job to worker
#   split/send jobs to all online workers

def offer (phenny, sinput):
    phenny.say("Offer")
    phenny.say(sinput)

offer.commands = ['offer']
offer.priority = 'low'


# claim task by worker
def claim (phenny, sinput):
    phenny.say("Claim")
    phenny.say(sinput)

claim.commands = ['claim']
claim.priority = 'low'

# start task by worker
#    estimate time needed
def claim (phenny, sinput):
    phenny.say("Claim")
    phenny.say(sinput)

claim.commands = ['claim']
claim.priority = 'low'

# progress on task by worker
#    log message 
def claim (phenny, sinput):
    phenny.say("Claim")
    phenny.say(sinput)

claim.commands = ['claim']
claim.priority = 'low'

# finish task by worker
#    upload result links
def claim (phenny, sinput):
    phenny.say("Claim")
    phenny.say(sinput)
claim.commands = ['claim']
claim.priority = 'low'

# abort task by worker
def abort (phenny, sinput):
    phenny.say("Abort")
    phenny.say(sinput)
abort.commands = ['abort']
abort.priority = 'low'

# timeout worker, rollback all work
def timeout (phenny, sinput):
    phenny.say("Timeout")
    phenny.say(sinput)

timeout.commands = ['timeout']
timeout.priority = 'low'

# remove worker, close all jobs
def scheduler (phenny, sinput):
    phenny.say("Hello schedule")
    phenny.say(sinput)

scheduler.commands = ['scheduler']
scheduler.priority = 'low'
