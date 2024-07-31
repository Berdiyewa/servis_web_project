from django.db import models

class TelecomData(models.Model):   #python manage.py sqlmigrate telecom 0001   - shtoby posmotret sozdalsya ili net
    hyzmat = models.CharField('Hyzmaty saýlaň', max_length=20, choices=[("wifi", "WiFi"), ("ip", "IP")])
    sahs = models.CharField('Şahsy saýlaň', max_length=20)
    ady = models.CharField('Ady, familiýasy', max_length=50)
    salgy = models.CharField('Öý salgyňyz', max_length=250)
    mobil_belgi = models.IntegerField('Telefon belgiňiz')
    telefon_belgi = models.IntegerField('Öý telefon belgiňiz')
    mesele = models.TextField('Meseläňiz', max_length=900)
    sene = models.DateTimeField('Wagty saýlaň')
    date_save = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hyzmat

    class Meta:
        verbose_name = 'Ýüz tutma'
        verbose_name_plural = 'Ýüz tutmalar'
