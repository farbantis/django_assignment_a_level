from django.shortcuts import render


def view_1(request):
    return render(request, 'view_1.html/')


def view_2(request):
    return render(request, 'view_2.html')


def view_3(request):
    return render(request, 'view_3.html')


def view_5(request):
    return render(request, 'view_5.html')


def view_6(request, article_number):
    context = {
        'article_number': article_number
    }
    return render(request, 'view_6.html', context)


def view_7(request, article_number):
    context = {
        'article_number': article_number
    }
    return render(request, 'view_7.html', context)


def view_8(request, article_number, slug_text):
    context = {
        'article_number': article_number,
        'slug_text': slug_text
    }
    return render(request, 'view_8.html', context)


def view_9(request, user_number):
    context = {
        'article_number': user_number,
    }
    return render(request, 'view_9.html', context)


def view_10(request, data):
    context = {
        'data': data
    }
    return render(request, 'view_10.html', context)


def view_11(request, phone_num):
    context = {
        'phone_num': phone_num
    }
    return render(request, 'view_11.html', context)
