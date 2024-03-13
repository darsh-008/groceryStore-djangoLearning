from django import forms
from myapp.models import *
class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('item', 'client', 'quantity_ordered')
        widgets={'client': forms.RadioSelect}
        labels={'quantity_ordered':'Quantity', 'client':'Client Name'}

class InterestForm(forms.Form):
    # interested = forms.RadioSelect(label='Interested' ,choices=((1,'Yes'),(0,'No')))
    interested = forms.ChoiceField(label='Interested', widget=forms.RadioSelect, choices=((1, 'Yes'), (0, 'No')))
    quantity = forms.IntegerField(label='Quantity', initial=1, min_value=1)
    comment = forms.CharField(label='Additional Comments', widget=forms.Textarea, required=False)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['shipping_address', 'city']
        labels = {
            'shipping_address': 'client_add',
            'city': 'client_city'
        }

class ItemSearchForm(forms.Form):
    items = forms.ModelChoiceField(queryset=item.objects.all(), label='Select Item', empty_label=None)

class CityForm(forms.Form):
    items = forms.ModelChoiceField(queryset=Client.objects.all(), label='Select Item', empty_label=None)