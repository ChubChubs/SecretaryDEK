from django.db import models

# Create your models here.


class Doc(models.Model):
    id = models.IntegerField(verbose_name="id", primary_key=True, db_index=True)
    template = models.CharField(verbose_name="template name", max_length=255, null=False)


class Fields(models.Model):
    document = models.ForeignKey(Doc, db_index=True, verbose_name="id")
    model = models.CharField(max_length=255, null=False)
