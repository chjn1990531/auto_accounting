import sys
import imaplib
import getpass
import email
import datetime


def process_mailbox(M):
    rv, data = M.search(None, "ALL")

    # print(rv)
    # print(data)

    if rv != 'OK':
        print("No messages found!")
        return
    else:
        print('successfully loading')
        # for num in data[0].split():
        #     typ, data = M.fetch(num, '(RFC822)')
        #     print('Message %sn%sn' % (num, data[0][1]))



M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    M.login('jnchen123.123@gmail.com', 'Abcd1234!@#$') # getpass.getpass())# Abcd1234!@#$
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
    # ... exit or deal with failure...


# rv, mailboxes = M.list()
# if rv == 'OK':
#     print("Mailboxes:")
#     print(mailboxes)

rv, data = M.select("INBOX")
if rv == 'OK':
    print("Processing mailbox...\n")
    process_mailbox(M) # the operation with selected mailbox
    M.close()
M.logout()