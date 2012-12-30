from profile import Customer, UserRegistrationForm

def user_created(sender, user, request, **kwargs):
    form = UserRegistrationForm(request.POST)
    data = Customer(user=user)
    data.first_name = form.data["first_name"]
    data.last_name = form.data["last_name"]
    data.address = form.data["address"]	
    data.city = form.data["city"]
    data.zip = form.data["zip"]
    data.date_of_birth = form.data["date_of_birth"]
    data.save()
    
from registration.signals import user_registered

user_registered.connect(user_created)