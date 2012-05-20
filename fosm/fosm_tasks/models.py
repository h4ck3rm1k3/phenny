from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    # tasks

class IrcClient(models.Model):
    handle = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # channel
    channels = models.ManyToManyField(IrcChannel, verbose_name="list of channels")
    # jobs 
    tasks = models.ManyToManyField(Task, verbose_name="list of tasks")

    # local files
    inputfiles = models.ManyToManyField(TaskFile, verbose_name="list of input files")
    localfiles = models.ManyToManyField(TaskFile, verbose_name="list of local files")
    outputfiles = models.ManyToManyField(TaskFile, verbose_name="list of output files")


class IrcServer(models.Model):
    handle = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    channels = models.ManyToManyField(IrcChannel, verbose_name="list of channels")

class IrcChannel(models.Model):
    server  = models.ForeignKey(IrcServer)
    project = models.ForeignKey(Project)
    # clients 
    clients = models.ManyToManyField(IrcClient, verbose_name="list of clients")
    # tasks
    tasks = models.ManyToManyField(Task, verbose_name="list of tasks")

class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    # channel
    channel= models.ForeignKey(IrcChannel)
    # input output files
    files = models.ManyToManyField(TaskFile, verbose_name="list of files")
    # client 
    client = models.ForeignKey(IrcClient)

    
class Role(models.Model):
    parent = models.ForeignKey(Role)    # recurse
    name   = models.CharField(max_length=255)

class TaskProcess(models.Model):
    client = models.ForeignKey(IrcClient)   
    #status on server
    status = models.ForeignKey(Role)   
    #transction
    start        = models.ForeignKey(TaskProcessEvent)  
    last_update  = models.ForeignKey(TaskProcessEvent)    
    stop         = models.ForeignKey(TaskProcessEvent)   

class TaskProcessEvent(models.Model):
    task = models.ForeignKey(TaskProcess)   
    time = models.DateField()
    status = models.ForeignKey(Role)   
    #status (starting, running, finishing)
    
class TaskFile(models.Model):
    #task
    creator = models.ForeignKey(TaskFile)
    #role: in or out
    role = models.ForeignKey(Role)   
    #url
    url = models.CharField(max_length=512)
    
