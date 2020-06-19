from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleModelViewset, basename='article')
router.register('member', views.MemberModelViewSet, basename='member')
router.register('group', views.GroupModelViewSet, basename='group')
router.register('membership', views.MembershipModelViewSet, basename='membership')
# router.register('create_membership', views.MembershipCreateAPIView, basename='create_mem')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
    # path('article/', views.article_list, name='article'),
    # path('article/', views.ArticleAPIView.as_view(), name='article'),
    # path('article/detail/<int:id>', views.ArticleDetailAPIView.as_view(), name='article_detail'),
    # path('generic/article/<int:id>', views.GenericAPIView.as_view(), name='generic_article'),
]
