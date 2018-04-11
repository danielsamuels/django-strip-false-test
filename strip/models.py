from django.db import models


class Test(models.Model):

    field = models.CharField(
        max_length=10,
        strip=False,
    )
