from src.proxy_smtp import ProxySMTP
from src.proxy_imap import SocksIMAP4SSL


SMTP_SERVER = '' # SMTP SERVER eg `smtp.gmail.com`
SMTP_PORT = 587 # SMTP PORT 25, 445, 587
IMAP_SERVER = '' # IMAP SERVER eg `imap.gmail.com`
IMAP_PORT = 993
SMTP_USERNAME = '' # SMTP LOGIN CREDENTIAL
SMTP_PASSWORD = '' # SMTP LOGIN CREDENTIAL
SMTP_EMAIL_ADDRESS = '' # SMTP EMAIL ADDRESS
IMAP_USERNAME = '' # # IMAP LOGIN CREDENTIAL
IMAP_PASSWORD = '' # IMAP LOGIN CREDENTIAL
IMAP_EMAIL_ADDRESS = '' # IMAP EMAIL ADDRESS
TO_EMAIL = '' # EMAIL ADDRESS TO WHICH MESSAGE SHOULD BE SENT 
MESSAGE = '' # EMAIL MESSAGE TO BE SENT

PROXY_DETAILS = dict()
PROXY_DETAILS['host'] = '' # PROXY HOST
PROXY_DETAILS['port'] = '' # PROXY PORT
PROXY_DETAILS['username'] = '' # PROXY CREDENTIAL
PROXY_DETAILS['password'] = '' # PROXY CREDENTIAL

# SMTP - SEND EMAIL MESSAGE

smtp = ProxySMTP(SMTP_SERVER, SMTP_PORT, proxy_addr=PROXY_DETAILS['host'], proxy_port=PROXY_DETAILS['port'],
                         proxy_username=PROXY_DETAILS['username'], proxy_password=PROXY_DETAILS['password'])
smtp.starttls()

smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
smtp.sendmail(
    SMTP_EMAIL_ADDRESS,
    TO_EMAIL, MESSAGE
)
smtp.quit()


# IMAP - READ EMAIL MESSAGES

imap = SocksIMAP4SSL(IMAP_SERVER, IMAP_PORT, proxy_addr=PROXY_DETAILS['host'], proxy_port=PROXY_DETAILS['port'],
                             username=PROXY_DETAILS['username'], password=PROXY_DETAILS['password'])

imap.login(IMAP_USERNAME, IMAP_PASSWORD)

imap.logout()
