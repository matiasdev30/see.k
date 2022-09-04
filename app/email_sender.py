import email
import smtplib

email_body = """Test email"""
gmail_smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
gmail_smtpserver.starttls()
gmail_smtpserver.login(user='matiasdev30@gmail.com', password='Mvninull00')
gmail_smtpserver.sendmail('matiasdev30@gmail.com', 'null.comercil@gmail.com', email_body)
gmail_smtpserver.quit()

