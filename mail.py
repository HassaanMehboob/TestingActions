import email, smtplib, ssl
import pathlib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''
Basic Explaination:
	Export Errors through Email using a Temp gmail account, by 
	opening a SSL connection with the google server. 

Required Inputs: 
	Path = (Path to the files Errors Output File):  Would assume to be Outputs/Errors.csv

Sample Execution:
	Email(path = 'Outputs/Errors.csv')
'''

class Email():
	def __init__(self,path=None):
		self.location=path
		subject = "Errors File Attached"
		body = "This file contains all the relevant errors that would be faced"

		sender_email = "vyndfurniture@gmail.com"
		receiver_email = "technicalsupport@vynd.com.au"
		password = "Temp123*"

		# Create a multipart message and set headers
		message = MIMEMultipart()
		message["From"] = sender_email
		message["To"] = receiver_email
		message["Subject"] = subject
		message["Bcc"] = receiver_email  # Recommended for mass emails

		# Add body to email
		message.attach(MIMEText(body, "plain"))
		filename = str(pathlib.Path(__file__).parent.parent/"Output/ERRORS.csv")  # In same directory as script
		# print(pathlib.Path(__file__))
		with open(filename, "rb") as attachment:
			# Add file as application/octet-stream
			# Email client can usually download this automatically as attachment
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		# Encode file in ASCII characters to send by email    
		encoders.encode_base64(part)
		s = "ERRORS.csv"
		# Add header as key/value pair to attachment part
		part.add_header(
			"Content-Disposition",
			f"attachment; filename= {s}",
		)

		# Add attachment to message and convert message to string
		message.attach(part)
		text = message.as_string()

		# Log in to server using secure context and send email
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
			server.login(sender_email, password)
			server.sendmail(sender_email, receiver_email, text)
