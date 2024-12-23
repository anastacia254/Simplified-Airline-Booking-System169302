from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'  # Includes all fields in the Flight model

class PassengerSerializer(serializers.ModelSerializer):
    # Include flight details in the passenger serializer
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'  # Includes all fields in the Passenger model
