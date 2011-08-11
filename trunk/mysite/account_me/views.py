from django.http import HttpResponse
from django.shortcuts import render_to_response

def add_account(request):
    return render_to_response('add_account.html')

def add(request):
    if 'acctName' in request.POST:
        message = 'Account Name: %s' % request.POST['acctName']
    else:
        message = 'No account name entered!'
    return HttpResponse(message)