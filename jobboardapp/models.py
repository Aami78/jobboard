from djongo import models

class JobListing(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'listings'