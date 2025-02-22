

from django.shortcuts import render


"""
Views for the HeyTree application.

This module contains view functions for rendering the homepage,
signup page, and login page.
"""

def HomePage(request):
    """Render the home page."""
    return render(request, "home.html")

def SignupPage(request):
    """Render the signup page."""
    return render(request, "signup.html")

def LoginPage(request):
    """Render the login page."""
    return render(request, "login.html")
# pylint: disable=C0114  # Disable the missing module docstring warning
# pylint: disable=C0114
def some_function():
    pass
# pylint: enable=C0114
