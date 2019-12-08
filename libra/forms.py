from django import forms
from django.forms.models import ModelForm
from libra.models import Books,Studant,Borrow1







        



class Book_Form(ModelForm):
      class Meta:
                model = Books
                fields = "__all__"

class Studant_Form(ModelForm):
        class Meta:
                model = Studant
                fields = "__all__"
class Borrow_Form(ModelForm):
      class Meta:
                model = Borrow1
                fields = "__all__"
