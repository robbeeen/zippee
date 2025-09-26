from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

from authentication.utils import create_tokens_for_user
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True
            , write_only=True
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if User.objects.filter(email__iexact=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email is already taken."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
            )
        
        
        user.set_password(validated_data['password'])
        user.save()
        return "User Created Successfully. Please Verify using OTP sent to your Email"
    
    def to_representation(self, instance):
        return {
            "message": 'User Created Successfully. Please Verify using OTP sent to your Email',
            "status": "success"
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email and password:
            try:
                user = User.objects.get(email__iexact=email)
            except ObjectDoesNotExist:
                raise serializers.ValidationError({"message": "User does not exist"})
            if not user.check_password(password):
                raise serializers.ValidationError({"message": "Invalid Password"})
            token = create_tokens_for_user(user)
            token['role'] = user.role
            return token
        else:
            raise serializers.ValidationError({"message": "Please provide email and password"})
