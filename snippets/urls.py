# from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # path("snippets/", views.snippet_list),
    # path("snippets/<int:pk>/", views.snippet_detail),
    # --
    # url(r"^snippets/<int:pk>", views.snippet_detail),
    # url(r"^snippets", views.snippet_list),
    # --
    url(
        r"^snippets/<int:pk>/highlight",
        views.SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
    url(r"^snippets/<int:pk>", views.SnippetDetail.as_view(), name="snippet-detail"),
    url(r"^snippets", views.SnippetList.as_view(), name="snippet-list"),
    url(r"^users/<int:pk>", views.UserDetail.as_view(), name="user-detail"),
    url(r"users", views.UserList.as_view(), name="user-list"),
    url(r"api-auth", include("rest_framework.urls")),
    url(r"", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
