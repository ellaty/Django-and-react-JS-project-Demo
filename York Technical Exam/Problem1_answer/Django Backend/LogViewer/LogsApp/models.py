from django.db import models

# Create your models here.

class Logs(models.Model):
    LogId = models.AutoField(primary_key=True)
    LOG_PRODUCER = models.CharField(max_length = 100)
    TIMESTAMP= models.DateTimeField()
    SEVERITY = models.IntegerField()
    LOG_MESSAGE= models.CharField(max_length =250)

