import boto3
from botocore.exceptions import ClientError

# CONFIG
AWS_REGION = "us-east-1"   # change if needed
SENDER = "noreply@4crisk.ai"      # must be verified in SES
RECIPIENT = "support@4crisk.ai"
SUBJECT = "Test Email from SES"
BODY_TEXT = "Hello,\n\nThis is a test email sent using Amazon SES from a local machine."
BODY_HTML = """
<html>
<head></head>
<body>
  <h2>SES Test Email</h2>
  <p>This email was sent from <b>local machine</b> using Amazon SES.</p>
</body>
</html>
"""

def send_email():
    ses_client = boto3.client("ses", region_name=AWS_REGION)

    try:
        response = ses_client.send_email(
            Source=SENDER,
            Destination={
                "ToAddresses": [RECIPIENT]
            },
            Message={
                "Subject": {
                    "Data": SUBJECT,
                    "Charset": "UTF-8"
                },
                "Body": {
                    "Text": {
                        "Data": BODY_TEXT,
                        "Charset": "UTF-8"
                    },
                    "Html": {
                        "Data": BODY_HTML,
                        "Charset": "UTF-8"
                    }
                }
            }
        )
        print("✅ Email sent successfully!")
        print("Message ID:", response["MessageId"])

    except ClientError as e:
        print("❌ Failed to send email")
        print(e.response["Error"]["Message"])


if __name__ == "__main__":
    send_email()