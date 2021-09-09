import joblib
from django.shortcuts import render,HttpResponse
from .models import *

randomr = joblib.load(open('./models/random.pkl', "rb"))
lasso = joblib.load(open('./models/lassos.pkl', "rb"))
linear = joblib.load(open('./models/linears.pkl', "rb"))


def home(request):
    return render(request, 'home.html')

def outlier(request):
    return render(request, 'outlier.html')

def contact(request):
    return render(request, 'contact.html')

def accuracy(request):
    return render(request, 'accuracy.html')

def eda(request):
    return render(request, 'eda.html')

def nullvalue(request):
    return render(request, 'null.html')

def data(request):
    return render(request, 'datadescription.html')

def intro(request):
    return render(request, 'introduction.html')

def methods(request):
    return render(request, 'methodology.html')

def cor(request):
    return render(request, 'correlation.html')

#
# #our result page view
def result(request):
    if request.method == 'POST':
        id = request.POST['id']
        No_of_years = int(request.POST['No_of_years'])
        Present_Price = float(request.POST['Present_Price'])
        Kms_Driven = int(request.POST['Kms_Driven'])
        Owner = int(request.POST['Owner'])

        No_of_years = 2021 - No_of_years

        Fuel_Type_Petrol = request.POST['Fuel_Type_Petrol']

        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif Fuel_Type_Petrol == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        Seller_Type_Individual = request.POST['Seller_Type_Individual']
        if Seller_Type_Individual == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        Transmission_Manual = request.POST['Transmission_Manual']
        if Transmission_Manual == 'Manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0


        Car_Brand_Kia = request.POST['Car_Brand_Kia']
        Car_Brand_Mahindra = 0
        Car_Brand_MarutiSuzuki = 0
        Car_Brand_Toyota = 0
        Color_Silver = 0
        Color_White = 0

        if Car_Brand_Mahindra == 'Mahindra':
            Car_Brand_Kia = 0
            Car_Brand_Mahindra = 1
            Car_Brand_MarutiSuzuki = 0
            Car_Brand_Toyota = 0
        elif Car_Brand_Kia == 'Kia':
            Car_Brand_Mahindra = 0
            Car_Brand_Kia = 1
            Car_Brand_MarutiSuzuki = 0
            Car_Brand_Toyota = 0
        elif Car_Brand_MarutiSuzuki == "MarutiSuzuki":
            Car_Brand_Mahindra = 0
            Car_Brand_Kia = 0
            Car_Brand_MarutiSuzuki = 1
            Car_Brand_Toyota = 0
        elif Car_Brand_Toyota == "Toyota":
            Car_Brand_Toyota = 1
            Car_Brand_Mahindra = 0
            Car_Brand_Kia = 0
            Car_Brand_MarutiSuzuki = 0
        else :
            Car_Brand_Toyota = 0
            Car_Brand_Mahindra = 0
            Car_Brand_Kia = 0
            Car_Brand_MarutiSuzuki = 0

        Color_Red = request.POST['Color_Red']

        if Color_Red == 'Red':
            Color_Red = 1
            Color_Silver = 0
            Color_White = 0
        elif Color_Silver == 'Silver':
            Color_Red = 0
            Color_Silver = 1
            Color_White = 0
        elif Color_White == "White":
            Color_Red = 0
            Color_Silver = 0
            Color_White = 1
        else:
            Color_Red = 0
            Color_Silver = 0
            Color_White = 0

        prediction = randomr.predict([[Present_Price, Kms_Driven, Owner, No_of_years,Car_Brand_Kia,Car_Brand_Mahindra,
                                       Car_Brand_MarutiSuzuki,
                                 Car_Brand_Toyota,Color_Red,Color_Silver,Color_White,Fuel_Type_Diesel,
                                 Fuel_Type_Petrol,Seller_Type_Individual, Transmission_Manual]])

        prediction1 = lasso.predict([[Present_Price, Kms_Driven, Owner, No_of_years,Car_Brand_Kia,Car_Brand_Mahindra,
                                      Car_Brand_MarutiSuzuki,
                                 Car_Brand_Toyota,Color_Red,Color_Silver,Color_White,Fuel_Type_Diesel,
                                 Fuel_Type_Petrol,Seller_Type_Individual, Transmission_Manual]])

        prediction2 = linear.predict([[Present_Price, Kms_Driven, Owner, No_of_years,Car_Brand_Kia,Car_Brand_Mahindra,
                                       Car_Brand_MarutiSuzuki,
                                 Car_Brand_Toyota,Color_Red,Color_Silver,Color_White,Fuel_Type_Diesel,
                                 Fuel_Type_Petrol,Seller_Type_Individual, Transmission_Manual]])





        output = round(prediction[0], 2)
        output1 = round(prediction1[0], 2)
        output2 = round(prediction2[0], 2)


        b = CarPrice(id,Car_Brand_Kia,Color_Red,No_of_years, Present_Price, Kms_Driven, Owner, Fuel_Type_Petrol, Seller_Type_Individual,
               Transmission_Manual)
        b.save()

        context = {'output1': output1, 'output2': output2,'output': output}
    else:
        context = {}
    return render(request, 'index.html', context)
