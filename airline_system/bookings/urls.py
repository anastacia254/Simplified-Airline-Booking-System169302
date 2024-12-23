from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)

urlpatterns = router.urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookings.urls')),  # Include the bookings app API routes
]
