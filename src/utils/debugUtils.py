# debugUtils.py

from dependencies.dependencies import *

def print_email(email_message):
    print(f"From: {email_message['from']}")
    print(f"To: {email_message['to']}")
    print(f"Subject: {email_message['subject']}")
    print(email_message.get_body(preferencelist=('plain', 'html')).get_content())

def print_email_list(emails):
    for email in emails:
        print_email(email)
        print("\n\n")

def print_email_list_with_index(emails):
    for index, email in enumerate(emails):
        print(f"Email {index}")
        print_email(email)
        print("\n\n")

def logger(message, error: bool):
        log_dir = '../logs'
        os.makedirs(log_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"[{timestamp}] : {message}\n"

        log_file = 'error.txt' if error else 'logs.txt'
        with open(os.path.join(log_dir, log_file), 'a') as f:
            f.write(formatted_message)

        with open(os.path.join(log_dir, 'history.txt'), 'a') as f:
            f.write(formatted_message)
    