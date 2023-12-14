from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from leave_in_good_hands.models import Donation, Institution, Category
from django.shortcuts import render, redirect

from .forms import DonationForm
from .models import Donation


# Create your views here.
class LandingPage (View):
    def get (self, request):
        donation_count = Donation.objects.all().count()
        institution_count = Institution.objects.all().count()
        institutions = Institution.objects.all()
        context = {
            "donation_count": donation_count,
            "institution_count": institution_count,
            "institutions": institutions,
        }
        return render(request, 'index.html', context)

class DashboardView (View):
    def get (self, request):
        donation_count = Donation.objects.all().count()
        institution_count = Institution.objects.all().count()
        institutions = Institution.objects.all()
        context = {
            "donation_count": donation_count,
            "institution_count": institution_count,
            "institutions": institutions,
        }
        return render(request, 'dashboard.html', context)


class DonationView(LoginRequiredMixin, View):
    login_url = 'login'  # konieczne podanie URL dla LoginRequiredMixin?

    def get(self, request):
        categories = Category.objects.all()
        form = DonationForm()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'institutions': institutions, 'form': form, 'categories': categories})


    def post(self, request):
        form = DonationForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            categories = form.cleaned_data['categories']
            institution = form.cleaned_data['institution']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            pick_up_date = form.cleaned_data['pick_up_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            pick_up_comment = form.cleaned_data['pick_up_comment']

            donation = Donation.objects.create(quantity=quantity, categories=categories, institution=institution,
                                               address=address,
                                               phone_number=phone_number, city=city, zip_code=zip_code,
                                               pick_up_date=pick_up_date,
                                               pick_up_time=pick_up_time, pick_up_comment=pick_up_comment,
                                               user=request.user)
            return render(request,'form-confirmation.html', {'donation': donation, 'quantity': quantity,
                                                       'categories': categories, 'institution': institution,
                                                       'address': address,
                                                       'phone_number': phone_number, 'city': city, 'zip_code': zip_code,
                                                       'pick_up_date': pick_up_date,
                                                       'pick_up_time': pick_up_time, 'pick_up_comment': pick_up_comment,
                                                       'user': request.user})

        institutions = Institution.objects.all()
        return render(request, 'form.html', {'institutions': institutions, 'form': form})


class Confirmation(LoginRequiredMixin, View):
    def get(self, request):
        donations = Donation.objects.all()
        return render(request, 'form-confirmation.html', {'donations': donations} )

class UserProfile(LoginRequiredMixin, View):

    def get(self, request):
        donation_count = Donation.objects.all().count()
        institution_count = Institution.objects.all().count()
        institutions = Institution.objects.all()
        context = {
            "donation_count": donation_count,
            "institution_count": institution_count,
            "institutions": institutions,
        }
        return render(request, 'profile.html', context)
