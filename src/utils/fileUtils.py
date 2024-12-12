# fileUtils.py

from dependencies.dependencies import *
from utils.debugUtils import *

def saveEmailReceived(email_message, subject, from_address):
    try:
        os.makedirs('../data/responses', exist_ok=True)

        from_address = from_address.replace('<', '').replace('>', '').replace('@', '_at_').replace('.', '_').replace(' ', '_')
        subject_sanitized = subject.replace(' ', '-').replace('/', '_')
        file_path = f"../data/responses/data_{from_address}_{subject_sanitized}.txt"

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"From: {email_message['from']}\n")
            file.write(f"To: {email_message['to']}\n")
            file.write(f"Subject: {subject}\n\n")
            file.write(f"{email_message['body']}\n")
        logger(f"Email received from {from_address} with subject {subject}", False)
    except Exception as e:
        logger(f"Error saving email received from {from_address} with subject {subject}: {str(e)}", True)

def SaveEmailTraited(email_message, subject, from_address, body):
    try:
        os.makedirs('../data/traits', exist_ok=True)

        from_address = from_address.replace('<', '').replace('>', '').replace('@', '_at_').replace('.', '_').replace(' ', '_')
        subject_sanitized = subject.replace(' ', '-').replace('/', '_')
        file_path = f"../data/traits/data_{from_address}_{subject_sanitized}.txt"

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"From: {email_message['from']}\n")
            file.write(f"To: {email_message['to']}\n")
            file.write(f"Subject: {subject}\n\n")
            file.write(body)
        logger(f"Email traited from {from_address} with subject {subject}", False)
    except Exception as e:
        logger(f"Error saving email traited from {from_address} with subject {subject}: {str(e)}", True)
