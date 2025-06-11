from rest_framework import routers
from app.views import StudentViewSet

router = routers.SimpleRouter()
router.register(r'student', StudentViewSet)
urlpatterns = router.urls