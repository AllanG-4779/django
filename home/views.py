from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):

    return render(request, "home/homepage.html")

def jobs(request):
    context = [{"title":"Computer Aided Design",
                "posts":2,"Location":"Nairobi","mode":"Full time",
                "sector": "Engineering and Technology",
                "organization":"JKUAT",
                "description":"Describe the job here"
                },
               {"title": "Java Lecturer",
                "posts": 21, "Location": "Kiambu", "mode": "Full time",
                "sector": "Technology",
                "organization":"USIU",
                "description":"Description goes here"
                },
               {"title": "Human Resource Manager",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Human Resource Management",
                "organization":"Kenyatta University",
                "description":"Describe the Job Here"
                },
               {"title": "Computer Aided Design",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Engineering and Technology",
                "organization": "JKUAT",
                "description": "Describe the job here"
                },
               {"title": "Java Lecturer",
                "posts": 21, "Location": "Kiambu", "mode": "Full time",
                "sector": "Technology",
                "organization": "USIU",
                "description": "Description goes here"
                },
               {"title": "Human Resource Manager",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Human Resource Management",
                "organization": "Kenyatta University",
                "description": "Describe the Job Here"
                },
               {"title": "Computer Aided Design",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Engineering and Technology",
                "organization": "JKUAT",
                "description": "Describe the job here"
                },
               {"title": "Java Lecturer",
                "posts": 21, "Location": "Kiambu", "mode": "Full time",
                "sector": "Technology",
                "organization": "USIU",
                "description": "Description goes here"
                },
               {"title": "Human Resource Manager",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Human Resource Management",
                "organization": "Kenyatta University",
                "description": "Describe the Job Here"
                },
               {"title": "Computer Aided Design",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Engineering and Technology",
                "organization": "JKUAT",
                "description": "Describe the job here"
                },
               {"title": "Java Lecturer",
                "posts": 21, "Location": "Kiambu", "mode": "Full time",
                "sector": "Technology",
                "organization": "USIU",
                "description": "Description goes here"
                },
               {"title": "Human Resource Manager",
                "posts": 2, "Location": "Nairobi", "mode": "Full time",
                "sector": "Human Resource Management",
                "organization": "Kenyatta University",
                "description": "Describe the Job Here"
                }
               ]
    return render(request,"home/jobs.html", {'ctx':context})
