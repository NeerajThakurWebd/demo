from django import forms

class contactForm(forms.Form):
    num1=forms.CharField(widget=forms.TextInput(attrs={"class":'fn_input'}))
    num2=forms.CharField(widget=forms.TextInput(attrs={"class":'fn_input'}))

    oprators= [
    ("+","+"),
    ("-","-"),
    ("*","*"),
    ("/","/"),
    ("%","%"),
           
           ]

    select_oprator=forms.ChoiceField(choices=oprators, label="Select Your oprator", widget=forms.Select(attrs={"class":'fn_input'}))

