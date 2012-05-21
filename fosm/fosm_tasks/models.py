from django.db import models

class Role(models.Model):
    parent = models.ForeignKey("Role",blank=True,null=True)    # recurse, forward to itself
    name   = models.CharField(max_length=255)

class Document(models.Model):
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=2048)
    url = models.CharField(max_length=512)
    role = models.ForeignKey(Role)   

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    # documents
    docs = models.ManyToManyField(Document,blank=True,null=True, verbose_name="list of documents")
    servers = models.ManyToManyField("IrcServer",related_name="in_project",blank=True,null=True, verbose_name="list of irc servers")

class IrcServer(models.Model):
    project = models.ForeignKey(Project)   
    handle = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    channels = models.ManyToManyField("IrcChannel",related_name="on_server",blank=True,null=True, verbose_name="list of channels")


class IrcChannel(models.Model):
    name = models.CharField(max_length=255)
    topic = models.CharField(max_length=512)
    server  = models.ForeignKey(IrcServer)
    project = models.ForeignKey(Project)
    # clients 
    clients = models.ManyToManyField("IrcClient",blank=True,null=True, verbose_name="list of clients")
    # tasks
    tasks = models.ManyToManyField("Task",blank=True,null=True, verbose_name="list of tasks")
  


    
class TaskFile(models.Model):
    #task
#    creator = models.ForeignKey("TaskFileEvent",blank=True,null=True)
    #role: in or out
    role = models.ForeignKey(Role)   
    #url
    url = models.CharField(max_length=512)
    
class IrcClient(models.Model):
    handle = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # channel
    channels = models.ManyToManyField(IrcChannel, blank=True,null=True,verbose_name="list of channels")
    # jobs 
    tasks = models.ManyToManyField("Task",blank=True,null=True, verbose_name="list of tasks")

    # local files
    inputfiles = models.ManyToManyField(TaskFile, blank=True,null=True,related_name="inputto",verbose_name="list of input files")
    localfiles = models.ManyToManyField(TaskFile, blank=True,null=True,related_name="localto", verbose_name="list of local files")
    outputfiles = models.ManyToManyField(TaskFile, blank=True,null=True,related_name="outputfrom", verbose_name="list of output files")

class Task(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    # channel
    channel= models.ForeignKey(IrcChannel,blank=True,null=True,)
    # input output files
    files = models.ManyToManyField(TaskFile,blank=True, null=True,verbose_name="list of files")
    # client 
    client = models.ForeignKey(IrcClient,blank=True,null=True,)


class TaskProcess(models.Model):
    client = models.ForeignKey(IrcClient)   
    #status on server
    status = models.ForeignKey(Role)   
    #transction
    start        = models.ForeignKey("TaskProcessEvent",related_name="start_process",blank=True,null=True,)  
    last_update  = models.ForeignKey("TaskProcessEvent",related_name="update_process",blank=True,null=True,)    
    stop         = models.ForeignKey("TaskProcessEvent",related_name="stop_process",blank=True,null=True,)   

class TaskProcessEvent(models.Model):
    task = models.ForeignKey(TaskProcess)   
    time = models.DateField()
    status = models.ForeignKey(Role)   
    #status (starting, running, finishing)


