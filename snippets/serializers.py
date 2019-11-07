from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User


# class SnippetSerializer(serializers.Serializer):
class SnippetSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(read_only=True)
    # code = serializers.CharField(style={"base_template": "textarea.html"})
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    # linenos = serializers.BooleanField(required=False)
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)

    # def create(self, validated_data):
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.code = validated_data.get("code", instance.code)
    #     instance.language = validated_data.get("language", instance.language)
    #     instance.linenos = validated_data.get("linenos", instance.linenos)
    #     instance.style = validated_data.get("style", instance.style)
    #     instance.title = validated_data.get("title", instance.title)

    #     instance.save()
    #     return instance

    # --
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    # --
    class Meta:
        model = Snippet
        fields = [
            "id",
            "code",
            "highlight",
            "language",
            "linenos",
            "owner",
            "style",
            "title",
            "url",
        ]


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all()
#     )

#     class Meta:
#         model = User
#         fields = ["id", "username", "snippets"]

# ---
class UserSerializer(serializers.HyperlinkedIdentityField):
    snippets = serializers.HyperlinkedIdentityField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["id", "snippets", "url", "username"]

