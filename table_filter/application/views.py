from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .filters import UserFilter

# Create your views here.
def index(request):
	return render(request, 'application/index.html')

def search(request):
    if dict(request.GET):
    	if 'page' not in request.GET:
    	    request.session['request_save'] = request.GET
    else:
    	request.session['request_save'] = None

    user_list = User.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    print(page)
    if page == 1:
    	user_filter = UserFilter(request.GET, queryset=user_list)
    else:
    	if request.session['request_save']:
    	    user_filter = UserFilter(request.session['request_save'], queryset=user_list)
    	else:
    		user_filter = UserFilter(request.GET, queryset=user_list)
    paginator = Paginator(user_filter.qs, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'application/index.html', {'filter': user_filter,
    	'users': users})