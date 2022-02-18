from attr import field
from django.forms import ValidationError
from rest_framework import serializers
from reviews.models import User
from rest_framework.validators import UniqueValidator


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)


class CodeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200, required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'confirmation_code'
        ]


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'role',
            'email',
            'first_name',
            'last_name',
            'bio'
        ]

    def validate_username(self, value):
        if value == 'me':
            raise ValidationError(
                f'Регистрация с именем пользователя {value} запрещена!'
            )
        return value


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'role',
            'email',
            'first_name',
            'last_name',
            'bio'
        ]
        read_only_fields = ('role',)


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )

    def validate_username(self, value):
        if value == 'me':
            raise ValidationError(
                f'Регистрация с именем пользователя {value} запрещена!'
            )
        return value
