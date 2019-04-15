from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from .models import Makaleler, Contact


# Create your views here.
def anasayfa(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/index.html', {'ucmakale' : ucmakale})

def hakkimizda(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/about.html', {'ucmakale' : ucmakale})

def uzmanliklar(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/practices.html', {'ucmakale' : ucmakale})

def ishukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/ishukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def ailehukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/ailehukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def ticarethukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/ticarethukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def gayrimenkulhukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/gayrimenkulhukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def sozlesmelerhukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/sozlesmelerhukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def cezahukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/cezahukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def icrahukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/icrahukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def saglikhukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/saglikhukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def sigortahukuku(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    besmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:5]
    return render(request, 'websitesi/sigortahukuku.html', {'ucmakale' : ucmakale, 'besmakale' : besmakale})

def makaleler(request):
    if request.GET.get('hukuki-alan'):

        alan = request.GET.get('hukuki-alan')

        makale_list = Makaleler.objects.filter(makale_kategori=alan)

        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)
        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/makaleler.html', {'articles' : articles, 'ucmakale' : ucmakale})

    elif request.GET.get('makale-ara'):

        arama = request.GET.get('makale-ara')

        makale_list = Makaleler.objects.filter(makale_baslik__icontains=arama)

        paginator = Paginator(makale_list, 4)
        page = request.GET.get('page')
        articles = paginator.get_page(page)
        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/makaleler.html', {'articles': articles, 'ucmakale': ucmakale})

    else:
        makale_list = Makaleler.objects.all()
        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)

        ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

        return render(request, 'websitesi/makaleler.html', {'articles': articles, 'ucmakale' : ucmakale})

def makaledetay(request, makaleslug):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    oncekimakale = Makaleler.objects.all().order_by('?').first()
    sonrakimakale = Makaleler.objects.all().order_by('?').first()

    makale = Makaleler.objects.get(makale_slug=makaleslug)

    return render(request, 'websitesi/makaledetay.html', {'makale' : makale,'ucmakale' : ucmakale, 'oncekimakale' : oncekimakale, 'sonrakimakale' : sonrakimakale})

def iletisim(request):

    if request.method == 'POST':

        adsoyad = request.POST.get('isim')
        email = request.POST.get('email')

        telefon = request.POST.get('telefon')
        mesaj = request.POST.get('mesaj')

        iletisim = Contact(iletisim_adsoyad=adsoyad, iletisim_telefon=telefon, iletisim_mail=email,
                             iletisim_mesaj=mesaj)
        iletisim.save()
        return redirect('anasayfa')

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'websitesi/iletisim.html', {'ucmakale' : ucmakale})