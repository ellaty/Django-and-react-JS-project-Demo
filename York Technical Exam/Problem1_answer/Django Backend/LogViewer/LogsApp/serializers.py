from rest_framework import serializers
from LogsApp.models import Logs

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('LogId',
                  'LOG_PRODUCER',
                  'TIMESTAMP',
                  'SEVERITY',
                  'LOG_MESSAGE')



