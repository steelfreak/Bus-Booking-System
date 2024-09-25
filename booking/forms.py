from django import forms
from .models import Booking, Seat, Bus

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger', 'seat_number']
        widgets = {
            'seat_number': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        bus = kwargs.pop('bus', None)
        super().__init__(*args, **kwargs)
        if bus:
            self.fields['seat_number'].queryset = Seat.objects.all()
            self.instance.departure_time = bus.departure_time
            self.instance.destination = bus.destination
            self.instance.price = bus.price
            self.instance.number_plate = bus.number_plate
            self.instance.amount = bus.price + 1300
            self.fields['seat_number'].queryset = Seat.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        seat_number = cleaned_data.get('seat_number')

        # Check if the seat_number is already booked for the same bus details
        if seat_number:
            existing_bookings = Booking.objects.filter(
                seat_number=seat_number,
                departure_time=self.instance.departure_time,
                date=self.instance.date,
                number_plate=self.instance.number_plate
            )
            if existing_bookings.exists():
                self.add_error('seat_number', 'This seat has already been occupied for this bus journey.')

        return cleaned_data




# from django import forms
# from .models import Booking

class BookingFilterForm(forms.Form):
    date = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    departure_time = forms.TimeField(required=False, widget=forms.TextInput(attrs={'type': 'time'}))
    destination = forms.CharField(required=False)
    number_plate = forms.CharField(required=False)

    def filter_queryset(self, queryset):
        if self.cleaned_data['date']:
            queryset = queryset.filter(date=self.cleaned_data['date'])
        if self.cleaned_data['departure_time']:
            queryset = queryset.filter(departure_time=self.cleaned_data['departure_time'])
        if self.cleaned_data['destination']:
            queryset = queryset.filter(destination__icontains=self.cleaned_data['destination'])
        if self.cleaned_data['number_plate']:
            queryset = queryset.filter(number_plate__icontains=self.cleaned_data['number_plate'])
        return queryset
