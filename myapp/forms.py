from django import forms
from myapp.models import OrderItem
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem.objects.all()
        fields = ('item', 'client', 'quantity_ordered')
        widgets={'client': forms.RadioSelect}
        labels={'quantity_ordered':'Quantity', 'client':'Client Name'}

class InterestForm(forms.Form):
    interested = forms.RadioSelect(label='Interested' ,choices=((1,'Yes'),(0,'No')))
    quantity = forms.IntegerField(label='Quantity', initial=1, min_value=1)
    comment = forms.CharField(label='Additional Comments', widget=forms.Textarea, required=False)

