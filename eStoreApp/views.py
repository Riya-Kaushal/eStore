from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . models import Product, ProductImage 

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username= request.POST['username'],
            password= request.POST['password'],
            )
        if user is None:
            messages.error(request, u'Invalid credentblog.ials')
        else:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                return redirect('/homepage/mobile')
            else:
                messages.error(request, u'User is not active.')

                return render_to_response('eStoreApp/registerOrLogin.html', locals(),      
                    context_instance=RequestContext(request))

    return render(request, 'eStoreApp/registerOrLogin.html', {})




def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				# show a popup user username already exists
				print('username taken')
				# return(request, 'register.html')

			else:
				user = User.objects.create_user(username=username, 
												password=password1, 
												email=email, 
												first_name=first_name, 
												last_name=last_name)
				user.save();
				print('User Created')
				return redirect('/homepage/mobile')

		print('password not matching')
	return render(request, 'eStoreApp/registerOrLogin.html', {})



@login_required(login_url='/login/')
def homepage_mobile(request):
	mobiles = Product.objects.filter(product_type="Mobile")
	return render(request, 'eStoreApp/homepage.html', 
							{'user': request.user,
							'products': mobiles})


@login_required(login_url='/login/')
def homepage_mobile(request):
	mobiles = Product.objects.filter(product_type="Mobile")
	return render(request, 'eStoreApp/homepage.html', 
							{'user': request.user,
							'products': mobiles})


@login_required(login_url='/login/')
def homepage_laptop(request):
	laptops = Product.objects.filter(product_type="Laptop")
	return render(request, 'eStoreApp/homepage.html', 
							{'user': request.user,
							'products': laptops})




@login_required(login_url='/login/')
def add_product(request):

	if request.method == 'POST':
		name = request.POST['name']
		description = request.POST['description']
		product_type = request.POST['product_type']
		processor = request.POST['processor']
		RAM = request.POST['ram']

		# creating object
		productObject = Product.objects.create(name=name, 
												description=description, 
												product_type=product_type, 
												processor=processor, 
												RAM=RAM)


		if product_type == 'Mobile':
			productObject.screen_size = request.POST['screen_size']
			productObject.color = request.POST['color']
			productObject.hd_capacity = '-'

		elif product_type == 'Laptop':
			productObject.screen_size = '-'
			productObject.color = '-'
			productObject.hd_capacity = request.POST['hd_capacity']

		productObject.save()
		print('Created productObject')

		return render(request, 'eStoreApp/homepage.html', {})

	else:
		return redirect('/homepage/mobile')





@login_required(login_url='/login/')
def update_product(request):
	if request.method == 'POST':
		product_id = request.POST.get('product-id')
		name = request.POST['name']
		description = request.POST['description']
		product_type = request.POST['product_type']
		processor = request.POST['processor']
		RAM = request.POST['ram']

		productObject = Product.objects.get(id=product_id)

		# creating object
		productObject.name=name
		productObject.description = description
		productObject.product_type = product_type
		productObject.processor = processor
		productObject.RAM = RAM

		if product_type == 'Mobile':
			productObject.screen_size = request.POST['screen_size']
			productObject.color = request.POST['color']
			productObject.hd_capacity = '-'

		elif product_type == 'Laptop':
			productObject.screen_size = '-'
			productObject.color = '-'
			productObject.hd_capacity = request.POST['hd_capacity']

		productObject.save()
		print('Updated productObject')		
		return render(request, 'eStoreApp/homepage.html', {})

	else:
		return redirect('/homepage/mobile')




@login_required(login_url='/login/')
def delete_product(request):
	if request.method == 'POST':
		product_id = request.POST.get('product-id')

		productObject = Product.objects.get(id=product_id).delete()
		print('Deleted productObject')		
		return render(request, 'eStoreApp/homepage.html', {})
	else:
		return redirect('/homepage/mobile')




@login_required(login_url='/login/')
def logout_view(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    logout(request)
    print("Logged out successfully!")
    return redirect('/homepage/mobile')
    