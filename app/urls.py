from django.urls import path
from app import views
from django.contrib.auth import views as auth_view

from .forms import LoginForm,CustomerPasswordChangeForm,MyPasswordReset,MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(),name="home"),

    path('product-detail/<int:pk>', views.ProductDetails.as_view(), name='product-detail'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    
    path('cart/',views.show_cart,name="cart"),
    path('pluscart/',views.plus_cart,name="pluscart"),
    path('minuscart/',views.minus_cart,name="minuscart"),
    path('removecart/',views.remove_cart,name="removecart"),

    path('buy/', views.buy_now, name='buy-now'),
    path('checkcat/',views.checking_cart,name="ceckcart"),
    path('profile/', views.ProFileView.as_view(), name='profile'),
    
    path('address/', views.address, name='address'),
    
    path('orders/', views.orders, name='orders'),

    
    path('mobile/', views.mobile, name='mobile'),
    
    path('mobile/<str:data>', views.mobile, name='mobiledata'),

    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=CustomerPasswordChangeForm,success_url='/profile/'),name="changepassword"),

    # pass word reset
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/passwod_reset.html',form_class=MyPasswordReset),name='password_reset'),

    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='app/password_restt_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    

    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password-reset-complete'),
    # end of password reset

    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/',views.payment,name="payment"),
]
