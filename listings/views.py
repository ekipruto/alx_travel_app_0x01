from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer,BookingSerializer

class ListingViewSet(ModelViewSet):
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer
    
class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer