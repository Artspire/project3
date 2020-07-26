# Pinocchio

Pinocchio is a web application for handling a pizza restaurant's online orders. The web application has been built with <a href="https://www.djangoproject.com/">Django</a> and makes use of <a href="https://django-crispy-forms.readthedocs.io/en/latest/">django-crispy-forms</a> to easily render good looking forms.

For a video walkthrough, see: https://youtu.be/Sk9php9HBgY

## Layout

The design of the website is quite minimalist with a combination of fairly bright colors and a light font weight. For the background of the website, I used the colors of the Italian flag which I found on <a href="https://www.schemecolor.com/italy-flag-colors.php">SchemeColor</a>. For the layout, I have made use of <a href="https://getbootstrap.com/">Bootstrap</a> components, including the grid system, a modal and a navbar.

## Files

My Django project folder contains one app: <b>orders</b>.

Inside <b>orders</b>, there is a <i>migrations</i> folder that lists all the database migrations, a <i>static</i> folder containing a number of images, an icon and a `styles.css` file, and a <i>templates</i> folder containing 8 .html template files that make up the website.

A few other noteworthy files are `forms.py` which defines the custom RegistrationForm, `models.py` which defines all the tables in the database, `urls.py` that lists all the URL routes and `views.py` that contains all the necessary Python code for running the website.

Lastly, outside of the app folder, there is <i>pizza</i> folder containing all the default Django project files, a `db.sqlite3` database file, a `manage.py` file and a `requirements.txt` file listing all the Python packages used and which django-crispy-forms has been added to.

## Functionality

When a user browses to the website, the user is shown a homepage with some information about the pizza restaurant. To make use of the other functionality of the website, an account needs to be created by clicking on 'register' at the top of the page and filling in all the required fields.

After registration or logging in, the user is redirected to the menu page where he or she can take a look at the restaurant's menu and add menu items to his/her shopping cart.

The user is solely responsible for selecting the right amount of toppings for his/her pizza. Moreover, the user can add any type of extra to his/her sub. The price of the sub is recalculated accordingly in the shopping cart.

To see the items the user has added to the shopping cart, the user can click on 'cart' at the top of the page. On the cart page, the user is presented with a list of the items (including toppings or extras if they were added) and the total price of all the items in the shopping cart. Furthermore, the user has the option to delete all the items from the shopping cart by clicking on 'clear cart' or to proceed to checkout by clicking on 'proceed to checkout'.

Before the order is actually placed, the user first needs to confirm the order by clicking on 'confirm' in the dialog box that is shown after clicking on 'proceed to checkout'. At this stage, the user can also still go back to the shopping cart by clicking on 'close'.

If the user confirms the order, the user is taken to the order history page where the user is shown a nice presentation of every placed order including the order number, the order status and the date and time the order was placed.

The items in the cart are deleted from the CartItem table and the order is saved to the Order table. Saving the order to the database was actually quite challenging. My solution is to save the entire list of items (including toppings or extras) as a long string to the 'items' field in the Order table and display every item on an new line on the order history/order manager page with the help of some JavaScript code that can be found in `base.html`.

### Personal touch

My personal touch is allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders. When the site administrator (superuser) logs in to the website, he/she sees a special order manager page that lists all the orders that have been placed by users on the website. Under every order, there is a large 'complete order' button to mark the order as completed and change the order status in the database. After clicking on the button, the order manager page gets refreshed and the button disappears.

At the same time, the user that placed the order will also see that the status of his/her order has changed from pending to completed on the order history page.
