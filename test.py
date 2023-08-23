import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from dotenv import load_dotenv
load_dotenv()

smtp_server = os.environ['smtp_server']
smtp_port = os.environ['smtp_port']
sender_email = os.environ['sender_email']
sender_password = os.environ['sender_password']
recipient_email = os.environ['recipient_email']

def send_email():
	subject = 'Sample email'
	message = 'This is a sample email sent using Python'

	msg = MIMEMultipart()
	msg['From'] = formataddr(('Brian', sender_email))
	msg['To'] = recipient_email
	msg['Subject'] = subject

	msg.attach(MIMEText(message, 'plain'))

	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.login(sender_email, sender_password)
		server.sendmail(sender_email, recipient_email, msg.as_string())
		server.quit()
		print('Email sent successfully!')
	except Exception as e:
		print('Error:', e)

if __name__ == '__main__':
	send_email()

