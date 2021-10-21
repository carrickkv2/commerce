from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.utils import timezone

CATEGORIES = (
    ('TY', 'TOY'),
    ('DR', 'DRESS'),
    ('SH', 'SHIRT'),
    ('SHO', 'SHOE'),
    ('BO', 'BOOKS'),
)


class User(AbstractUser):
    """
    Allows one to get more data about a user than Django allows.
    """
    pass

    def __str__(self):
        return f"{self.id}: Username:{self.username} Email:{self.email}"


class AuctionListings(models.Model):
    """
    Model for all the listings listed on the site.
    """
    title = models.CharField(max_length=40)
    description = models.TextField()
    image_url = models.URLField()
    starting_bid = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(choices=CATEGORIES, max_length=5)
    date = models.DateField(default=date.today)
    datetime = models.DateTimeField(default=timezone.now)
    date_last_updated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_last_updated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title:{self.title}, Date Added:{self.date_added}, Category:{self.category}"

    class Meta:
        """
        Specifies the plural name of the model for the Django Admin Panel.
        """
        verbose_name_plural = "Auction Listings"


class Bids(models.Model):
    """
    Model to allow one to place bids on listings.
    """
    bid_price = models.PositiveSmallIntegerField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Bids"


class Comments(models.Model):
    """
    Model to allow one comment on listings.
    """
    comments = models.CharField(max_length=500)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"


class WatchList(models.Model):
    """
    Model to add listings to watchlist.
    """
    on_watch_list = models.BooleanField()
    lister = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_listed_listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
