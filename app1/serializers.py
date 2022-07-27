
from rest_framework import serializers
from rest_framework import employees

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employees
    fields = '__all__'