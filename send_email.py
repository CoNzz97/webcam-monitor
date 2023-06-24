import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import imghdr

load_dotenv("B:\\Coding\\Python\\EnviromentVariables\\.env")

MY_EMAIL = os.getenv("webcam_gmail_email")
PASSWORD = os.getenv("webcam_gmail_password")


def send_email(image):
    print("Send Email Started")
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected."
    email_message.set_content("New motion has been detected on Webcam 1.")

    with open(image, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message.as_string())
        connection.quit()
    print("Send Email Ended")


if __name__ == "__main__":
    send_email(image="images/19.png")
