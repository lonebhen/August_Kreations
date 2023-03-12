from django.shortcuts import render, get_object_or_404
from base.models import Product
from base.forms import PurchaseForm
from base.send_sms import send_message
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'product_list.html', context)


@csrf_exempt
def purchase_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            location = form.cleaned_data['location']
            city = form.cleaned_data['city']
            quantity = form.cleaned_data['quantity']
            # email = form.cleaned_data['email']

            # code logic here

            print(name)
            print(product.name)

            # send_message(product_name=product.name,name=name,phone_number=phone_number,location=location,city=city,quantity=quantity)

            return render(request, 'success.html')

    else:
        form = PurchaseForm()


    return render(request, 'purchase_product.html', {'product':product, 'form':form})





def success(request):
    return render(request, 'success.html')



        