from .serializers import SignUpSerializer, CodeSerializer, UserInfoSerializer, UserSerializer
from reviews.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdministrator, IsAdministratorOrReadOnly, IsAuthorOrStaffOrReadOnly, IsModerator
from rest_framework.decorators import action
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from api_yamdb.settings import DEFAULT_FROM_EMAIL
from rest_framework.generics import get_object_or_404


class SignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            email = serializer.data.get('email')
            user = User.objects.create(
                username=username,
                email=email
            )
            token = default_token_generator.make_token(user)
            subject = 'Спасибо за регистрацию в нашем чудо сервисе'
            send_mail(
                subject=subject,
                message=f'Ваш токен авторизации: {token}',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetToken(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(
                User,
                username=serializer.data.get('username')
            )
            confirmation_code = serializer.data.get('confirmation_code')
            if default_token_generator.check_token(user, confirmation_code):
                token = AccessToken.for_user(user)
                return Response(
                    {'Ваш токен доступа к API': str(token)},
                    status=status.HTTP_200_OK
                )
            return Response(
                'Неверный код доступа',
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdministrator,)
    filterset_fields = ['username']
    lookup_field = 'username'

    @action(detail=False,
            methods=['GET', 'PATCH'],
            permission_classes=[IsAuthenticated]
            )
    def me(self, request):
        user = get_object_or_404(User, username=request.user.username)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = UserInfoSerializer(
                user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_200_OK
                            )
