from django.shortcuts import render, redirect


# Create your views here.
def view_bag(request):
    """
    A view that renders the shopping bag page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  
    # checks if 'bag' object exists in session cookies and creates an empty object if it doesn't

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    # checks if item_id is in the bag already. If it is, it increases quantity
    # if not it's added to the bag dictionary

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
 