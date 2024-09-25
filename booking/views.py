from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Bus, Booking
from .forms import BookingForm
from .forms import BookingFilterForm
from django.http import HttpResponse
from .pdf_utils import generate_receipt_pdf
from django.contrib.auth.decorators import login_required

@login_required
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'booking/bus_list.html', {'buses': buses})


def success(request):
    return render(request, 'booking/success.html')



# from .pdf_utils import generate_receipt_pdf
@login_required
def book_bus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, bus=bus)
        if form.is_valid():
            booking = form.save()
            # After saving, redirect to success page
            return redirect('transaction_success', booking_id=booking.id)
    else:
        form = BookingForm(bus=bus)

    return render(request, 'booking/book_bus.html', {'form': form, 'bus': bus})




# from django.urls import reverse
# from django.shortcuts import get_object_or_404, render
# from .models import Booking
@login_required
def transaction_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    pdf_url = reverse('download_receipt', args=[booking_id])
    return render(request, 'booking/success.html', {
        'booking': booking,
        'pdf_url': pdf_url
    })



# def transaction_success(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     pdf_url = reverse('download_receipt', args=[booking_id])
#     return render(request, 'booking/success.html', {
#         'booking': booking,
#         'pdf_url': pdf_url
#     })




@login_required
def filtered_bookings(request):
    form = BookingFilterForm(request.GET or None)
    bookings = Booking.objects.all()
    
    if form.is_valid():
        bookings = form.filter_queryset(bookings)

    return render(request, 'booking/filtered_bookings.html', {'form': form, 'bookings': bookings})




from django.http import HttpResponse
from .models import Booking
from .pdf_utils import generate_receipt_pdf
@login_required
def download_receipt(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return generate_receipt_pdf(booking)



# def download_receipt(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     return generate_receipt_pdf(booking)


# from django.shortcuts import get_object_or_404, render, redirect
# from django.urls import reverse
# from django.http import HttpResponse
# from .models import Booking
# from .pdf_utils import generate_receipt_pdf

# def download_receipt(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
    
#     # Generate the PDF and save it to a file or URL
#     pdf_response = generate_receipt_pdf(booking)
    
#     # Here you might save the PDF to a file system or store its URL
#     # For demonstration, we will just redirect to a success page

#     # Assuming you have a mechanism to store or provide the PDF URL
#     pdf_url = reverse('receipt_pdf', args=[booking_id])  # Update this if needed

#     # Redirect to a success page with the receipt URL
#     return redirect('transaction_success', booking_id=booking_id)




