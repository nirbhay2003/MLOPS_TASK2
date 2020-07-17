import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("kumarnirbhay2688@gmail.com","****")

subject1='Important'


message1 = "your latest code ha been failed, please debug it as soon as possible."

s.sendmail("kumarnirbhay2688@gmail.com","1706339@kiit.ac.in",message1)

s.quit()
