from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.core.mail import EmailMultiAlternatives

# Create your views here.
from building_manager.forms import BuildingForm, ApartmentForm, RenterForm, EmailUserCreationForm
from building_manager.models import Building, Apartment, Renter
from building_project import settings


def home(request):
    return render_to_response("home.html")

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            # <h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>
            html_content = '<div style="width:500px;">' \
                           '<table width="100%" border="0" align="center" cellpadding="5" style="background: #ffffff; border-right: 1px solid #cccccc; border-left: 1px solid #cccccc; border-top: 1px solid #cccccc; border-bottom: 1px solid #cccccc;">' \
                           '<tr><td valign="bottom"><table width="100%" height="75px;" border="0" style=" background-color:#285e8e; padding-left:10px;"><tr><td align="left" valign="bottom"><span style="color:#fff; padding-bottom:5px; font-size:22px; font-family:Arial, Helvetica, sans-serif; letter-spacing:2px;"><strong>PROPERTY MANAGER</strong></span></td></tr></table></td></tr><tr><td><div style="padding:5px; color:#555555; font-family: Arial, Helvetica, sans-serif;"><h2>Hi {}, thank you for signing up!</h2> I hope you enjoy using our site!</div></td></tr><tr><td><table width="100%" height="20px;" border="0" style=" background-color:#285e8e;"><tr><td align="left" valign="bottom">&nbsp;</td></tr></table></td></tr></table></div>'.format(user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("/profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("registration/login")
    return render(request, "registration/profile.html")

#####  Building section  #####
@login_required
def building(request):
    buildings = Building.objects.all()
    return render(request, "building/building.html", {'buildings': buildings})

@login_required
def view_building(request, building_id):
    building = Building.objects.get(id=building_id)
    data = {'building': building}
    return render(request, "building/view_building.html", data)

@login_required
def add_building(request):
      # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = BuildingForm(request.POST)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new Building object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/building")
    # Else if the user is looking at the form page
    else:
        form = BuildingForm()

    data = {'form': form}
    return render(request, "building/add_building.html", data)

@login_required
def edit_building(request, building_id):
    # Similar to the the detail view, we have to find the existing Building we are editing
    building = Building.objects.get(id=building_id)
    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            if form.save():
                return redirect("/building/{}".format(building_id))
    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = BuildingForm(instance=building)
    data = {"building": building, "form": form}
    return render(request, "building/edit_building.html", data)

def delete_building(request, building_id):
    building = Building.objects.get(id=building_id)
    building.delete()
    return redirect("/building")

#####  Apartment section  #####
@login_required
def apartment(request):
    apartments = Apartment.objects.all()
    return render(request, "apartment/apartment.html", {'apartments': apartments})

@login_required
def view_apartment(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    data = {'apartment': apartment}
    return render(request, "apartment/view_apartment.html", data)

@login_required
def add_apartment(request):
      # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = ApartmentForm(request.POST, request.FILES)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new Apt object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/apartment")
    # Else if the user is looking at the form page
    else:
        form = ApartmentForm()
    data = {'form': form}
    return render(request, "apartment/add_apartment.html", data)

@login_required
def edit_apartment(request, apartment_id):
    # Similar to the the detail view, we have to find the existing apt we are editing
    apartment = Apartment.objects.get(id=apartment_id)
    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form.is_valid():
            if form.save():
                return redirect("/apartment/{}".format(apartment_id))
    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ApartmentForm(instance=apartment)
    data = {"apartment": apartment, "form": form}
    return render(request, "apartment/edit_apartment.html", data)

@login_required
def delete_apartment(request, apartment_id):
    apartment = Apartment.objects.get(id=apartment_id)
    apartment.delete()
    return redirect("/apartment")

#####  Renter section  #####
@login_required
def renter(request):
    renters = Renter.objects.all()
    s3_url = "https://jng-aws.s3.amazonaws.com/"
    return render(request, "renter/renter.html", {'renters': renters, 's3_url': s3_url})

@login_required
def view_renter(request, renter_id):
    renter = Renter.objects.get(id=renter_id)
    s3_url = "https://jng-aws.s3.amazonaws.com/"
    data = {'renter': renter, 's3_url': s3_url}
    return render(request, "renter/view_renter.html", data)

@login_required
def add_renter(request):
    s3_url = "https://jng-aws.s3.amazonaws.com/"
      # If the user is submitting the form
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = RenterForm(request.POST, request.FILES)
        # Django will check the form's validity for you
        if form.is_valid():
            # Saving the form will create a new renter object
            if form.save():
                # After saving, redirect the user back to the index page
                return redirect("/renter")
    # Else if the user is looking at the form page
    else:
        form = RenterForm()
    data = {'form': form, 's3_url': s3_url}
    return render(request, "renter/add_renter.html", data)

@login_required
def edit_renter(request, renter_id):
    # Similar to the the detail view, we have to find the existing renter we are editing
    renter = Renter.objects.get(id=renter_id)
    s3_url = "https://jng-aws.s3.amazonaws.com/"
    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = RenterForm(request.POST, request.FILES, instance=renter)
        if form.is_valid():
            if form.save():
                return redirect("/renter/{}".format(renter_id))
    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = RenterForm(instance=renter)
    data = {"renter": renter, "form": form, "s3_url": s3_url}
    return render(request, "renter/edit_renter.html", data)

@login_required
def delete_renter(request, renter_id):
    renter = Renter.objects.get(id=renter_id)
    renter.delete()
    return redirect("/renter")