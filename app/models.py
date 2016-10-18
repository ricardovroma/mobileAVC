#-*- encoding=utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class App(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    package = models.CharField(max_length=255, blank=False, null=False)

    def __unicode__(self):
        return self.name

class UpdateTypes():
    TYPES_UPDATE_CHOICES = (
        (1, 'simples'),
        (2, 'CRITICA')
    )

class Version(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE, blank=False, null=False)
    version_code = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(null=False, blank=False, verbose_name='Tipo',
                               choices=UpdateTypes.TYPES_UPDATE_CHOICES)
    message = models.TextField(default="")

    class Meta():
        verbose_name_plural = 'versões'
        ordering = ('-version_code',)

    def __unicode__(self):
        _type = "Simples" if self.type == 1 else "CRITICA"
        return u'version %s (%s) - %s' % (self.version_code, _type, self.app.name)