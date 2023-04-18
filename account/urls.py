from django.urls import path
from account.views import *
from django.contrib.auth.views import LogoutView


# Con el name le doy un nombre a mi ruta-url, que después voy a incluir en la base
urlpatterns = [
    path('login/', login_account, name="accountloging"),
    path('registrar/', register_account, name="accountRegistrar"),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name="accountlogout")
]