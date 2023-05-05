import smtplib
from email.message import EmailMessage
from string import Template

with open('index.html', 'r') as f:
    html = f.read()

sablonas = Template(html)

email = EmailMessage()
email['from'] = 'Meskiukas'
email['to'] = 'karolinutepl@gmail.com'
email['subject'] = 'email from python'

email.set_content(sablonas.substitute({'vardas': 'Enrike'}), 'html')

with open('elephant.png', 'rb') as file:
    content = file.read()
    email.add_attachment(
        content,
        maintype='image/png',
        subtype='png',
        filename='elephant.png')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('eriss97@gmail.com', 'pcbgxppqcnryfiaj')
    smtp.send_message(email)

print('Done')