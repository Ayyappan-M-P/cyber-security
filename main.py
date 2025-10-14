# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# from config import SENDGRID_API_KEY, TARGET_EMPLOYEES, SENDER_EMAIL

# def send_email(target_email, subject, body):
#     message = Mail(
#         from_email=SENDER_EMAIL,
#         to_emails=target_email,
#         subject=subject,
#         html_content=body)
#     try:
#         sg = SendGridAPIClient(SENDGRID_API_KEY)
#         response = sg.send(message)
#         print(f"Email sent to {target_email}: Status {response.status_code}")
#     except Exception as e:
#         print(f"Failed to send email to {target_email}: {e}")

# def main():
#     subject = "Phishing Awareness Test"
#     body = """
#     <p>Dear Employee,</p>
    
#     <p>This is a simulated phishing email for training purposes. Please do not click on any links or provide any personal information.</p>
#     <p>Best regards,<br>Your IT Security Team</p>
#     """
#     for employee in TARGET_EMPLOYEES:
#         send_email(employee, subject, body)

# if __name__ == "__main__":
#     main()


import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import SENDGRID_API_KEY, TARGET_EMPLOYEES, SENDER_EMAIL

def send_email(target_email, subject, body):
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=target_email,
        subject=subject,
        html_content=body
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent to {target_email}: Status {response.status_code}")
    except Exception as e:
        print(f"Failed to send email to {target_email}: {e}")

def main():
    subject = "Phishing Awareness Test"
    body = """
    <p>Dear Employee,</p>
    <p>This is a simulated phishing email for training purposes. Please do not click on any links or provide any personal information.</p>
    <p>Click <a href="http://localhost:5000/track?email={{email}}">here</a> for more details.</p>
    <p>Best regards,<br>Your IT Security Team</p>
    """
    for employee in TARGET_EMPLOYEES:
        personalized_body = body.replace("{{email}}", employee)
        send_email(employee, subject, personalized_body)

if __name__ == "__main__":
    main()
