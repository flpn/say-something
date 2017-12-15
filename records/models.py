from django.db import models


class Record(models.Model):
    text = models.CharField(max_length=100)
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.text
