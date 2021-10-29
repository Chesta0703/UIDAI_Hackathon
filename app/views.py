from django.shortcuts import redirect, render

# Create your views here.
def index(request):
	return render(request, "index.html")

def login(request):
	if request.user.is_authenticated:
		return redirect('app:index')
	else:
		return render(request, 'login/login.html')

def otp(request):
	if request.user.is_authenticated:
		return redirect('app:index')
	else:
		if request.method == "POST":
			aadharNum = request.POST.get("aadharNum")
			return render(request, 'login/otp.html')
		else:
			return redirect('app:login')
