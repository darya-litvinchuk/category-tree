from django.db import models

DEFAULT_PARENT = "NULL"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    right = models.IntegerField(blank=True, null=True)
    left = models.IntegerField(blank=True, null=True)
    parent_name = models.CharField(max_length=100, default=DEFAULT_PARENT)

    class Meta:
        ordering = ("left",)
        db_table = "application_category"

    def __repr__(self):
        return f"Category ({self.pk}) `{self.name}` ({self.left}, {self.right})"
