from django.http import HttpResponse


def full_name(request, name, age, interests):
    return HttpResponse(f"""
<h2>name: {name} {age} {interests}</h2>

""")


def full_about(request, city, perfomance, study_preference):
    return HttpResponse(f"""
<h2>name: {city} {perfomance} {study_preference}</h2>         
""")


def full_contracts(request, github, number_phone, tg):
    return HttpResponse(f"""
<h2>name: {github} {number_phone} {tg}</h2>    
""")
