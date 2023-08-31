from django.shortcuts import render
from MoviesApp.models import Contact
from MoviesApp.models import Movie

# Create your views here.


def movies(request):
    trend = Movie.objects.filter(trendingORHighImdbratedORLatestORNone__icontains = "trend").order_by('-id')[0:5]
    Latest = Movie.objects.filter(trendingORHighImdbratedORLatestORNone__icontains = "Latest").order_by('-id')[0:5]
    highimdb = Movie.objects.filter(trendingORHighImdbratedORLatestORNone__icontains = "imdb").order_by('-id')[0:5]
    newadded = Movie.objects.all().order_by('-id')[0:5]
    soon = Movie.objects.filter(CompletedYESorNO__icontains = "no")
    # print(mydata)
    context = {
            'trend': trend,
            'newadded': newadded,
            'highimdb': highimdb,
            'latest': Latest,
            'soon': soon,
        }
    return render(request, "movies.html",context)


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        review = request.POST.get("review")
        contact = Contact(name=name, email=email, review=review)
        contact.save()
    return render(request, "home.html")


def search(request):
    if request.method == "GET":
        search = request.GET.get("search")
        print(search)
        mydata = Movie.objects.filter(name__icontains=search) | Movie.objects.filter(genre1__icontains=search) | Movie.objects.filter(genre2__icontains=search) | Movie.objects.filter(country__icontains=search)| Movie.objects.filter(trendingORHighImdbratedORLatestORNone__icontains=search)
        mydata = mydata.order_by('-id')
        context = {
            
            'movieresult': mydata,
            'search': search,
        }
        

    return render(request, "search.html",context)
def about(request):        

    return render(request, "about.html")

def ohmygod(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/ohmygod/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def oppenheimer(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/oppenheimer/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def rrr(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/rrr/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def Interstellar(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/Interstellar/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def it(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/it/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def incrediblehulk(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/incrediblehulk/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def thorthedarkworld(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/thorthedarkworld/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def captainamericathewintersoldie(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/captainamericathewintersoldie/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def thorloveandthunder(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/thorloveandthunder/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def thorragnarok(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/thorragnarok/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def captainamericathefirstavenger(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/captainamericathefirstavenger/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def ironman3(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/ironman3/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def avengers2012(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/avengers2012/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def thor(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/thor/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def ironman(request):
    mydata = Movie.objects.filter(movielinkonwebsite = "/ironman/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def it2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/it2/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
def bhoolbhulaiyaa(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/bhoolbhulaiyaa/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
def bhoolbhulaiyaa2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/bhoolbhulaiyaa2/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def ninele(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/ninele/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def jollyllb(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/jollyllb/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def jollyllb2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/jollyllb2/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def omg2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/omg2/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def gadar2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/gadar2/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def idiots3(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/idiots3/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def avatar(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/avatar/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def avatar2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/avatar2/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def pushpa2(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/pushpa2/")[0]
    print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def kashmirfiles(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/kashmirfiles/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def pushpa(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/pushpa/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def raazi(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/raazi/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)
def keralastory(request):
    mydata = Movie.objects.filter(movielinkonwebsite= "/keralastory/")[0]
    # print(mydata)
    context = {
            'moviedetails': mydata,
        }
    return render(request, "watchmovie.html",context)


# def moviename(request):
#     mydata = Movie.objects.filter(movielinkonwebsite = "moviename")[0]
#     # print(mydata)
#     context = {
#             'moviedetails': mydata,
#         }
#     return render(request, "watchmovie.html",context)