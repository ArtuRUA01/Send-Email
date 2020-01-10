import smtplib

class send_mail():
    def __init__(self, user_mail, user_password):
        self.email = user_mail
        self.password = user_password
        self.server = 'smtp.gmail.com'
        self.port = 465
        session = smtplib.SMTP_SSL( self.server, self.port)
        session.ehlo()
        session.login(self.email, self.password)
        self.session = session

    def send_email(self, send_to, subject, text):
        email_text = [
            'From: ' + self.email,
            'To: ' + send_to,
            'Subject: ' + subject,
            text
        ]
        email_text = '\r\n'.join(email_text)
        self.session.sendmail(self.email, send_to, email_text)
        self.session.close()
        print('Email sent!')

gmail_user = 'inpit user email'
gmail_password = 'input password'



# sent1 = send_mail(gmail_user, gmail_password)
# text = 'text which you want to send'
# sent1.send_email('enter the email to whom you want to send the message', 'subject', text)

