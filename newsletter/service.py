from contact.models import Contact
from .models import Newsletter

class ContactService:

    def saveNewsletter(self, email):
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()