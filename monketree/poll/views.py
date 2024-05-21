
from rest_framework.viewsets import ModelViewSet

from poll.models import User, Block, Click, Tree
from poll.serializer import UserSerializer, BlockSerializer, ClickSerializer, TreeSerializer
# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlockViewSet(ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class ClickViewSet(ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer


class TreeViewSet(ModelViewSet):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer





