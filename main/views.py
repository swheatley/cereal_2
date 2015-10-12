from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from main.models import Manufacturer, Cereal
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect  


def detail_view(request, pk):
    maker = Manufacturer.objects.get(pk=pk)

    context = {}

    context['maker'] = maker

    

    

    return render_to_response('detail_view.html', context, context_instance=RequestContext(request))


def list_view(request):
    makers = Manufacturer.objects.all()

    cereals = Cereal.objects.all()

    context = {}

    context['makers'] = makers

    context['cereals'] = cereals

    return render_to_response('list_view.html', context, context_instance=RequestContext(request))


def create_view(request):
    context = {} 
    form = MakerForm()
    context['form'] = form

    if request.method == 'POST':
            form = MakerForm(request.POST, request.FILES)

            if form.is_valid():
                print form.is_valid()

                form.save()
                return HttpResponseRedirect('/list_view/')
            else:
                context['errors'] = form.errors

    return render_to_response('create_view1.html', context, context_instance=RequestContext(request))
    #  #context = {}

    # context['request'] = request.method

    # context['Manufacturer'] = Manufacturer.objects.all()

    # if request.method == 'POST':
    #     form = ManufacturerForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print form.is_valid()

    #         form.save()
    #         return HttpResponseRedirect('/list_view/')
    #     else:
    #         context['errors'] = form.errors
    # return render_to_response('create_view.html', context, context_instance=RequestContext(request))


def create_view2(request):
     context = {}

     form = MakerForm2()
     context['form'] = form

     #if request.method == 'POST':
    #     form = SpeedModelForm2(request.POST, request.FILES)

    #     if form.is_valid():

    #         print form.cleaned_data

    #         title = form.cleaned_data['title']
    #         info = form.cleaned_data['info']
    #         image = form.cleaned_data['image']

    #         new_object = SpeedModel()

    #         new_object.title = title
    #         new_object.info = info
    #         new_object.image = image

    #         new_object.save()

    #         return HttpResponseRedirect('/list_view/')
    #     else:
    #         context['errors'] = form.errors

    # return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


    # #context = {}

    # context['request'] = request.method

    # context['Manufacturer'] = Manufacturer.objects.all()

    # if request.method == "POST":
    #     cereal_name = request.GET.get('Cereal Name', None)
    #     manufacturer = request.GET.get('Manufacturer', None)
    #     protein = request.GET.get('Protein', None)
    #     fat = request.GET.get('Fat', None)
    #     sodium = request.POST.get('Sodium', None)
    #     dietary_fiber = request.POST.get('Dietary Fiber', None)
    #     carbs = request.POST.get('Carbs', None)
    #     sugars = request.POST.get('Sugars', None)
    #     postassium = request.POST.get('Potassium', None)
    #     vitamins_and_minerals = request.POST.get('Vitamins and Minerals', None)

    #     # #if != None:
    #     #     state = State.objects.get(pk=state_id)
    #     # else:
    #     #     state = State.objects.get(name="Texas")

    #     the_create_view, created = Manufacturer.objects.get_or_create(name=cereal_name)

    #     the_create_view.protein = protein
    #     the_create_view.fat = fat 
    #     the_create_view.sodium = sodium 
    #     the_create_view.dietary_fiber = dietary_fiber
    #     the_create_view.carbs = carbs
    #     the_create_view.sugars = sugars
    #     the_create_view.postassium = postassium
    #     the_create_view.vitamins_and_minerals = vitamins_and_minerals

    #     the_create_view.save()

    #     context['created'] = "Operation Successful"

    # elif request.method == 'GET':
    #     pass

    # return render_to_response('create_view.html', context, context_instance=RequestContext(request))




def update_view(request, pk):

    # #context = {}

    # speed_object = SpeedModel.objects.get(pk=pk)

    # context['speed_object'] = speed_object

    # form = SpeedModelUpdateForm()

    # context['form'] = form

    # if request.method == 'POST':
    #     form = SpeedModelUpdateForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         speed_object.title = form.cleaned_data['title']
    #         speed_object.info = form.cleaned_data['info']

    #         if form.cleaned_data['image'] != None:
    #             speed_object.image = form.cleaned_data['image']

    #         speed_object.save()

    #         return HttpResponseRedirect('/update_view/%s/' % pk)

    #     else:
    #         context['errors'] = form.errors

    # return render_to_response('update_view.html', context, context_instance=RequestContext(request))
    # maker = Manufacturer.objects.get(pk=pk)

    # context = {}

    context['maker'] = maker 

    return render_to_response('update_view.html', context, context_instance=RequestContext(request))


def delete_view(request, pk):
    pass
    # #SpeedModel.objects.get(pk=pk).delete()

    # return HttpResponseRedirect('/list_view/')
    # maker = Manufacturer.objects.get(pk=pk)

    # context = {}

    # context['maker'] = maker 

    # return render_to_response('delete_view.html', context, context_instance=RequestContext(request))


def signup(request):

    context = {}

    form = UserSignUp()
    context['form'] = form

    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            print form.cleaned_data

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                new_user = User.objects.create_user(name, email, password)
                context['valid'] = "Thank You For Signing Up!"

                auth_user = authenticate(username=name, password=password)
                login(request, auth_user)

                return HttpResponseRedirect('/list_view/')

            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    if request.method == 'GET':
        context['valid'] = "Please Sign Up!"

    return render_to_response('signup.html', context, context_instance=RequestContext(request))




def login_view(request):

    # #context = {}

    # context['form'] = UserLogin()

    # username = request.POST.get('username', None)
    # password = request.POST.get('password', None)

    # auth_user = authenticate(username=username, password=password)

    # if auth_user is not None:
    #     if auth_user.is_active:
    #         login(request, auth_user)
    #         context['valid'] = "Login Successful"

    #         return HttpResponseRedirect('/home/')
    #     else:
    #         context['valid'] = "Invalid User"
    # else:
    #     context['valid'] = "Please enter a User Name"


    # return render_to_response('login_view.html', context, context_instance=RequestContext(request))

    # maker = Manufacturer.objects.get(pk=pk)

    context = {}

    context['maker'] = maker 

    return render_to_response('login_view.html', context, context_instance=RequestContext(request))


def logout_view(request):
    maker = Manufacturer.objects.get(pk=pk)

    context = {}

    context['maker'] = maker 

    return render_to_response('logout_view.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/login_view/')