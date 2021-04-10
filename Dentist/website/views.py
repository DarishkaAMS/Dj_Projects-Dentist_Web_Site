from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return render(request, 'index.html', {})


def contact_page_view(request):
    # if request.method == "POST":
    #     pass
    # else:
    return render(request, 'contacts.html', {})

