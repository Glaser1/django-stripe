from django.contrib import admin
from django.urls import path
from stripe_payment.views import (create_checkout_session_view,
                                  ItemLandingPageView,
                                  cancel_page,
                                  success_page,
                                  OrderPageView,
                                  create_checkout_session_for_order
                                  )


urlpatterns = [
    path('order/<int:order_id>/', OrderPageView.as_view()),
    path('order/pay/<int:order_id>/', create_checkout_session_for_order),
    path('item/<int:item_id>/', ItemLandingPageView.as_view()),
    path('buy/<int:item_id>/', create_checkout_session_view),
    path('cancel/', cancel_page, name='cancel'),
    path('success/', success_page, name='success'),
    path('admin/', admin.site.urls),
]
