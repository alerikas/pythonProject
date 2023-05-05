import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage


# elementarios email žinutės sukūrimas:
email = EmailMessage()
email['from'] = 'Prievartautojas Ojas Ojasaleksane'
email['to'] = 'karolinutepl@gmail.com'
email['subject'] = 'email from python'

email.set_content('Sveiki adresate,\n\nKarolyte buk gerute \n jei nebusi \n Tai tave pagausiu ir isprievartausiu\n\npagarbiai, siuntėjas')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
    smtp.starttls() # inicijuojame šifruotą kanalą
    smtp.login('eriss97@gmail.com', 'pcbgxppqcnryfiaj') # nurodome prisijungimo duomenis
    smtp.send_message(email) # išsiunčiame žinutę

print("Done")