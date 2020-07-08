import smtplib

def sending_mail(text):
    print('What is the subject?')
    # time.sleep(3)
    subject = "this is subject"
    print('What should I say?')
    # time.sleep(3)
    message = "this is message"
    content = 'Subject: {}\n\n{}'.format(subject, message)

    # init gmail SMTP
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    # identify to server
    mail.ehlo()

    # encrypt session
    mail.starttls()

    # login
    mail.login('******@gmail.com', '**********')

    # send message
    mail.sendmail('rjrishabh29@gmail.com', 'rjjrishabh29@gmail.com', content)

    # end mail connection
    mail.close()
    print('Email sent.')
