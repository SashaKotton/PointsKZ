import logging
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers, exceptions
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import(
    TokenRefreshSerializer,
    TokenObtainPairSerializer,
)
from authorization.models import User

logger = logging.getLogger(__name__)

class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, *args, **kwargs):
        # if not self.user.is_active:
        #     raise AuthenticationFailed({
        #         'detail': f"Пользователь {self.user.username} был деактевирован"
        #     }, code='user_deleted')
        try:
            data = super().validate(*args, **kwargs)
        except exceptions.AuthenticationFailed as e:
            logger.exception(e)
            raise AuthenticationFailed({
                'detail': f"Логин или пароль некорректные!"
            }, code='user_deleted')
        
        if not self.user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.username} был деактевирован"
            }, code='user_deleted')
        
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['role'] = self.user.ROLE_GROUP[self.user.role]

        return data
    
class TokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])

        try:
            user = User.objects.get(
                pk=refresh.payload.get('user_id')
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'detail': f"Пользователь был удален"
            }, code='user_does_not_exists')
        
        if not user.is_active:
            raise AuthenticationFailed({
                'details': f"Пользователь {user.username} был архивирован"
            }, codd='user_deleted')
        
        data['id'] = user.id
        data['username'] = user.username
        data['role'] = user.ROLE_GROUP[user.role]

        return data
    
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'first_name', 'email']

class UserNameEditSerializer(serializers.Serializer):
    first_name = serializers.CharField()