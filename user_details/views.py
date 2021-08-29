from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import (
    CreateView,
    UpdateView
)

from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin
)

from .forms import UserSurveyForm

from .models import UserDetails

# @login_required
# def userSurveyView(request):
#     user = request.user
#     context = {
#         'user': user
#     }
#     template_name = 'user-survey/user_survey.html'

#     if request.method == 'POST':
#         form = UserSurveyForm(request.POST)

#         if form.is_valid():
#             form.data['user'] = user
#             form.save()
#         return redirect('survey-app:user_details:user_survey')

#     else:
#         form = UserSurveyForm()

#     context['form'] = form 
#     return render(request, template_name, context)


class UserSurveyView(LoginRequiredMixin, CreateView):
    model = UserDetails
    form_class = UserSurveyForm
    template_name = template_name = 'user-survey/user_survey.html'
    success_url = '/surveys/user-survey/'

    def form_valid(self, form):
        user = self.request.user

        form.instance.user = user
        
        return super().form_valid(form)