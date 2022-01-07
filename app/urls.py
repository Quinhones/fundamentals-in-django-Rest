from app.views import TodoViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoViewSet)
urlpatterns = router.urls