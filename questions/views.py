from django.shortcuts import render, redirect
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["qa_database"]
collection = db["answers"]

def question_form(request):
    if request.method == "POST":
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")

        data = {
            "question1": q1,
            "question2": q2,
            "question3": q3
        }

        collection.insert_one(data)

        return render(request, "questions/form.html", {"message": "Submitted Successfully!"})

    return render(request, "questions/form.html")

def view_answers(request):

    data = collection.find()

    return render(request, "questions/answers.html", {"data": data})