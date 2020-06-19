from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']

    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=50)
    #
    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='group.id')
    name = serializers.ReadOnlyField(source='group.name')
    member_name = serializers.ReadOnlyField(source='member.name')

    class Meta:
        model = Membership
        fields = ['id', 'name', 'join_date', 'member_name']


class MembershipSerializer_nomember(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='group.id')
    name = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Membership
        fields = ['id', 'name', 'join_date',]


class MemberSerializer(serializers.ModelSerializer):
    groups = MembershipSerializer_nomember(source='membership_set', many=True, read_only=True)

    class Meta:
        model = Member
        fields = ['id', 'name', 'groups']
