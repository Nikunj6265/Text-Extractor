from rest_framework import serializers
from text_search_app.models import User, Paragraph

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text']

class SearchSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)

class TextSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=None)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "name","dob", "password", "confirm_password"]

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Password and Confirm_Password doesn't match.")
        return attrs
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
          raise serializers.ValidationError('user with this Email already exists.')
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            dob=validated_data['dob'],
            password=validated_data['password'],
        )
        user.is_active = False
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance