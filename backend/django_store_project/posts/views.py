from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status


from store.models import Game
from .models import Post, PostReply
from .serializers import PostSerializer, PostReplySerializer
from .permissions import PostUserWritePermission

from rest_framework.response import Response


# class PostView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)

#     def get(self, request):
#         queryset = self.get_queryset()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         return self.create(request)


class PostViewSet(viewsets.ModelViewSet):
    permissions = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_object(self, queryset=None, **kwargs):
        return generics.get_object_or_404(Post, id=self.kwargs.get('pk'))


# class PostView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         posts = Post.objects.filter(author=request.user)
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         data = request.data
#         author = request.user
#         game = Game.objects.get(id=data.get('game_id'))
#         content = data.get('content')
#         post = Post(author=author, game=game, content=content)
#         post.save()
#         return Response({'success': 'Post is published'}, status=status.HTTP_200_OK)

#     def put(self, request):
#         post = Post.objects.filter(author=request.user, id=request.data.get('post_id')).first()
#         content = request.data.get('content')
#         post.content = content
#         post.edited = True
#         post.save()
#         return Response({'success': 'Post is updated'}, status=status.HTTP_200_OK)
