import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order

def order_create(request):
    # Two-step flow within one endpoint:
    # 1) POST (valid, no confirm) -> summary screen
    # 2) POST with confirm -> save and redirect to success
    if request.method == 'POST':
        if 'confirm' in request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                order = Order.objects.create(
                    name=data['name'],
                    address=data['address'],
                    phone=data['phone'],
                    email=data['email'],
                    sticks_count=data['sticks_count'],
                    sticks_type=data['sticks_type'],
                    need_napkins=data['need_napkins'],
                    need_wasabi=data['need_wasabi'],
                    sushi_json=json.dumps(data['sushi']),
                    comment=data.get('comment', ''),
                )
                return redirect('orders:success', order_id=order.id)
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                return render(request, 'orders/order_summary.html', {'data': data})
    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {'form': form})

def order_success(request, order_id: int):
    order = get_object_or_404(Order, pk=order_id)
    sushi = json.loads(order.sushi_json or '[]')
    return render(request, 'orders/order_success.html', {'order': order, 'sushi': sushi})