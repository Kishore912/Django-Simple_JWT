from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user   

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()   

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Invalid Credentials")
    
class PasswordResetSerailizer(serializers.Serializer):
    email = serializers.EmailField()

class OTPSerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=6)
    
