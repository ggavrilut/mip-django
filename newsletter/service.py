from contact.models import Contact

class ContactService:

    def saveNewsletter(email):
        newsletter = Newsletter()
        newsletter.email = email
        newsletter.save()