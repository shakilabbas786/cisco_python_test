from django.shortcuts import render
from django.http import HttpResponse
from routers import models
import json, random, sys, string

def home(request):
    result = []
    routers = models.Routers.objects.all()#.values_list("sapid","loopback","hostname","macaddress")
    for r in routers:
        result.append([str(r.sapid),str(r.loopback),str(r.hostname),str(r.macaddress)])
    return render(request, "home.html",{'data':json.dumps(result)})


def delete_router(request):
    sapid = request.POST.get("sapid",None)
    try:
        routers = models.Routers.objects.filter(sapid = sapid)
        if len(routers) > 0:
            routers.delete()
        else:
            return HttpResponse("NOT FOUND",status=404)
        return HttpResponse("Deleted")
    except Exception as e:
        print e
        return HttpRespoinse("SERVER ERROR", status = 500)

def create_routers(request):
    """create random routers"""
    total = request.POST.get("total",10)
    try:
        for i in range(0,int(total)):
            sip = int(random.random()*10**8)
            loopback = "%s.%s.%s.%s"%(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
            hostname = randomString()
            macaddress = "%s:%s:%s:%s:%s:%s"%(random.randrange(11,99),random.randrange(11,99),random.randrange(11,99),random.randrange(11,99),random.randrange(11,99),random.randrange(11,99))
            models.Routers.objects.create(sapid = sip, loopback = loopback,
                                hostname = hostname, macaddress = macaddress)
        return HttpResponse("Created")
    except Exception as e:
        print e
        print "line number of error {}".format(sys.exc_info()[-1].tb_lineno)
        return HttpResponse("ServerError",status = 500)


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
