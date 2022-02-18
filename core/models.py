from django.db import models

class TimeStampeModel(models.Model):
    created = models.DateTimeField(
           'criado em',
         auto_now_add=True,
         auto_now=False,

    )
    modified = models.DateTimeFil(
          'Modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
          abstract = True
