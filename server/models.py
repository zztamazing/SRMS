import uuid
from django.db import models
from user.models import Profile


# Create your models here.


class Server(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    server_image = models.ImageField(null=True, blank=True, default='default.jpg')
    server_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # tags = models.ManyToManyField('Tag', blank=True)
    # vote_total = models.IntegerField(default=0, null=True, blank=True)
    # vote_ratio = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


"""
example
"""
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.featured_image.url
    #     except:
    #         url = ''
    #     return url
    #
    # @property
    # def reviewers(self):
    #     queryset = self.review_set.all().values_list('owner__id', flat=True)
    #     return queryset
    #
    # @property
    # def getVoteCount(self):
    #     reviews = self.review_set.all()
    #     upVotes = reviews.filter(value='up').count()
    #     totalVotes = reviews.count()
    #
    #     ratio = (upVotes / totalVotes) * 100
    #     self.vote_total = totalVotes
    #     self.vote_ratio = ratio
    #
    #     self.save()




class Review(models.Model):
    # VOTE_TYPE = (
    #     ('up', 'Up Vote'),
    #     ('down', 'Down Vote'),
    # )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = [['owner', 'server']]

    def __str__(self):
        return self.body