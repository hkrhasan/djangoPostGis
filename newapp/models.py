from django.contrib.gis.db import models

class Zipcode(models.Model):
    poly = models.PolygonField(geography=True)


class TestModel(models.Model):
    code = models.CharField(max_length=5)
