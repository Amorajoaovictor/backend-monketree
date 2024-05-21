from rest_framework import serializers

from poll.models import User, Block, Click, Tree

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = '__all__'


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['id', 'link', 'user']
