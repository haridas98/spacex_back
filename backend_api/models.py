from django.db import models

class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Adv(models.Model):
    text1 = models.CharField(max_length=15)
    number = models.CharField(max_length=5)
    text2 = models.CharField(max_length=15)

    def __str__(self):
        return f"Adv {self.id}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(id__lte=4),
                name='max_adv_objects'
            )
        ]