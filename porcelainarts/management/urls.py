from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
    url(r'^/index/$', index, name="index"),

    url(r'^/inventari/$', inventari, name="inventari"),
    url(r'^/inventari/(?P<pk>\d+)$', detail, name="detail"),
    url(r'^/inventari/(?P<pk>\d+)/edit/$', edit, name="edit"),
    url(r'^/addnew$', addnew, name="addnew"),

    url(r'^/furnizimi', furnizimi, name="furnizimi"),
    url(r'^/addnewFurnziim$', addnewFurnziim, name="addnewFurnziim"),
    url(r'^/(?P<pk>\d+)/furnizim/$', detailFurnizim, name="detailFurnizim"),
    url(r'^/(?P<pk>\d+)/editFurnizim/$', editFurnizim, name="editFurnizim"),

    url(r'^/shitje', shitje, name="shitje"),
    url(r'^/addnewShitje$', addnewShitje, name="addnewShitje"),
    url(r'^/(?P<pk>\d+)/shitje/$', detailShitje, name="detailShitje"),
    url(r'^(?P<pk>\d+)/editShitje/$', editShitje, name="editShitje"),

    url(r'^/klienti', klienti, name="klienti"),
    url(r'^/addnewKlienti$', addnewKlienti, name="addnewKlienti"),
    url(r'^/(?P<pk>\d+)/klienti/$', detailKlient, name="detailKlient"),
    url(r'^/(?P<pk>\d+)/editKlient/$', editKlient, name="editKlient"),

    url(r'^/produktet', produktet_web, name="produktet"),
    url(r'^/(?P<pk>\d+)/produkti/$', detailProdukt, name="detailProdukt"),
    url(r'^/addnewProdukt$', addnewProdukt, name="addnewProdukt"),
    url(r'^/(?P<pk>\d+)/editProdukt/$', editProdukt, name="editProdukt"),

    url(r'^/kategorite', categorite_web, name="kategorite"),
    url(r'^/(?P<pk>\d+)/kategoria/$', detailCategory, name="detailCategory"),
    url(r'^/addnewCategory', addnewCategory, name="addnewCategory"),
    url(r'^/(?P<pk>\d+)/editCategory/$', editCategory, name="editCategory"),

    url(r'^/login/$', LoginView, name='login'),
    url(r'^/logout/$', LogoutView, name='logout'),
    url(r'^/export/csv_inventari/$', views.export_inventari_csv, name='export_inventari_csv'),
    url(r'^/export/csv_shitjet/$', views.export_shitjet_csv, name='export_shitjet_csv'),
    url(r'^/export/csv_furnizimet/$', views.export_furnizim_csv, name='export_furnizim_csv'),
    url(r'^/export/csv_perfurnizim/$', views.export_perFurnizim_csv, name='export_perFurnizim_csv'),
    url(r'^/export/csv_klientet/$', views.export_klientet_csv, name='export_klientet_csv'),

]
