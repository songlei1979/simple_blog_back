from rest_framework.routers import DefaultRouter

from blog.viewsets import CategoryViewSet, PostViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls