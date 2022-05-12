from rest_framework import serializers
from zerofire.models import Manager

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['mno','name','email','workarea','id','pass_field','rno']