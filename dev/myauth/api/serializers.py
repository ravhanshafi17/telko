from ..models import *
from rest_framework import serializers



class Low_level_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Low_level_User
        fields = '__all__'

class Mid_level_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mid_level_User
        fields = '__all__'

class High_level_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = High_level_User
        fields = '__all__'


# class Custom_userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['password']

# class CombinedSerializer(serializers.Serializer):
#     model1 = User_detailsSerializer()
#     model2 = Custom_userSerializer()

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'username','email',"is_midlevel","is_lowlevel"]