from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Username, Product, Cart
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'product/index.html'
#     context_object_name = 'list'
#     show_case()
#     def get_queryset(self):
#         return Username.objects.all()

def index(request):
    product = Product.objects.all()
    return render(request,'product/index.html',{'list':Username.objects.all(),'product_object':product})


def register(request):
    return render(request, 'product/register.html')

def submit(request):
    username = request.POST.get('username_post_test','')
    password = request.POST.get('password_post','')
    confirm_password = request.POST.get('confirm_password',False)
    alert_message = ''
    create_correct = True
    for i in Username.objects.values():
        if username == i['username']:
            alert_message = 'This email has been registered'
            create_correct = False
            return render(request,'product/register.html',{'create_correct':create_correct,'alert_message':alert_message})
    if password != confirm_password:
        alert_message = 'The two password do not match, please enter again'
        create_correct = False
        return render(request, 'product/register.html', {'create_correct': create_correct, 'alert_message': alert_message})
    if create_correct:

        user = Username.objects.create_user(username=username,password=password)
        auth.login(request, user)
        return HttpResponseRedirect(reverse('product:index'))



def show_case(request):
    product = Product.objects.all()
    return render(request, 'product/include/product_lib.html', {'product':product})

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username)

    user = auth.authenticate(username=username,password=password)
    print(user)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('product:index'))
    else:

        return render(request, 'product/login.html',{'login_fail':True})

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('product:index'))

def cart(request):
    return render(request,'product/cart.html',{'items':Cart.objects.filter(user=request.user)})

def show(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request, 'product/showcase.html', {'product':product,'range':range(38,46)})

def buy(request):
    count = request.POST.get('quantity',0)
    size = request.POST.get('size',40)
    user = request.user
    product = request.POST.get('product','')

    print('***********************\n\n\n')
    print(product)
    print('\n\n\n')
    print('#######################\n\n\n')
    cart = Cart(count=count,size=size,user=user,product_id=product)
    cart.save()
    return HttpResponseRedirect(reverse('product:cart'))