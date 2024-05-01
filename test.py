import smtplib

EMAIL_HOST = 'live.smtp.mailtrap.io'
EMAIL_HOST_USER = 'api'
EMAIL_HOST_PASSWORD = '575949836b8e40d2042a8ee8dd692588'
EMAIL_PORT = '587'

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()  # Enable STARTTLS
server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

# Rest of your email sending code
