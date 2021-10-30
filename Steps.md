ddavid

skdd

ddka

dkob

tithe 20

Box with display flex
inside box, we have two cards , and on the cards both would have display flex with a flex of 1 and direction of coloum
the left box have an outline of line grey
the link 

https://leo-commerce.herokuapp.com/

https://github.com/LeoZorzoli/Commerce/blob/master/auctions/models.py

https://shopwice.com/product/converse-all-star-navy-blue/



For this Project the site should be 

1. Responsive.
2. The Django admin should use one of the templates.
3. Docker should be used. 

Four things to allow the user to do. 

1. Post auction listings, 
2. Place bids on listings, 
3. Comment on those listings, 
4. Add listings to a “watchlist.”
5. auction listings, one for bids, and one for comments, one for a watchlist

For Specification 1, make sure the User model works. Logout, Login, etc. 

***Use documentation for all functions and classes.***

Google the error. 

Check how you can register. 

Check if you remove the model what happens.

Google the User model. 

When we register, it should add the user and all the relevant details to the model. 

How would we know that it's added to the model?



Create a superuser. Check to see if you can add a user and then log in. - You can't. Brian did something

Add the models. Migrate. Add at least one entry in the shell

Add a model for bids



Post auction listings



Create a user id custom field 

For this the user should be able to provide a url field for the image -url has to not be optional, 

title for the listing,
text based description,

 and starting bid(manytoMany, foriegn key?), 

and a catergory, also text, 

a data and a time model field 



Bid would be a number or int field right? Bid should also relate back to the user field, so we know the user who bid. 

Highest bidder would just be thew current bidder There has to be a bid for each listing. You only have to update the bid for a specific listing. 

Comments would be text



Watchlist would be a bool and link to a listing



if I create a listing? I create it on the webpage with a form(like Django forms) and then I save the data the user gave me from the webpage in the database? So we have to check how to do that.



So then it's created. Then the DB would render that listing out on the frontpage as an active auction. 



So now if the user is signed in, the listing should still be displayed, but the webpage should show the add to watchlist option (done in the view and html) and then when the user clicks add to watchlist, then info should be sent to the DB that this user added to the listing. 

So the bool value should become 1. 

Now if the user goes to the watchlist page and the bool is 1, they should be able to see the listing that they added to their watchlist.

This means that watchlist should relate to the user field in a way. So that we can either get the username or user id

foreign key as string



bids should be deleted when a listing is deleted. So bids should be tired to listings. 

Create listing should be a form that allows one to enter the title, description, and what the starting bid should be.  a URL for an image for the listing and a category 

because the seller should be signed in before the form can be created, if the user is not signed it should give an error



if user not signed in, render, you'll need to be signed if before you can create a listing. Please sign in and try again. Just like Tonaton.

It's a JS modal

Else, allow the user to create the listing so that we can. 

For starting bid and any bid, price cannot be larger than any small positive int



we must first check if a user is signed in.



When we create a listing how do we save it to the DB, how do we show the DB choices in the listing? 



if that part is clicked, then go to the else clause and show the modal. Else the script should show the modal

js to close

js to trigger



For creating a listing, if it is a post request method, then get the title, the description, image url, starting bid and cateory and save them to the Db. The question is how to get the data. Make sure that the form is valid before you get the data

get the user from the person submitting 

form.[user id] == 



on modal close go back home



do it like flight. Loop through all the lisitngs. But then for the first context, the Yeezy one, add only that one. As a seperate context. 



Check to see if you can do the Yeezy one. If you can, then that is all. 

Becuase it's CSS, you might have to access each element seperatly. Look at how the flight page was done. 



Insert the flight id in the YEEzy div



it should not show a particular flight, it should show all flights



Dave 3

Random user names 3 each

if bid in bid table, then current bid = bid from bid table else it's bid from auction table

Use the listing id

Section

JS and links



The nav bar should only hold things that are relevant to the page

Use icon with drop down to show the current user, login, register

Shop would be active listings
