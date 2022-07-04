from .models import Newsletter


class NewsletterRepository:

    @staticmethod
    def create(email: str, user=None):
        new_email = Newsletter.objects.filter(
            newsletter_email=email
        )
        if not new_email:
            if user:
                Newsletter.objects.create(
                    newsletter_email=email,
                    user=user
                )
            else:
                Newsletter.objects.create(
                    newsletter_email=email
                )

    @staticmethod
    def get_all_emails(limit: int = 0) -> Newsletter:
        newsletters_emails = Newsletter.objects.all()
        if limit:
            return newsletters_emails[:limit]
        return newsletters_emails
