from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from item.models import Category,Item
from .models import Wishlist

@login_required
def index(request):
    wishlist,created = Wishlist.objects.get_or_create(user=request.user)
    items = wishlist.items.all()

    return render(request, 'wishlist/index.html', {'items': items})

@login_required
def remove_from_wishlist(request, item_id):
    wishlist = Wishlist.objects.get(user=request.user)
    item = get_object_or_404(Item, id=item_id)
    wishlist.items.remove(item)
    return redirect('wishlist:index')