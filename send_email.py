import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

reportname = "report.xml"
fromaddr = "kds360@mail.ru"
toaddr = "chvalena@mail.ru"
mypass = "fB56hZ2RpxtbVNuwb0z6"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"

with open(reportname,"rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename = "%s"' % basename(reportname)
    msg.attach(part)

body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
