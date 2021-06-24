from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from category.models import Category


class PostCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    children = serializers.ListField(
        child=RecursiveField(), allow_null=True, required=False
    )

    class Meta:
        model = Category
        fields = ("name", "children")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class GetCategorySerializer(serializers.ModelSerializer):
    parents = serializers.ListField(child=CategorySerializer(), allow_null=True)
    children = serializers.ListField(child=CategorySerializer(), allow_null=True)
    siblings = serializers.ListField(child=CategorySerializer(), allow_null=True)

    class Meta:
        model = Category
        fields = ("id", "name", "parents", "children", "siblings")
