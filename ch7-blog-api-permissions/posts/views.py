from rest_framework import generics

from . import models
from . import permissions
from . import serializers


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthorOrReadOnly,)
    # queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.Post.objects.filter(author=user)
