from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import contactForm
import random
from product.models import Product

# def shopHome(req):
#     data={
# 'heading':'shop home page',
# 'text':'''Lorem ipsum dolor sit, amet consectetur adipisicing elit. Atque repellat perspiciatis consequuntur debitis
#         reiciendis iste nam! Quis non commodi a unde earum distinctio recusandae molestias assumenda eum ipsa, eveniet
#         maxime?''',
# 'product':["tea","coffie","water","milk"],
# 'quantity':[10,20,50,80,70]

#     }
#     return render(req,"index.html",data)


def shopHome(req):
    context = random.randint(100, 1000)

    # allproducts=Product.objects.all().order_by('-product_name')[2:5]
    allproducts=Product.objects.all()

    data={
    'randomnum': context,
    'product': allproducts,


    }
    

    return render(req,"index.html", data)


def productDes(req,id):
   productDetail=Product.objects.get(id=id)
   data={
    'productDetail':productDetail

    }
   return render(req,"productdetails.html",data)


def about(req):
    return render(req,"about-us.html")

def faq(req):
    return render(req,"faq.html")



def fromdata(req):
    return HttpResponse(req)


def contact(req):
    return render(req,"contact-us.html")





def contact_form(req):

    fn=contactForm()
    formData = {'contactfrom':fn}

    try:
       if req.method=="POST":
         temp = req.POST.get('fname')
         temp2 = req.POST.get('phone_number')
         print(temp)
         print(temp2)
        #  return HttpResponseRedirect('/contact/')
         return redirect('/contact/')

    #    temp = req.GET['fname']
    #    temp2 = req.GET['phone_number']
        # temp = 1
    except:
        pass

    return render(req,"contact-form.html",formData)




def calc(req):
    
    fn=contactForm()
    
    n1=int(req.POST.get('num1'))
    n2=int(req.POST.get('num2'))
    opr=req.POST.get('select_oprator')
   
    output=0
    
    try:
   
     if(opr=="+"):
       output=n1+n2
     elif(opr=="-"):
        output=n1-n2
     elif(opr=="*"):
        output=n1*n2
     elif(opr=="/"):
        output=n1/n2
     elif(opr=="%"):
       output=n1%n2

    except:
      
      output = "nota vaild oprator"


    formData = {'contactfrom':fn,
    'output': output
    }

    return render(req,"calc.html",formData)

