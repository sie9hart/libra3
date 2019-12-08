from django.shortcuts import render
from libra.models import Books , Borrow1, Studant
from django.http import HttpResponse
from libra.forms import Book_Form,Studant_Form,Borrow_Form
from django.contrib import messages
def home(request):
    return render(request,"home.html")



def books_list(request):

    var={}
    Booklist=Books.objects.all()
    var['my_list2']=Booklist
    return render(request,'books.html',context=var)




def studant_list(request):
   
    var={}
    studantlist=Studant.objects.all()
    var['my_list2']=studantlist
    return render(request,'custs.html',context=var)


    
def Borrows_list(request):
   
    var={}
    borrowlist=Borrow1.objects.all()
    var['borrow_list']=borrowlist
    return render(request,'Borrow.html',context=var) 


def addbook(request):
    var={}
    var['forms']=Book_Form
     
    if request.method =="POST":
        form=Book_Form(request.POST)
        if form.is_valid():
            
            isbninputchecker=form.cleaned_data['isbn']
            checkisbn=Books.objects.filter(isbn=isbninputchecker).exists()
            if checkisbn:
               messages.warning(request, 'this book is registered .')  

            else:  
              form.save()
    return render(request,'addbook.html',context=var)


def addstudant(request):
        var={}
        var['forms']=Studant_Form
        
        if request.method =="POST":
            
            form=Studant_Form(request.POST)
            if form.is_valid():

                c_id_var=form.cleaned_data['c_id']
                checkstudant=Studant.objects.filter(c_id=c_id_var).exists()
                
                if checkstudant:
                    messages.warning(request, 'this cust is registered .')  
                else:
                    form.save()
        return render(request,'addstudant.html',context=var)

def makeborrow(request):
        var={}
        var['forms'] = Borrow_Form
        
        
        if request.method =="POST":
            form=Borrow_Form(request.POST)
            if form.is_valid():
                new_b = Borrow1()
                
                new_book = Books()
                booknamevar = new_book.bookname=form.cleaned_data['bookname']
                borrownamevar = new_b.custname=form.cleaned_data['custname']
                borrowbookvar =new_b.bookname=form.cleaned_data['bookname']
                
                if  Borrow1.objects.filter(bookname=borrowbookvar).exists() :
                    if Borrow1.objects.filter(custname=borrownamevar).exists():
                        post = Books.objects.get (bookname=booknamevar.bookname)    
                        if Books.objects.filter(available=False).exists():
                                post.available = True
                                Borrow1.objects.filter(bookname=borrowbookvar).delete()
                                post.save()
                                messages.success(request, 'return success')
                        
                    else:
                                messages.error(request, 'this is not who borrow the book')
                                        
                                
                else :           
                    post = Books.objects.get (bookname=booknamevar.bookname)
                    if Books.objects.filter(available=True).exists():
                            post.available = False
                            post.save()
                        
                            new_b.save()
                            messages.success(request, 'booking succss')
                    

        return render(request,'makeborrow.html',context=var) 

def Borrow_details(request, id):
    var = {}
    std = Studant.objects.get(id=id)
    borrowstd = Borrow1.objects.filter(custname= std)
    
    var['st'] = borrowstd
    

    return render(request,'Borrow_details.html',context=var)