def print_email_summary(email, summary):
    print(f"\nSubject: {email['subject']}")
    print(f"From: {email['from']}")
    print("Summary:\n" + summary)
    print("="*50)
