import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    # Email sender and receiver
    sender_email = "your_email@gmail.com"  # Replace with your Gmail address
    receiver_email = to_email
    password = "your_email_password"  # Replace with your Gmail password

    # Setting up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Email body
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login with your Gmail credentials
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        server.quit()  # Logout from the server
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
