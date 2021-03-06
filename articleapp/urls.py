from django.urls import path

from articleapp.views import ArticleCreateAPIView, ArticleCreateTemplateView, ArticleRUDAPIView, \
    ArticleRetrieveTemplateView, ArticleUpdateTemplateView, ArticleDestroyTemplateView, MagicGridTemplateView, \
    ArticleListAPIView, ArticleListTemplateView, ArticleListCreateAPIView

app_name = 'articleapp'

urlpatterns = [
    path('create_template/', ArticleCreateTemplateView.as_view(), name='create_template'),
    path('', ArticleListCreateAPIView.as_view(), name='list'),
    path('list/', ArticleListTemplateView.as_view(),name='list_template'),
    path('retrieve_template/<int:pk>', ArticleRetrieveTemplateView.as_view(), name='retrieve_template'),
    path('update_template/<int:pk>', ArticleUpdateTemplateView.as_view(), name='update_template'),
    path('destroy_template/<int:pk>', ArticleDestroyTemplateView.as_view(), name='destroy_template'),
    path('magic_grid/',MagicGridTemplateView.as_view(),name='create'),
    path('<int:pk>', ArticleRUDAPIView.as_view(), name='RUD'),
    path('',ArticleListCreateAPIView.as_view(),name="LC")
]

