from django.urls import path
from .views import anasayfa, hakkimizda, uzmanliklar, ishukuku, ailehukuku, \
    ticarethukuku, gayrimenkulhukuku, sozlesmelerhukuku, cezahukuku, \
    icrahukuku, saglikhukuku, sigortahukuku, makaleler, makaledetay, \
    iletisim

from django.views.generic import TemplateView

urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('hakkimizda/', hakkimizda, name="hakkimizda"),
    path('hukuki-uzmanliklar/', uzmanliklar, name="uzmanliklar"),
    path('is-hukuku/', ishukuku, name="ishukuku"),
    path('aile-hukuku/', ailehukuku, name="ailehukuku"),
    path('ticaret-hukuku/', ticarethukuku, name="ticarethukuku"),
    path('gayrimenkul-hukuku/', gayrimenkulhukuku, name="gayrimenkulhukuku"),
    path('sozlesmeler-hukuku/', sozlesmelerhukuku, name="sozlesmelerhukuku"),
    path('ceza-hukuku/', cezahukuku, name="cezahukuku"),
    path('icra-hukuku/', icrahukuku, name="icrahukuku"),
    path('saglik-hukuku/', saglikhukuku, name="saglikhukuku"),
    path('sigorta-hukuku/', sigortahukuku, name="sigortahukuku"),
    path('hukuki-yayinlar/', makaleler, name="makaleler"),
    path('bize-ulasin/', iletisim, name="iletisim"),
    path('sitemap.xml/', TemplateView.as_view(template_name='websitesi/sitemap.xml', content_type='text/plain'), name="sitemap" ),
    path('robots.txt/', TemplateView.as_view(template_name='websitesi/robots.txt', content_type='text/plain')),

    path('<slug:makaleslug>/', makaledetay, name="makaledetay"),  ## Bu regexden dolayı url'in karışmaması için en sona gelecek.
]
