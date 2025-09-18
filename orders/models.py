from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Order(models.Model):
    STICKS_TYPES = [
        ('Regular', 'Regular'),
        ('Training', 'Training'),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=32,
        validators=[RegexValidator(r'^[+0-9\s\-()]{7,}$', message='Enter a valid phone number.')]
    )
    email = models.EmailField()
    sticks_count = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    sticks_type = models.CharField(max_length=20, choices=STICKS_TYPES)
    need_napkins = models.BooleanField(default=True)
    need_wasabi = models.BooleanField(default=False)
    sushi_json = models.TextField(help_text="JSON array of selected sushi items")
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.pk} by {self.name}'