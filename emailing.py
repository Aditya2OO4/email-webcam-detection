import smtplib
import os
from email.message import EmailMessage
from PIL import Image

PASSWORD = os.getenv("Password")
SENDER = "adityasnalla1412@gmail.com"
RECEIVER = "adityasnalla1412@gmail.com"

def get_image_type(image_path):
    with Image.open(image_path) as img:
        return img.format.lower()

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!!"
    email_message.set_content("Hey, we just saw a new customer!!!")

    with open(image_path, "rb") as file:
        content = file.read()

    image_type = get_image_type(image_path)
    email_message.add_attachment(content, maintype="image", subtype=image_type)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/15.png")
