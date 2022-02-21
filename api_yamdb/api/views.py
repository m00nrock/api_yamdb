from rest_framework import viewsets, status
from rest_framework.response import Response
from reviews.models import Comment, Review, Title
from .serializers import CommentSerializer, ReviewSerializer
from .permissions import IsAuthorOrAdministrationOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrAdministrationOrReadOnly,)

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

    def retrieve(self, request, *args, **kwargs):
        if Title.objects.filter(pk=kwargs['id']).count() != 0:
            title = Title.objects.get(pk=kwargs['id'])
            if Review.objects.filter(title=title).count() != 0:
                queryset = Review.objects.filter(title=title)
                for review in queryset:
                    if str(review.id) == kwargs['pk']:
                        serialiser = ReviewSerializer(review)
                        return Response(serialiser.data)
        error = {"detail": "Произведение или отзыв не найден"}
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        if Title.objects.filter(pk=kwargs['id']).count() == 0:
            error = {"detail": "Произведение не найдено"}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return super(CommentViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if Title.objects.filter(pk=kwargs['id']).count() == 0:
            error = {"detail": "Произведение или отзыв не найден"}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        return super(CommentViewSet, self).destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
