from django import forms

SUSHI_CHOICES = [
    ('Philadelphia Roll', 'Philadelphia Roll'),
    ('California Roll', 'California Roll'),
    ('Green Dragon', 'Green Dragon'),
    ('Spicy Tuna', 'Spicy Tuna'),
    ('Vegetarian Roll', 'Vegetarian Roll'),
    ('Salmon Nigiri', 'Salmon Nigiri'),
    ('Eel Nigiri', 'Eel Nigiri'),
    ('Salmon Sashimi', 'Salmon Sashimi'),
]

STICKS_TYPES = [
    ('Regular', 'Regular'),
    ('Training', 'Training'),
]

class OrderForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    address = forms.CharField(label="Delivery address", max_length=255)
    phone = forms.CharField(
        label="Phone",
        max_length=32,
        help_text="e.g., +380 XX XXX XX XX",
    )
    email = forms.EmailField(label="Email")
    sticks_count = forms.IntegerField(
        label="Number of chopsticks",
        min_value=0, max_value=20, initial=2,
        help_text="You can choose 0 if chopsticks aren’t needed."
    )
    sticks_type = forms.ChoiceField(label="Chopstick type", choices=STICKS_TYPES)
    sushi = forms.MultipleChoiceField(
        label="Sushi selection",
        choices=SUSHI_CHOICES,
        widget=forms.SelectMultiple(attrs={'size': 6}),
    )
    need_napkins = forms.BooleanField(label="Need napkins?", required=False, initial=True)
    need_wasabi = forms.BooleanField(label="Add wasabi and ginger", required=False)
    comment = forms.CharField(label="Additional comment", widget=forms.Textarea(attrs={'rows': 3}), required=False)
    delivery_time = forms.TimeField(
        label="Preferred delivery time",
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        help_text="Select the time for delivery (optional)"
    )
    contact_after = forms.BooleanField(
        label="Contact me after order",
        required=False,
        initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and placeholders
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'e.g., 10 Example St, Apt 5'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': '+380 XX XXX XX XX', 'pattern': '^[+0-9\\s\\-()]{7,}$'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'you@example.com'})
        self.fields['sticks_count'].widget.attrs.update({'class': 'form-control'})
        self.fields['sticks_type'].widget.attrs.update({'class': 'form-select'})
        self.fields['sushi'].widget.attrs.update({'class': 'form-select'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Delivery notes, door code, preferred time, etc.'})
        self.fields['delivery_time'].widget.attrs.update({'placeholder': 'HH:MM'})