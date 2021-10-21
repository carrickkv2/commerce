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



bids should be deleted when a listing is deleted. So bids should be tired to lisitngs. 

