import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.views.generic.base import TemplateView
from items.models import Order, Item


stripe.api_key = settings.STRIPE_API_KEY
DOMAIN = settings.DOMAIN


def cancel_page(request):
    return render(request, template_name='cancel.html')


def success_page(request):
    return render(request, template_name='success.html')


class ItemLandingPageView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = kwargs.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        context.update({
            'item': item,
        })
        return context


def create_checkout_session_for_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_list = list()
    for item in order.items.all():
        item_attributes = {
                'price_data': {
                    'currency': item.currency,
                    'unit_amount': item.price,
                    'product_data': {
                        'name': item.name
                    }
                },
                'quantity': 1
        }
        order_list.append(item_attributes)
    checkout_session = stripe.checkout.Session.create(
        line_items=order_list,
        mode='payment',
        success_url=DOMAIN + '/success/',
        cancel_url=DOMAIN + '/cancel/',
    )
    return redirect(checkout_session.url, code=303)


class OrderPageView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_id = kwargs.get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        order_items = order.items.all()
        context.update({
            'order': order,
            'order_items': order_items
        })
        return context


def create_checkout_session_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'currency': item.currency,
                    'unit_amount': item.price,
                    'product_data': {
                        'name': item.name
                    }
                },
                'quantity': 1
            },
        ],
        mode='payment',
        success_url=DOMAIN + '/success/',
        cancel_url=DOMAIN + '/cancel/',
    )
    return redirect(checkout_session.url, code=303)
