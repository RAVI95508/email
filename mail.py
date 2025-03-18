import smtplib 
import random
def send_email():
 sender_email = "********@gmail.com" #usermail
 list=["**********@gmail.com","***********@gmail","***********"] #recipient_email
 for i in list:
       otp_number=random.randint(00000,99999)
       s=smtplib.SMTP("smtp.gmail.com",587)
       s.starttls()
       s.login(sender_email,"passward")
       message=f"Dear user, we are happy to say that you can wrie test,use {otp_number} as passward to attend test"
       s.sendmail(sender_email,i,message)
       print("mail send successfully")
       s.quit()
send_email()         
    





