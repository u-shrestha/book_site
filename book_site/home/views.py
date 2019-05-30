from django.shortcuts import render
from django.http import HttpResponse
from home.models import Book_detail


def f_home(request):
    try:
        book1 = Book_detail.objects.filter(bgenre__contains='nf')

        book2 = Book_detail.objects.filter(bgenre__contains='cl' and 'fi' and 'hi')

        book4 = Book_detail.objects.filter(bgenre__contains='ro')

        book5 = Book_detail.objects.filter(bgenre__contains='my')

        book6 = Book_detail.objects.filter(bgenre__contains='fa')

        book7 = Book_detail.objects.filter(bgenre__contains='sf')

        book8 = Book_detail.objects.filter(bgenre__contains='co' and 'gn')

        context = {'booklist1': book1, 'booklist2': book2, 'booklist4': book4, 'booklist5': book5, 'booklist6': book6,
                   'booklist7': book7, 'booklist8': book8}

        # context['loop1'] = range(0,5)
        # context['loop2'] = range(5, 10)
        # context['loop3'] = range(10, 15)
        # context['loop4'] = range(15, 20)
        return render(request, 'home/home.html', context)
    except Book_detail.DoesNotExist:
        return HttpResponse(request, "doesnot exist")


def f_detail(request,btitle):
    try:
        bbook = Book_detail.objects.get(btitle=str(btitle))
        context = {'book': bbook}
        return render(request, 'home/details.html', context)
    except Book_detail.DoesNotExist:
        return HttpResponse(request,  " doesnot exist")

