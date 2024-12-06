from django.db import models

class UserIP(models.Model):
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address