'''from django.db import models
from django.conf import settings as dj_settings

class Post(models.Model):
    """
    Blog post
    """

    author = models.ForeignKey(
        dj_settings.AUTH_USER_MODEL,
        verbose_name=("author"),
        null=True,
        blank=True,
        related_name="djangocms_blog_post_author",
        on_delete=models.PROTECT,
    )

    date_created = models.DateTimeField(("created"), auto_now_add=True)
    date_modified = models.DateTimeField(("last modified"), auto_now=True)
    date_published = models.DateTimeField(("published since"), null=True, blank=True)
    date_published_end = models.DateTimeField(("published until"), null=True, blank=True)
    text = models.TextField(("text"), blank=True)

    def __str__(self):
        return "post of " + self.author.username


class Follower(models.Model):
    followed = models.ForeignKey(dj_settings.AUTH_USER_MODEL, related_name='followed_by', on_delete=models.CASCADE)
    follower = models.ForeignKey(dj_settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(followed=models.F('follower')), name='followed_and_follower_are_different'),
        ]
        unique_together = ('followed', 'follower')

    def __str__(self):
        return "followers of " + self.followed.username




'''