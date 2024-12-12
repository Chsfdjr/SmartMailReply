# emailUtils.py

from dependencies.dependencies import *
from utils.debugUtils import *

load_dotenv()

IMAP_SERVER = os.getenv('IMAP_SERVER')
SMTP_SERVER = os.getenv('SMTP_SERVER')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


def connectImap():
    try:
        client = IMAPClient(IMAP_SERVER)
        client.login(EMAIL, PASSWORD)
        logger("Connexion au serveur IMAP réussie.", False)
        return client
    except Exception as e:
        logger(f"Erreur lors de la connexion au serveur IMAP : {e}", True)

def sendMessageToSomeone(subject, body, recipient):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        logger("E-mail envoyé avec succès.", False)
    except Exception as e:
        logger(f"Erreur lors de l'envoi de l'e-mail : {e}", True)

def sendMessageToDraft(client, subject, body, recipient):
    try:
        message = MIMEMultipart()
        message['From'] = EMAIL
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        client.select_folder('[Gmail]/Brouillons')

        raw_message = f"From: {EMAIL}\r\nTo: {recipient}\r\nSubject: {subject}\r\n\r\n{body}".encode('utf-8')
        
        client.append('[Gmail]/Brouillons', raw_message)
        
        logger("Brouillon sauvegardé dans le dossier Brouillons.", False)

    except Exception as e:
        logger(f"Erreur lors de la sauvegarde du brouillon via IMAP : {e}", True)

def fetch_unread_emails(client):
    try:
        client.select_folder('INBOX')
        messages = client.search(['UNSEEN'])
        emails = []

        for message_id in messages:
            response = client.fetch(message_id, ['RFC822'])
            raw_email = response[message_id][b'RFC822']
            email_message = BytesParser(policy=default).parsebytes(raw_email)        
            subject, encoding = decode_header(email_message['Subject'])[0]
            if subject is not None and isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else 'utf-8')
            elif subject is None:
                subject = "(No Subject)"    

            emails.append({
                'subject': email_message['subject'],
                'from': email_message['from'],
                'to': email_message['to'],
                'body': email_message.get_body(preferencelist=('plain', 'html')).get_content()
            })

        return emails
    except Exception as e:
        logger(f"Erreur lors de la récupération des e-mails non lus : {e}", True)

def list_folders(client):
    try:
        folders = client.list_folders()
        print("Dossiers disponibles :")
        for folder in folders:
            print(folder)
    except Exception as e:
        logger(f"Erreur lors de la récupération des dossiers : {e}", True)
