from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Users can follow multiple users
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def follow(self, user):
        """Follow another user."""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user."""
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        """Check if following a user."""
        return self.following.filter(id=user.id).exists()