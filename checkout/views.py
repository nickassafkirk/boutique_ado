from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total*100)
    if stripe_secret_key:
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
    else:
        print("SECRET KEY NOT BEING FOUND", settings.SECRET_KEY)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JFKHwHUYBtMekWnR6HNd1REv9M0rJPZxF0jPgZTK9zx6n94WotJ21upinfgsdm0VohzKg2Ww1hCKxsXGbwR9izm00aj8uBJTF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
