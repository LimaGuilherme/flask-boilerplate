import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app import config as config_module

config = config_module.get_config()


class Postman(object):

    @classmethod
    def send_welcome_email(cls, guest_name, from_address, to_address, subject):
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = "Notification: {}".format(subject)

            body = """
            Hello, {0}.
            Welcome to My Application
            """.format(guest_name)

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT)
            server.starttls()
            server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()
        except Exception as ex:
            print('ERROR! The postman could not send the email: {}'.format(str(ex)))
