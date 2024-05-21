from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

from seventh.models import Student


def index(request):
    #student1 = Student.objects.create(surname="Булгаков", name="Михал", patronymic="Непомнович", year=1891, group="У-189")
    #student2 = Student.objects.create(surname="Будков", name="Валерий", patronymic="Валерьевич", year=2002, group="У-234")
    #student3 = Student.objects.create(surname="Холодов", name="Вадим", patronymic="Сергеевич", year=2002, group="У-226")
    #student4 = Student.objects.create(surname="Руднев", name="Юрий", patronymic="Александрович", year=2002, group="У-226")
    #student5 = Student(surname="Заграй", name="Александр", patronymic="Александрович", year=2002, group="ИСП-185")
    #student5.save()
    #student6 = Student(surname="Сычёв", name="Владимир", patronymic="Игоревич", year=2002, group="ИСП-185")
    #student6.save()
    #student7 = Student.objects.get_or_create(surname="Богатырёв", name="Павел", patronymic="Евгеньевич", year=2002, group="Т-239")

    #С ПОМОЩЬЮ all()
    students = Student.objects.all()

    return render(request, "index.html", {"students": students})


def get_student(request):
    try:
        student = Student.objects.get(surname="Будков")
        return render(request, "get.html", {"student": student})
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h2>Студент не найден</h2>")


def get_filter(request):
    students = Student.objects.filter(year=1891)
    return render(request, "index.html", {"students": students})


def get_exclude(request):
    students = Student.objects.exclude(group="ИСП-185")
    return render(request, "index.html", {"students": students})


def get_two_students(request):
    students = Student.objects.all()[:2]
    return render(request, "index.html", {"students": students})


def save(request):
    michael = Student.objects.get(id=1)
    michael.group = "Т-211"
    michael.save()
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


def update_student(request):
    Student.objects.filter(id=2).update(name="СкаредЪ")
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


def delete_student(request):
    student = Student.objects.get(id=3)
    student.delete()
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


def get_spec(request):
    students = Student.objects.filter(surname__contains="Б")
    return render(request, "index.html", {"students": students})


def sort(request):
    students = Student.objects.order_by("-surname")
    return render(request, "index.html", {"students": students})


def get_exact(request):
    students = Student.objects.filter(name__exact="Павел")
    return render(request, "index.html", {"students": students})


