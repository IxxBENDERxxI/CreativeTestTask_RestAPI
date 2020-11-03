from django.db import models
from django.conf import settings


#Make model for Cities
class Cities(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


#Make model for users, we extended base User model.
#User - OnetoOne, City - ForeignKey
class UserData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='profileCity', blank=True, null=True)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user.username


#Make advert model. User and city as ForeignKey.
class UserAdverts(models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='advert_user')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='advert_user_city', blank=True, null=True)
    body = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Adverts'
        verbose_name_plural = 'Adverts'

    def __str__(self):
        return self.name

