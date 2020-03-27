import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from datetime import date
import time
import subprocess
import schedule

# create the email alert
class covid_email_alert:


    def send_email(email, password, recepients):

        #auth

        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        smtp_username = email
        smtp_password = password

        #email_to_sm = 'szu-min_yu@dkcnews.com'
        email_to = recepients
        email_from = email
        email_subject = 'Coronavirus Monitoring Report, ' + str(date.today())


        # send email
        msg = MIMEMultipart()
        msg['Subject'] = email_subject
        msg['TO'] = ', '.join(email_to)
        msg['From'] = email_from

        #body
        words = 'Coronavirus Media and Social Conversation Tracking Report'
        msg.attach(MIMEText(words, 'plain'))

        #file
        filename = 'COVID-19 Monitoring Report ' + str(date.today()) + '.pptx'
        attachment = open(filename, 'rb')
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode to base64
        encoders.encode_base64(part)
        # Add header
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        #Add attachment to your message and convert it to string
        msg.attach(part)
        text = msg.as_string()

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(email_from, email_to, text)

# define my job list
def job():
    exec(open('prep_data.py').read())
    print('Read data')
    subprocess.call(['Rscript', '--vanilla', 'state_dma.r'])
    print('Read R and get the state map')
    exec(open('pptx.py').read())
    print('PPT is done')
    time.sleep(10)
    covid_email_alert.send_email()
    print('Email sent with pptx attached')

# schedule my job

schedule.every().monday.at("09:00").do(job)
schedule.every().tuesday.at("09:00").do(job)
schedule.every().wednesday.at("09:00").do(job)
schedule.every().thursday.at("09:00").do(job)
schedule.every().friday.at("09:00").do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)