from rest_framework.routers import DefaultRouter

from webapp.viewsets import StudentsViewSet

router = DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
urlpatterns = router.urls