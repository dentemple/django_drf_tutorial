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
    url(r"^snippets/<int:pk>", views.SnippetDetail.as_view()),
    url(r"^snippets", views.SnippetList.as_view()),
    url(r"^users/<int:pk>", views.UserDetail.as_view()),
    url(r"users", views.UserList.as_view()),
    url(r"api-auth", include("rest_framework.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
