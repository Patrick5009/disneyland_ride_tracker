from django.db import models
from django.contrib.auth.models import User

# Ride model, representing a ride in the tracker.


class Ride(models.Model):

    # The name of the ride, with a maximum length of 50 characters.
    ride_name = models.CharField(max_length=50)

    # A boolean field indicating whether the ride has been visited.
    state = models.BooleanField(default=False)

    # A foreign key linking the ride to a specific user.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Returns the ride name when the object is printed or displayed.
    def __str__(self):
        return self.ride_name
