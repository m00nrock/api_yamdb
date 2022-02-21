from rest_framework import viewsets, status
from rest_framework.response import Response
from reviews.models import Comment, Review, Title
from .serializers import CommentSerializer, ReviewSerializer
from .permissions import IsAuthorOrAdministrationOrReadOnly
#from rest_framework.permissions import AllowAny


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrAdministrationOrReadOnly,)
    #permission_classes = (AllowAny,)

    def list(self, request, *arg, **kwargs):
        if Title.objects.filter(pk=kwargs['id']).count() == 0:
            error = {"detail": "Произведение не найдено."}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        title = Title.objects.get(pk=kwargs['id'])
        queryset = Review.objects.filter(title=title)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        title = Title.objects.get(pk=self.kwargs['id'])
        serializer.save(
            author=self.request.user,
            title=title
        )

    def create(self, request, *args, **kwargs):
        if Title.objects.filter(pk=kwargs['id']).count() == 0:
            error = {"detail": "Произведение не найдено."}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return super(ReviewViewSet, self).create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
