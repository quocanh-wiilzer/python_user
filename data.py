import imaplib
import email
import sys
import pytz
import datetime

timezone = pytz.timezone('US/Pacific')

today = datetime.datetime.now(timezone)

today = today.strftime("%d-%b-%Y")

imap_server = "imap.mail.yahoo.com"
email_address = "quocanh.vien@yahoo.com"
password = "gnfimcldthrpqkin"


query = f"(SUBJECT \"Your Transport for NSW account verification code\" SINCE \"{today}\")"
query_sms = f"(SUBJECT \"Forward SMS From: Microsoft\" SINCE \"{today}\")"

status=""
code=""
get_sms=""
contents=[]
sms=[]


def check_email():
    try:
        global contents
        contents=[]
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(email_address, password)
        imap.select("Inbox")
        _, msgnums = imap.search(None, query)
        for msgnum in msgnums[0].split():
            _, data = imap.fetch(msgnum, "(RFC822)")
            message = email.message_from_bytes(data[0][1])
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    my_email = email.message_from_string(part.as_string())
                    content=my_email.get_payload(decode=True).decode(sys.stdout.encoding)
                    contents.append(content)
        imap.close()
        contents.reverse()
        return contents[0]

    except Exception as e:
        print(e)
        print("Something went wrong!")


def check_email_sms():
    try:
        global sms
        sms=[]
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(email_address, password)
        imap.select("Inbox")
        _, msgnums = imap.search(None, query_sms)
        for msgnum in msgnums[0].split():
            _, data = imap.fetch(msgnum, "(RFC822)")
            message = email.message_from_bytes(data[0][1])
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    my_email = email.message_from_string(part.as_string())
                    content=my_email.get_payload(decode=True).decode(sys.stdout.encoding)
                    sms.append(content)
        imap.close()
        sms.reverse()
        return sms[0]
    except Exception as e:
        print(e)
        print("Something went wrong!")



def get_email_code():
    try:
        global code
        code = check_email()
        if code is not None:
            sorted_code = code[171:190]
            return sorted_code
        else:
            return "Email has not been sent by RMS :("
    except Exception as e:
        return str(e)

def get_sms_code():
    try:
        global get_sms
        get_sms = check_email_sms()
        if get_sms is not None:
            sorted_sms = get_sms[38:45]
            return sorted_sms
        else:
            return "SMS has not been sent by RMS :("

    except Exception as e:
        return str(e)


