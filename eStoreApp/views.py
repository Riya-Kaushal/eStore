from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required

from . models import Product, ProductImage 

# Create your views here.


# def login_view(request):
#     login(request)
#     print("Logged in successfully!")
#     return redirect('/homepage')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username= request.POST['username'].strip(),
            password= request.POST['password'],
            )
        if user is None:
            messages.error(request, u'Invalid credentblog.ials')
        else:
            if user.is_active:
                login(request, user)
                return redirect('/homepage')
            else:
                messages.error(request, u'User is not active.')

                return render_to_response('eStoreApp/login.html', locals(),      
                    context_instance=RequestContext(request))

    return render(request, 'eStoreApp/login.html', {})




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
				return redirect('/homepage')

		print('password not matching')
	return render(request, 'eStoreApp/register.html', {})




@login_required(login_url='/login/')
def homepage(request):
	
	laptops = Product.objects.filter(product_type="Laptop")
	mobiles = Product.objects.filter(product_type="Mobile")
	products = Product.objects.all()
	# completed_bookings_count = BookingDetail.objects.filter(status="Completed", guest=user).count()
	# draft_bookings_count = BookingDetail.objects.filter(status="Draft", guest=user).count()
	# # for hotel in recommended_hotels:
	# print(completed_bookings_count)

	return render(request, 'eStoreApp/homepage.html', 
							{'user': request.user,
							'laptops': laptops,
							'mobiles': mobiles,
							'products': products})




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

		return render(request, 'eStoreApp/homepage.html', 
							{'alert_action': 'created',
							'openAlertModal': 1})

	else:
		return redirect('/homepage')





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
		return render(request, 'eStoreApp/homepage.html', 
							{'alert_action': 'updated'})

	else:
		return redirect('/homepage')




@login_required(login_url='/login/')
def delete_product(request):
	if request.method == 'POST':
		product_id = request.POST.get('product-id')
		name = request.POST['name']
		description = request.POST['description']
		product_type = request.POST['product_type']
		processor = request.POST['processor']
		RAM = request.POST['RAM']

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
		return render(request, 'eStoreApp/homepage.html', 
							{'alert_action': 'updated'})

	else:
		return redirect('/homepage')




@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    print("Logged out successfully!")
    return redirect('/homepage')