from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    
class Reaction(models.Model):
    category = models.ForeignKey(Category, related_name='reactions', on_delete=models.CASCADE)
    conversion = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    reactants = models.TextField(blank=False, null = False)
    products = models.TextField(blank=False, null = False)
    catalysts = models.CharField(max_length=70)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null= True, blank = True)
    extra = models.TextField(blank=True, null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category}/{self.slug}/'
