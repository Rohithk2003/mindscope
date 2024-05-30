from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *


# Create your views here.
@csrf_exempt
def updateDB(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Patient.objects.create(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            focusTime=data["focusTime"],
            password=data["password"],
            email=data["email"],
            username=data["username"],
        )
        return JsonResponse({"status": "success"})
    if request.method == "GET":
        patient = Patient.objects.all()
        return JsonResponse(
            {
                "status": "success",
                "data": list(patient.values()),
            }
        )


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            data = Patient.objects.filter(
                password=data["password"], email=data["email"]
            ).first()
            print(data)
            return JsonResponse({"status": data is not None})
        except:
            return JsonResponse({"status": False})


@csrf_exempt
def deleteAll(request):
    if request.method == "POST":
        Patient.objects.all().delete()
        return JsonResponse({"status": "success"})
    if request.method == "GET":
        patient = Patient.objects.all()
        Patient.objects.all().delete()
        return JsonResponse(
            {
                "status": "success",
                "data": list(patient.values()),
            }
        )


@csrf_exempt
def updateTimer(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data["email"]
        print(email, "dd")
        patient = Patient.objects.filter(email=email)
        Patient.objects.create(
            name=patient.first().name,
            age=patient.first().age,
            email=patient.first().email,
            username=patient.first().username,
            password=patient.first().password,
            focusTime=data["focusTime"],
            no_of_test_attempts=patient.first().no_of_test_attempts + 1,
        )
        patient.update(
            focusTime=data["focusTime"],
            no_of_test_attempts=patient.first().no_of_test_attempts + 1,
        )
        return JsonResponse({"status": "success"})


def listall(request):
    patients = Patient.objects.all()
    usualTimeData = FocusCheck.objects.all()
    output = []
    for patient in patients:
        temp = {}
        temp["age"] = patient.age
        temp["name"] = patient.name
        temp["email"] = patient.email
        temp["focusTime"] = f"{(patient.focusTime / 60):.2f} Min"
        temp["no_of_test_attempts"] = patient.no_of_test_attempts
        for usualTimeValue in usualTimeData:
            if (
                patient.age >= usualTimeValue.age_start
                and patient.age <= usualTimeValue.age_end
            ):
                temp["range_start"] = f"{usualTimeValue.range_start / 60:.2f} Min"
                temp["range_end"] = f"{usualTimeValue.range_end / 60:.2f} Min"
        output.append(temp)
    return JsonResponse({"status": "success", "data": output})


@csrf_exempt
def getPastTests(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data["email"]
        patients = Patient.objects.filter(email=email)
        usualTimeData = FocusCheck.objects.all()
        output = []
        for patient in patients:
            temp = {}
            temp["age"] = patient.age
            temp["name"] = patient.name
            temp["email"] = patient.email
            temp["focusTime"] = f"{(patient.focusTime / 60):.2f} Min"
            temp["no_of_test_attempts"] = patient.no_of_test_attempts
            for usualTimeValue in usualTimeData:
                if (
                    patient.age >= usualTimeValue.age_start
                    and patient.age <= usualTimeValue.age_end
                ):
                    temp["range_start"] = f"{usualTimeValue.range_start / 60:.2f} Min"
                    temp["range_end"] = f"{usualTimeValue.range_end / 60:.2f} Min"
            output.append(temp)
        return JsonResponse({"status": "success", "data": output})
