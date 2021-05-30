from rest_framework import serializers
from rest_framework import Login_Details

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login_Details
        fields=('emailAddress,password')
        fields= '__all__'

