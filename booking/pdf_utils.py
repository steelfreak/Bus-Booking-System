from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse

def generate_receipt_pdf(booking):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 50, "Booking Receipt")

    # Booking Details
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Receipt Number: {booking.receipt}")
    p.drawString(100, height - 120, f"Date: {booking.date}")
    p.drawString(100, height - 140, f"Departure Time: {booking.departure_time}")
    p.drawString(100, height - 160, f"Destination: {booking.destination}")
    p.drawString(100, height - 180, f"Seat Number: {booking.seat_number}")
    p.drawString(100, height - 200, f"Passenger: {booking.passenger}")
    p.drawString(100, height - 220, f"Price: ${booking.price}")
    p.drawString(100, height - 240, f"Amount: ${booking.amount}")
    p.drawString(100, height - 260, f"Paid: {'Yes' if booking.paid else 'No'}")
    p.drawString(100, height - 280, f"Number Plate: {booking.number_plate}")

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{booking.receipt}.pdf"'
    return response
