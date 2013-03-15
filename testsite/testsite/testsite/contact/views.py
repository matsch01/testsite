from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from testsite.contact.forms import ContactForm
from django.core.context_processors import csrf
from sys import stdout

def contact(request):
    print 'in contact...'
    stdout.flush()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!', 'email':'me@low.com'})
    return render_to_response('contactapp/contact_form.html', {'form': form})


