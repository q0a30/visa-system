from	django.db	import	models
class	Client(models.Model):
				full_name	=	models.CharField(max_length=200)
				passport_number	=	models.CharField(max_length=50,	unique=True)
				phone	=	models.CharField(max_length=30)
				photo	=	models.ImageField(upload_to='photos/')
				passport_image	=	models.ImageField(upload_to='passports/')
				status	=	models.CharField(max_length=20,	default='new')
				notes	=	models.TextField(blank=True)
				def	__str__(self):
								return	self.full_name