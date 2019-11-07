# from django.urls import path
from django.conf.urls import include, url

from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

# from snippets.views import SnippetViewSet, UserViewSet, api_root


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

# --
# snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})

# snippet_detail = SnippetViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )

# snippet_highlight = SnippetViewSet.as_view(
#     {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
# )

# user_list = UserViewSet.as_view({"get": "list"})

# user_detail = UserViewSet.as_view({"get": "retrieve"})

# urlpatterns = format_suffix_patterns(
#     [
#         url(
#             r"^snippets/<int:pk>/highlight", snippet_highlight, name="snippet-highlight"
#         ),
#         url(r"^snippets/<int:pk>", snippet_detail, name="snippet-detail"),
#         url(r"^snippets", snippet_list, name="snippet-list"),
#         url(r"^users/<int:pk>/", user_detail, name="user-detail"),
#         url(r"^users", user_list, name="user-list"),
#         url(r"", api_root),
#     ]
# )

# --
# router = DefaultRouter()
# router.register(r"snippets", views.SnippetViewSet)
# router.register(r"users", views.UserViewSet)

# urlpatterns = [path("", include(router.urls))]

