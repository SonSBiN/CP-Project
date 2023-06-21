from django.db import models


class Auction_Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    item_name = models.CharField(max_length=30)
    min_price = models.IntegerField()
    unit_price = models.IntegerField()

    head_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/auction/{self.pk}/'
