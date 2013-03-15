from django.shortcuts import render_to_response
from django.http import HttpResponse
from testsite.books.models import Book

    
def search(request):
    print 'searching...'
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('bookapp/search_results.html',
                {'books': books, 'query': q})
    print 'rendering search form again: %s' % error
    return render_to_response('bookapp/search_form.html', {'error': error})

