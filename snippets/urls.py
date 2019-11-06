# from django.urls import path
from django.conf.urls import url
from snippets import views

urlpatterns = [
    # path("snippets/", views.snippet_list),
    # path("snippets/<int:pk>/", views.snippet_detail),
    url(r"^snippets/<int:pk>/", views.snippet_detail),
    url(r"^snippets/", views.snippet_list),
]
