from gmail_client import authenticate_gmail, get_recent_emails
from summarizer import summarize_email
from utils import print_email_summary

def main():
    print("🔐 Authenticating Gmail...")
    service = authenticate_gmail()

    print("📥 Fetching Emails...")
    emails = get_recent_emails(service)

    for email in emails:
        summary = summarize_email(email['body'])
        print_email_summary(email, summary)

if __name__ == "__main__":
    main()
