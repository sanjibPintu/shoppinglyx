from django.shortcuts import render,HttpResponse,reverse,redirect
from django.views import View
from math import ceil
from app import forms
from django.contrib import messages
from .models import Product,Customer,Cart,OrerPlaced
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# product view
class ProductView(View):
  def get(self,request):

    topware=Product.objects.filter(catagory='TW')
    buttomware=Product.objects.filter(catagory='BW')
    mobile=Product.objects.filter(catagory='M')
    laptop=Product.objects.filter(catagory='L')
    # print(list(topware)[0].product_image)
    return render(request,'app/home.html',{'topware':topware,'buttomware':buttomware,'mobile':mobile,'laptop':laptop})


class ProductDetails(View):
  def get(self,request,pk):
    product=Product.objects.get(id=pk)
    e=False
    off=((product.seeling_price-product.discount_price)/product.seeling_price)*100
    if request.user.is_authenticated:
      e= Cart.objects.filter(Q(product=product) & Q(user=request.user)).exists()
      print("productdetails")
    

     
    off_c =ceil(off)
    return render(request,'app/productdetail.html',{'product':product,'off_c':off_c,'e':e})

@login_required
def add_to_cart(request):
  user=request.user
  product=Product.objects.get(id=request.GET.get('productid'))
  
  try:
    Cart(user=user,product=product).save()
    return redirect('/cart')
  except:
    return HttpResponse('Not loged in')  
@login_required
def show_cart(request):
  if request.user.is_authenticated:
    user=request.user
    cart=Cart.objects.filter(user=user)
    amaount=0.0
    original_price=0.0
    

    for i in cart: 
      amaount+=i.quantity*i.product.discount_price
      original_price+=i.quantity*i.product.seeling_price
    try:
      discount=ceil(((original_price-amaount)/original_price)*100)
    except ZeroDivisionError:
      discount=0  
    
    return render(request, 'app/addtocart.html',{'cart':cart,'amaount':amaount,'original_price':original_price,'discount':discount})
  else:
    return render(request,'app/emptycart.html')

@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')


@login_required
def address(request):
  add=Customer.objects.filter(user=request.user)
  return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request):
  op=OrerPlaced.objects.filter(user=request.user)
  return render(request, 'app/orders.html',{'op':op})

# for mobile
def mobile(request ,data=None):
  if data==None:
    mobile=Product.objects.filter(catagory='M')
  else :
    mobile=Product.objects.filter(catagory='M').filter(brand= data)
   
  return render(request, 'app/mobile.html',{'mobile':mobile})

def login(request):
 return render(request, 'app/login.html')


class CustomerRegistration(View):

  def get(self,request):
    form=forms.CustomerRegistrationForm()
   
    return render(request,'app/customerregistration.html',{'form':form})
  def post(self,request):
    
    form=forms.CustomerRegistrationForm(request.POST) 
    if form.is_valid():
      messages.success(request,'Congratulation!! You Register Successfully')
      form.save()
      return redirect('login')
    
    
    return render(request,'app/customerregistration.html',{'form':form}) 

@login_required
def checkout(request):

  c=Customer.objects.filter(user=request.user)
  cart=Cart.objects.filter(user=request.user)
  return render(request, 'app/checkout.html',{'c':c,'cart':cart})
  
@method_decorator(login_required,name='dispatch')
class ProFileView(View):
  def get(self,request):
    customerForm=forms.CustomerProfileForm()
    return render(request ,'app/profile.html',{'customerForm':customerForm,'active':'btn-primary'})

  def post(self,request):
    customerForm=forms.CustomerProfileForm(request.POST)
    if customerForm.is_valid():
      usr=request.user
      name=customerForm['name'].value()
      locality=customerForm['locality'].value()
      city=customerForm['city'].value()
      state=customerForm['state'].value()
      zipcode=customerForm['zipcode'].value()    
      customer_data_save=Customer(user=usr,name=name,locality=locality,city=city,zipcode=zipcode,state=state)
      customer_data_save.save()
      messages.success(request,'Congratulation! Profile Has been Updated Successfully')
    
    return render(request,'app/profile.html',{'customerForm':customerForm,'active':'btn-primary'})  


# plus cart
def plus_cart(request):
  if request.method=='GET':
    prod_id=request.GET['prod_id']
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    cart_product=[c  for c in Cart.objects.all() if c.user ==request.user]
    total_amount=0.0
    youhavetopay=0.0
    for p in cart_product:
      temptotal_amoun=(p.quantity*p.product.seeling_price)
      tempyouhaveopay=(p.quantity*p.product.discount_price)
      total_amount+=temptotal_amoun
      youhavetopay+=tempyouhaveopay
    discount=ceil(((total_amount-youhavetopay)/total_amount)*100)

    data={
      'quantity':c.quantity,
      'originalprice':total_amount,
      'youhavetpay':youhavetopay,
      'discount':discount
    }
    return JsonResponse(data)


# minus cart
def minus_cart(request):
  if request.method=='GET':
    prod_id=request.GET['prod_id']
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    cart_product=[c  for c in Cart.objects.all() if c.user ==request.user]
    total_amount=0.0
    youhavetopay=0.0
    for p in cart_product:
      temptotal_amoun=(p.quantity*p.product.seeling_price)
      tempyouhaveopay=(p.quantity*p.product.discount_price)
      total_amount+=temptotal_amoun
      youhavetopay+=tempyouhaveopay
    discount=ceil(((total_amount-youhavetopay)/total_amount)*100)

    data={
      'quantity':c.quantity,
      'originalprice':total_amount,
      'youhavetpay':youhavetopay,
      'discount':discount
    }
    return JsonResponse(data)

# remove cart
def remove_cart(request):
  if request.method=='GET':
    prod_id=request.GET['prod_id']
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    cart_product=[c  for c in Cart.objects.all() if c.user ==request.user]
    total_amount=0.0
    youhavetopay=0.0
    for p in cart_product:
      temptotal_amoun=(p.quantity*p.product.seeling_price)
      tempyouhaveopay=(p.quantity*p.product.discount_price)
      total_amount+=temptotal_amoun
      youhavetopay+=tempyouhaveopay
    try:
      discount=ceil(((total_amount-youhavetopay)/total_amount)*100)
    except ZeroDivisionError:
      discount=0
    data={
      'originalprice':total_amount,
      'youhavetpay':youhavetopay,
      'discount':discount
    }
    return JsonResponse(data)

@login_required
def checking_cart(request):
  cartNumber=Cart.objects.filter(user=request.user)
  totalcart=0
  for i in cartNumber:
    totalcart+=i.quantity
  data={
    'totalcart':totalcart
  }  
  return JsonResponse(data)    

def payment(request):
  user=request.user
  try:
    cutomerid=request.GET["customerid"]
  except :
    return redirect("checkout")
      
  c=Customer.objects.get(id=cutomerid)
  cart=Cart.objects.filter(user=user)
  print(cart)
  for cr in cart:
    OrerPlaced(user=user,customer=c,product=cr.product,quantity=cr.quantity,
    price=cr.price).save()
    cr.delete()
    

  return redirect("orders")