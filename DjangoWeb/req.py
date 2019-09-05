from django.http import HttpResponse


def req(request):
    msg = "hello req" + " \r\n"
    msg += request.path + " \r\n"
    msg += request.method + " \r\n"
    # msg += request.GET + " \r\n"
    # msg += request.POST + " \r\n"
    # msg += request.REQUEST + " \r\n"
    print(request.COOKIES)
    # msg += request.COOKIES + " \r\n"
    # msg += request.FILES + " \r\n"
    # msg += request.META + " \r\n"
    # msg += request.user + " \r\n"
    # msg += request.session + " \r\n"
    # msg += request.raw_post_data + " \r\n"


    return HttpResponse(msg)
