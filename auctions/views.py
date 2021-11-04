from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import User, AuctionListings
from django.forms import ModelForm
import datetime


class NewListingForm(ModelForm):
    class Meta:
        model = AuctionListings
        fields = ["title", "description", "image_url", "starting_bid", "category"]


def index(request):
    """
    Returns the main page of the site.
    """
    main_banner = get_object_or_404(AuctionListings, title="YEEZY BOOST 350")
    featured1 = get_object_or_404(AuctionListings, title="Nike Jordan Max")
    # featured2 = get_object_or_404(AuctionListings, title="YEEZY BOOST 350")
    # featured3 = get_object_or_404(AuctionListings, title="YEEZY BOOST 350")
    return render(
        request,
        "auctions/index.html",
        {
            "main_banner": main_banner,
            "featured1": featured1,
            "current_year": datetime.datetime.now().year,
        },
    )


def login_view(request):
    """
    Allows a user to login.
    """
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "auctions/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """
    Allows a person to register for the site.
    """
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    """
    Allows one to create an auction listing.
    """
    if request.method == "POST":
        current_user = request.user

        form = NewListingForm(request.POST)
        author = form.save(commit=False)
        author.seller = current_user
        author.save()

        return redirect("listing_page", listing_id=author.pk)

    return render(request, "auctions/create_listings.html", {"form": NewListingForm()})


def all_listings(request):
    """
    Shows all listings currently on the site.
    """

    return render(
        request, "auctions/all_listings.html"
    )  # Loop through all listings here


def listing_page(request, listing_id):
    """
    Shows the specifics of a listing.
    """
    listing = get_object_or_404(AuctionListings, pk=listing_id)
    return render(
        request,
        "auctions/listing_page.html",
        {"listing": listing},
    )
