# Project 3

<b>Web Programming with Python and JavaScript</b>

For project3, I have made, per the requirements, a web application for handling a pizza restaurant's online orders. The web application is built with <a href="https://www.djangoproject.com/">Django</a> and makes use of <a href="https://django-crispy-forms.readthedocs.io/en/latest/">django-crispy-forms</a> to easily render good looking forms.

## Layout

The design of the website is quite minimalist with a combination of fairly bright colors and a light font weight. For the background of the website, I used the colors of the Italian flag which I found on <a href="https://www.schemecolor.com/italy-flag-colors.php">SchemeColor</a>. For the layout, I have made use of <a href="https://getbootstrap.com/">Bootstrap</a> components, including the grid system, a modal and a navbar. The size of the containers change depending on the width of the screen, making the website responsive and look good on all screen sizes.

## Files

My Django project folder contains two apps: <b>orders</b> and <b>pizza</b>.

Inside 'orders', there is a <i>static</i> folder that lists all the database migrations, a <i>static</i> folder containing a number of images, an icon and a `styles.css` file, and a <i>templates</i> folder containing 8 .html template files that make up the website.

`forms.py`

django-crispy-forms has been added to `requirements.txt`

 The SocketIO JavaScript code can all be found at the bottom of the `layout.html` file. Furthermore, the project folder contains a `requirements.txt` file listing all the Python packages used, a `helpers.py` file that defines the @login-required function and, lastly, an `application.py` file that contains all the necessary Flask code for running the website.

## Functionality

When a user browses to the website, the user is shown a homepage with some information about the pizza restaurant. To make use of the other functionality of the website, an account needs to be created by clicking on 'register' at the top of the page and filling in all the required fields.

After registration or logging in, the user is redirected to the menu page where he or she can take a look at the restaurant's menu and add menu items to his/her shopping cart.

The user is solely responsible for selecting the right amount of toppings for his/her pizza. Moreover, the user can add any type of extra to his/her sub. The price of a sub is recalculated accordingly in the shopping cart.

If the user confirms the order, the user is taken to the order history page where the user

a nice presentation including the order number, the order status and the date and time the order was placed.

Items from cart are deleted.

Saving the order to the database was actually quite challenging. My solution is to as a long string
with the help of some JavaScript.

### Personal touch

My personal touch is allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders. When the site administrator (superuser) logs in to the website, the
