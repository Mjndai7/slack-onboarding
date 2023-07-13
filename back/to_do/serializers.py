from rest_framework import serializers
from .models import ToDo
from users.models import ToDoUser
from misc.fields import ContentField


class ToDoSerializer(serializers.ModelSerializer):
    search_type = serializers.CharField(default='to_do', read_only=True)
    id = serializers.IntegerField(required=False)
    content = ContentField()

    class Meta:
        model = ToDo
        fields = '__all__'


# new hire serializer
class ToDoFormSerializer(serializers.ModelSerializer):
    to_do = ToDoSerializer(read_only=True)

    class Meta:
        model = ToDoUser
        fields = ('id', 'to_do', 'completed', 'form')