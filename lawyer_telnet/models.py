from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=70, default="", null=True, blank=True)
    phone = models.CharField(max_length=70, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    serviceName = models.CharField(max_length=100, null=True, blank=True)
    serviceDesc = models.CharField(max_length=10000, null=True, blank=True)
    serviceImage = models.FileField(upload_to='serviceImage', editable=True, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class Practices(models.Model):
    practiceName = models.CharField(max_length=100, null=True, blank=True)
    practiceDesc = models.CharField(max_length=10000, null=True, blank=True)
    practiceImage = models.FileField(upload_to='practiceImage', editable=True, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class Law(models.Model):
    lawName = models.CharField(max_length=100, null=True, blank=True)
    lawDesc = models.CharField(max_length=10000, null=True, blank=True)
    lawImage = models.FileField(upload_to='lawImage', editable=True, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class Media(models.Model):
    mediaTitle = models.CharField(max_length=1000, null=True, blank=True)
    mediaDesc = models.CharField(max_length=10000, null=True, blank=True)
    byName = models.CharField(max_length=100, null=True, blank=True)
    pub_date = models.DateField(auto_now_add=True, blank=True)
    mediaImage = models.FileField(upload_to='mediaImage', editable=True, null=True, blank=True)
    related = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.related


class MediaComment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=70, null=True, blank=True)
    phone = models.CharField(max_length=70, null=True, blank=True)
    commentDesc = models.CharField(max_length=100000, null=True, blank=True)
    commentDate = models.DateField(auto_now_add=True, null=True, blank=True)
    commentReply = models.CharField(max_length=100000, null=True, blank=True)
    commentReplyDate = models.DateField(null=True, blank=True)
    mediaId = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='mediaId', null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)


class Consulation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=70, default="", null=True, blank=True)
    phone = models.CharField(max_length=70, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.name
