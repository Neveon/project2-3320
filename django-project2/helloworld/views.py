from django.http import HttpResponse
from django.shortcuts import render
from .InputForm import InputForm


def index(request):
    print('\nSee the date, time, request type and HTTP response: ')

    if request.method == 'GET':
        context = {}
        context['form'] = InputForm()
        return render(request, "home.html", context)

    elif request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = InputForm(request.POST)

        # check whether it's valid using the Form instance is_valid() method:
        if form.is_valid():
            # print("\n{}\n\n".format(form['firstName'].value()))
            strArr = []
            strArr.append("First Name: {}".format(form['firstName'].value()))
            strArr.append("Last Name: {}".format(form['lastName'].value()))
            strArr.append("Password You Inputted: {}".format(
                form['password'].value()))

            return HttpResponse("<br/>".join(strArr))
