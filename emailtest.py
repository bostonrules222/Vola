import smtplib, ssl

testlst = [1,2,3]

sender_email = "maxarilltestdev@gmail.com"
receiver_email = "maxarilltestdev@gmail.com"
message = ''.join(str(e) for e in testlst)



port = 465  # For SSL
password = '123GoSox!'
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login("maxarilltestdev@gmail.com", password)
	server.sendmail(sender_email, receiver_email, message)