from django.shortcuts import render
import joblib
def home(request):
    return render(request,"home.html")


def result(request):
    cls = joblib.load('flight_rf.pkl')

    lis = []

    lis.append(request.GET['Choose Your Source'])
    lis.append(request.GET['Choose Your Destination'])
    lis.append(request.GET['Airline'])
    lis.append(request.GET['Total Stop'])
    lis.append(request.GET['Departure Date and Time'])
    lis.append(request.GET['Arrival Date and Time'])

   

    print(lis)

    ans = cls.predict([lis])

    return render(request,"result.html",{'ans':ans,'lis':lis})