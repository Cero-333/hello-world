from smtplib import SMTP

try:

    # set up some fundamental requirements
    message = "Hello! Check out the new video!"
    subject = "Hello Pal"
    content = "Subject: {0}\n\n{1}".format(subject, message)

    myMailAdress = "ceren.sahin04@gmail.com"
    myPassword = "your password comes here"

    sendTo = "ceren.sahin04@gmail.com"

    # How to send?
    mail = SMTP("smtp.gmail.com", 587)

    mail.ehlo()

    mail.starttls()

    mail.login(myMailAdress, myPassword)

    mail.sendmail(myMailAdress, sendTo, content)
    print("Gönderdim")

except Exception as e:
    print(e)
