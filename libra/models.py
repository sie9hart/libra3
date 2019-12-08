from django.db import models

from django.db import models

class Books(models.Model):
    bookname=models.CharField(max_length=25)
    isbn=models.IntegerField(null=True,blank=True)
    available = models.BooleanField(default=True)
    def __str__(self):
        return '{} {}'.format(self.bookname, self.isbn)
class Studant(models.Model):
      studantname=models.CharField(max_length=25)
      c_id=models.IntegerField(null=True,blank=True)
      def __str__(self):
        return '{} {}'.format(self.studantname, self.c_id)
class Borrow1(models.Model):
    custname=models.ForeignKey(to='Studant', on_delete=models.DO_NOTHING)
    bookname=models.ForeignKey(to='Books', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{} {}'.format(self.custname, self.bookname)
    
       
        
    

      



