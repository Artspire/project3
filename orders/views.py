from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum

from .forms import RegistrationForm, AuthenticationForm

from .models import MenuItem, Topping, Extra, CartItem, Order

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def register(request):
    if request.method == 'POST':

        # Custom registration form imported from forms.py
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
    else:
        form = RegistrationForm()
    return render(request, "orders/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':

        # Django built-in authentication form
        form = AuthenticationForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("menu"))
        else:
            return render(request, "orders/login.html", {"form": form, "message": "Invalid credentials"})
    else:
        form = AuthenticationForm()
        return render(request, "orders/login.html", {"form": form})

def logout_view(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, "orders/login.html", {"form": form, "message": "Logged out"})

def menu(request):

    # Get all menu items from database
    context = {
        "regular_pizzas": MenuItem.objects.filter(category="RP"),
        "sicilian_pizzas": MenuItem.objects.filter(category="SP"),
        "toppings": Topping.objects.all(),
        "subs": MenuItem.objects.filter(category="SU"),
        "extras": Extra.objects.all(),
        "pastas": MenuItem.objects.filter(category="PA"),
        "salads": MenuItem.objects.filter(category="SA"),
        "platters": MenuItem.objects.filter(category="DP")
    }

    return render(request, "orders/menu.html", context)

def add(request):

    try:
        item_id = request.POST["menu"]
    except KeyError:
        # return render(request, "orders/menu.html", {"message": "No selection"})
        ## Does not work, because you need to pass the context as well to display menu items
        return redirect("menu")

    # Get item data from MenuItem table
    menu_item = MenuItem.objects.get(pk=int(item_id))

    # If user added toppings to pizza
    if 'toppings' in request.POST:

        # Get list of toppings
        toppings = request.POST.getlist("toppings")

        # Convert list to string
        top_string = ', '.join(map(str, toppings))

        # Save pizza + toppings to cart
        cart = CartItem(user=request.user, item=menu_item, price=menu_item.price, toppings=top_string)
        cart.save()

    # If user added extras to sub
    elif 'extras' in request.POST:

        # Get list of extras
        extras = request.POST.getlist("extras")

        # Convert list to string
        extra_string = ', '.join(map(str, extras))

        # Calculate price of extras
        extras_price = 0.50 * len(extras)

        # Calculate new price of sub
        sub_price = float(menu_item.price) + extras_price

        # Save sub + extras to cart
        cart = CartItem(user=request.user, item=menu_item, price=sub_price, extras=extra_string)
        cart.save()

    # If user added a salad, pasta, dinner platter or no toppings/extras
    else:

        if menu_item.category == 'PA' or menu_item.category == 'SA':

            # Convert menu_item to string object
            item_string = str(menu_item)

            # Delete last 3 characters from string
            item_slice = item_string[:-3]

            # Save pasta or salad to cart
            cart = CartItem(user=request.user, item=item_slice, price=menu_item.price)
            cart.save()

        else:
            # Save dinner platter to cart
            cart = CartItem(user=request.user, item=menu_item, price=menu_item.price)
            cart.save()

    return redirect("menu")

def cart(request):

    # If there are items in the cart
    if CartItem.objects.filter(user=request.user):

        # Get sum of items in cart
        total_price = CartItem.objects.filter(user=request.user).aggregate(Sum('price'))['price__sum']

        # Round total price to 2 decimals
        price_rounded = "{:.2f}".format(total_price)

    # If not, the total price is $0.00
    else:
        price_rounded = 0

    context = {
        # Get all items from CartItem table
        "items": CartItem.objects.filter(user=request.user),
        "total_price": price_rounded
    }

    if request.method == 'POST':

        # If users presses "Clear cart" button
        if 'clear' in request.POST:

            # Delete items from cart
            CartItem.objects.filter(user=request.user).delete()

        # If users presses "Confirm" button
        elif 'confirm' in request.POST:

            # Get total price of items
            total_price = request.POST["price"]

            # Get items in cart from CartItem table
            cart = CartItem.objects.filter(user=request.user)

            # Convert QuerySet to list
            cart_list = list(cart)

            # Convert list to string
            order_list = ', '.join(map(str, cart_list))
            print(order_list)

            # Save order to Order table
            order = Order(user=request.user, items=order_list, total_price=total_price)
            order.save()

            # Delete items from CartItem table
            CartItem.objects.filter(user=request.user).delete()

            # Redirect to order history page
            return redirect("history")

        return render(request, "orders/cart.html", context)

    else:
        return render(request, "orders/cart.html", context)

def manager(request):

    # Get all orders from database
    context = {
      "orders": Order.objects.all()
    }

    if request.method == 'POST':

        order_number = request.POST["number"]

        # Update status of order to "Completed"
        Order.objects.filter(order_number=order_number).update(status="C")

        return render(request, "orders/manager.html", context)

    else:
        return render(request, "orders/manager.html", context)

def history(request):

    # Get user orders from database
    context = {
      "user": request.user,
      "orders": Order.objects.filter(user=request.user)
    }

    return render(request, "orders/history.html", context)
