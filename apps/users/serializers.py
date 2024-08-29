from rest_framework import serializers

from apps.users import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email', 'phone','age')


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        model = models.User
        fields = ('username', 'email', 'phone', 'password', 'confirm_password', 'age', 'birthday')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': "Пароли отличаются"})
        elif len(attrs['password']) < 8:
            raise serializers.ValidationError({'password_len': "Слишком короткий пароль (не менее 8 символов)"})

        return attrs

    def create(self, validated_data):
        user = models.User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            phone = validated_data['phone'],
            birthday = validated_data['birthday'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user