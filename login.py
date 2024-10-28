import datetime as dt
import random
from dotenv import load_dotenv
import os
import smtplib

class OTPManager:
    def __init__(self):
        # Load environment variables and set email and password
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('APP_PASSWORD')
        self.otp = None  # This will hold the generated OTP

    def generate_otp(self):
        # Generate a 4-digit OTP
        self.otp = random.randint(1000, 9999)
        self.save_otp()  # Save OTP to file
        print(f"Generated OTP: {self.otp}")  # For debugging; remove in production

    def save_otp(self):
        # Save OTP to a file for persistence
        with open("working-with-email/otp.txt", "w") as otp_file:
            otp_file.write(str(self.otp))

    def send_otp(self, recipient_email):
        # Send OTP via email to the recipient
        if self.otp is None:
            self.generate_otp()

        # Setup email connection and send the OTP
        # try:
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=recipient_email,
                msg=f"Subject: Your OTP\n\nYour OTP is {self.otp}. Please use it within 5 minutes."
            )
            connection.close()
            # print("OTP sent successfully.")
        # except Exception as e:
        #     print(f"Error sending email: {e}")

    def verify_otp(self, user_input_otp):
        # Verify the OTP entered by the user
        if str(user_input_otp) == self.otp:
            return True
        else:
            return False