# Bus Booking System

## Project Description

The **Bus Booking System** is a web-based application developed using Django that simplifies the process of booking bus tickets. Users can search for available bus routes, view schedules, and make reservations with ease. A standout feature of this application is the integration of **MOMO Pay**, allowing users to make secure payments through the MOMO API.

### Features

- **User Registration and Login**: Secure user accounts for managing bookings.
- **Bus Route Search**: Find available bus routes based on departure and arrival locations.
- **Real-Time Availability**: Check seat availability in real time.
- **Booking Management**: View, modify, and cancel bookings.
- **MOMO Pay Integration**: Secure and convenient payment option through the MOMO API.
- **Email Notifications**: Receive booking confirmations and updates via email.
- **Admin Dashboard**: Manage bus schedules, routes, and user accounts.

### Tech Stack

- **Frontend**: HTML and CSS
- **Backend**: Django (Python)
- **Database**: PostgreSQL (or SQLite for development)
- **Payment Integration**: MOMO API

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/steelfreak/Bus-Booking-System.git
   
   ```
   GitHub CLI
   ```bash
   gh repo clone steelfreak/Bus-Booking-System
   ```
   SSH
   ```bash
   git@github.com:steelfreak/Bus-Booking-System.git
   ```
   HTTPS
   ```bash
   https://github.com/steelfreak/Bus-Booking-System.git
   ```
3. Navigate to the project directory:
   ```bash
   cd Bus-Booking-System
   ```
4. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set up environment variables for MOMO API and database settings in a `.env` file:
   - `MOMO_API_KEY`
   - `MOMO_SECRET`
   - Database configurations

7. Run database migrations:
   ```bash
   python manage.py migrate
   ```
8. Start the development server:
   ```bash
   python manage.py runserver
   ```

### API Documentation

For details on how to use the MOMO Pay API, please refer to the [MOMO API documentation](https://momoapi.com/docs).

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

### License

This project is licensed under the MIT License.

---

Feel free to adjust any sections to better suit your project details!

---
___
All the best i remain Steelfreak (Kinen Key Samson) 
Happy Coding...!!!
