import json 
import csv

import markdown2
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# inputs 
with open("config/config.json", "r") as fp:
    config = json.load(fp)

sender = f"'{config['sender_name']}' <{config['sender_email']}>"
print(sender)
markdown_file_path = f"posts/{config['markdown_filename']}"


# get list of subscribers
with open("config/subscribers.csv", 'r') as file:
    reader = csv.DictReader(file)
    recipients = [row["email"] for row in reader]


# open markdown and convert to html content
with open(markdown_file_path, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

html_content = markdown2.markdown(markdown_content)


# send email with SES
ses_client = boto3.client('ses', region_name='us-east-1')

try:
    response = ses_client.send_email(
        Source=sender,
        Destination={'ToAddresses': recipients},
        Message={
            'Subject': {'Data': config['subject']},
            'Body': {
                'Html': {'Data': html_content},
            },
        }
    )
    print("Email sent! Message ID:", response['MessageId'])
except (NoCredentialsError, PartialCredentialsError) as e:
    print("Error: AWS credentials not configured properly.", str(e))
except Exception as e:
    print("An error occurred:", str(e))