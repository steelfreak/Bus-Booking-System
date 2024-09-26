Integrating Google authentication into your Django application involves using OAuth 2.0 to allow users to sign in with their Google accounts. Here's a step-by-step guide to add Google authentication to your Django app using `django-allauth`, which is a popular library for handling authentication with various providers.

### 1. Install Required Packages

You'll need `django-allauth` and `django` if you haven't installed them already.

```bash
pip install django
pip install django-allauth
```

### 2. Update Django Settings

Update your Django settings to include `django-allauth` and configure it for Google authentication.

#### `settings.py`

Add the following apps to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # Other apps
    'django.contrib.sites',  # Required by django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Add this line for Google
]
```

Set up the authentication backends:

```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Keep default backend
    'allauth.account.auth_backends.AuthenticationBackend',  # Add django-allauth backend
)
```

Set the site ID:

```python
SITE_ID = 1
```

Configure `django-allauth`:

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'username'  # or 'email' if you prefer email login
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # or 'mandatory' based on your needs
SOCIALACCOUNT_QUERY_EMAIL = True
```

### 3. Configure URLs

Include `django-allauth` URLs in your project's URL configuration.

#### `urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
]
```

### 4. Set Up Google OAuth 2.0

1. **Go to the Google Developers Console**: [Google Developers Console](https://console.developers.google.com/)

2. **Create a new project**: If you don’t have one already, create a new project.

3. **Enable the Google+ API**: Go to "Library" and search for "Google+ API" and enable it. (Note: Google+ API is deprecated, but Google Sign-In will still work through `OAuth 2.0`.)

4. **Create OAuth 2.0 Credentials**:
   - Navigate to "Credentials" and click "Create Credentials" > "OAuth 2.0 Client IDs".
   - Choose "Web application" and configure the **Authorized Redirect URIs**. For local development, this might be something like `http://localhost:8000/accounts/google/login/callback/`.
   - Note down your **Client ID** and **Client Secret**.

5. **Add Google Credentials to Django**:
   - Go to your Django admin panel (usually at `http://localhost:8000/admin`).
   - Navigate to **Sites** and ensure you have an entry for your domain (e.g., `localhost` for local development).
   - Go to **Social applications** and create a new social application for Google. Enter your Client ID and Client Secret obtained from Google.
   - Assign this application to your site.

### 5. Migrate Database

Run migrations to create necessary tables:

```bash
python manage.py migrate
```

### 6. Set Up the Login URL

You can now use Django’s built-in authentication views, or create your own views and templates. Django-allauth provides login and authentication pages out of the box.

#### Example Login URL

You can access the Google login by visiting:

```
http://localhost:8000/accounts/google/login/
```

### 7. Create a Login Template (Optional)

If you want to customize the login page, create a template:

#### `templates/account/login.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <a href="{% url 'account_login' %}">Login with Email</a><br>
    <a href="{% url 'socialaccount_login' 'google' %}">Login with Google</a>
</body>
</html>
```

### Summary

1. **Install `django-allauth`** and configure it in your `settings.py`.
2. **Add URL patterns** for authentication in `urls.py`.
3. **Set up Google OAuth 2.0** by creating credentials in the Google Developers Console and adding them to Django.
4. **Run migrations** and test the Google login flow.

This setup will enable Google authentication for your Django application, allowing users to sign in using their Google accounts.
