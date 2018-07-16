from django.db import models
from decimal import Decimal
from models import *
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver

class Kodi(models.Model):
    kodi = models.CharField(max_length=50, blank=True, null=True)
    pershkrim = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-kodi',)
        verbose_name = 'Produkti'
        verbose_name_plural = 'Produktet'
    def __str__(self):
        return self.kodi

class Inventari(models.Model):
    kodiI = models.ForeignKey(Kodi, related_name='kodiI')
    gjendje = models.IntegerField(blank=True, null=True)
    cmimi_per_njesi = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    cmimi_shitjes = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    pershkrim = models.TextField(blank=True, null=True)
    permasat = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering = ('-kodiI',)
        verbose_name = 'Inventari'
        verbose_name_plural = 'Inventari'

    def __str__(self):
        return str(self.kodiI)

class Furnizimi(models.Model):
    kodiF = models.ForeignKey(Kodi, related_name='kodiF')
    data_porosise = models.DateTimeField(auto_now_add=True)
    cmimi_per_njesi = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    sasia = models.IntegerField(blank=True, null=True)
    cmimi_total = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    pershkrim = models.TextField(blank=True, null=True)
    permasat = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering = ('-data_porosise',)
        verbose_name = 'Furnizimi'
        verbose_name_plural = 'Furnizimet'
        index_together = (('kodiF', 'data_porosise'),)
    def __str__(self):
        return str(self.kodiF)


def pre_saved_cmimi_total_reciver(sender, instance, *args, **kwargs):
    cmimi_total = instance.cmimi_per_njesi*instance.sasia
    instance.cmimi_total = cmimi_total
pre_save.connect(pre_saved_cmimi_total_reciver, sender=Furnizimi)

@receiver(post_save, sender=Furnizimi)
def gjeendja_inventarit_llogaritje(sender, instance, created, **kwargs):

    if Inventari.objects.filter(kodiI= instance.kodiF):
        if created:
            i=Inventari.objects.get(kodiI= instance.kodiF).gjendje
            f=Inventari.objects.get(kodiI= instance.kodiF).cmimi_per_njesi
            Inventari.objects.filter(kodiI= instance.kodiF).update(gjendje=i+instance.sasia, cmimi_per_njesi=(f+instance.cmimi_per_njesi)/2)

        else:
            instance.sasia.save()
    else:
        if created:
            Inventari.objects.create(kodiI=instance.kodiF, gjendje=instance.sasia, cmimi_per_njesi=instance.cmimi_per_njesi, pershkrim=instance.pershkrim, permasat=instance.permasat)
        else:
            instance.sasia.save()



class Klienti(models.Model):
    emer = models.CharField(max_length=50)
    mbiemer = models.CharField(max_length=50)
    nrTel = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    class Meta:
        ordering = ('-emer',)
        verbose_name = 'Klienti'
        verbose_name_plural = 'Klientet'
    def __str__(self):
        return self.emer + " " + self.mbiemer

class Shitje(models.Model):
    kodiS = models.ForeignKey(Kodi, related_name='kodiS')
    sasia = models.IntegerField(blank=True, null=True)
    ulje = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    cmimi_per_njesi = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    cmimi_shitjes = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    pershkrim = models.TextField(blank=True, null=True)
    klienti = models.ForeignKey(Klienti, related_name='klienti')
    kapari = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    data_porosise = models.DateTimeField(auto_now_add=True)
    data_dorezimit = models.DateTimeField()
    class Meta:
        ordering = ('-data_porosise',)
        verbose_name = 'Shitje'
        verbose_name_plural = 'Shitjet'
        index_together = (('kodiS', 'klienti'),)
    def __str__(self):
        return str(self.kodiS)


def pre_saved_cmimi_total_reciver_shitje(sender, instance, *args, **kwargs):
    cmimi_total_shitje = (instance.cmimi_per_njesi*instance.sasia)-instance.ulje
    instance.cmimi_shitjes = cmimi_total_shitje
pre_save.connect(pre_saved_cmimi_total_reciver_shitje, sender=Shitje)

@receiver(post_save, sender=Shitje)
def gjeendja_inventarit_llogaritje_shitje(sender, instance, created, **kwargs):

        if created:
            i=Inventari.objects.get(kodiI= instance.kodiS).gjendje
            Inventari.objects.filter(kodiI= instance.kodiS).update(gjendje=i-instance.sasia)

        else:
            instance.sasia.save()