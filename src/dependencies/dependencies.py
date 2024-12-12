# dependencies.py

# Bibliothèques standard
import smtplib
import base64
import imaplib
import os
import time
from datetime import datetime
from email import message_from_bytes
from email.header import decode_header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.parser import BytesParser
from email.policy import default

# Bibliothèques tierces
from imapclient import IMAPClient
from dotenv import load_dotenv
