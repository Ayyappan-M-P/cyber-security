#cyber-security projects 
# Phishing Awareness Training Project

This project is designed to simulate phishing attacks to raise awareness and train employees to recognize phishing threats. The system sends emails to specified targets and tracks who clicks on a link within the email, logging the data into an Excel file.

## Features

- Send phishing awareness emails to multiple recipients.
- Track when recipients click on a link in the email.
- Record recipient email addresses and click timestamps in an Excel file.

## Prerequisites

- Python 3.x
- [SendGrid API Key](https://sendgrid.com/solutions/email-api/)
- SMTP server access (for email sending)
- Flask and OpenPyXL libraries

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/phishing-awareness-training.git
   cd phishing-awareness-training
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


pip install -r requirements.txt

# config.py

SENDGRID_API_KEY = 'your-sendgrid-api-key'
SENDER_EMAIL = 'youremail@example.com'
TARGET_EMPLOYEES = [
    'employee1@example.com',
    'employee2@example.com',
    # Add more employee emails here
]


python app.py


python main.py


.
├── app.py              # Flask application to track clicks
├── config.py           # Configuration file with API keys and target emails
├── main.py             # Script to send emails
├── requirements.txt    # Python package dependencies
└── clicks.xlsx         # Excel file where click data is stored

License



### Additional Tips for Your README

- **Replace placeholders:** Ensure you replace placeholders like `yourusername`, `your-sendgrid-api-key`, and `youremail@example.com` with actual values relevant to your project.
- **Instructions for running the server in production:** If you have specific instructions for deploying the server in a production environment, consider adding those to the `Deployment` section.
- **Screenshots:** If applicable, add screenshots or diagrams to illustrate the workflow or architecture of the project.
- **FAQ section:** Consider adding a FAQ section to address common questions or issues users might encounter.

By following this template, you'll provide a clear and informative README that helps users understand your project and get started with it quickly.

