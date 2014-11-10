# encoding: utf-8
"""Send email through Gmail using SMTP."""

from __future__ import absolute_import
from __future__ import print_function

import smtplib
import mimetypes
import email
import email.mime.application

def _to_list(o):
    if o is None:
        return []
    if isinstance(o, (str, unicode)):
        return [o]
    if isinstance(o, (list, tuple)):
        return o
    raise TypeError('Must be a string or list of strings: %r' % o)

def send_gmail(username=None, password=None, subject='', body='', to=None,
               bcc=None, cc=None, attachments=None,
               debug=False):
    """Send an email using Gmail and SMTP.
    
    Parameters
    ----------
    username : str
        The Gmail username of the sender, which include @gmail.com.
    password : str
        The Gmail password of the sender.
    subject : str
        The subject of the email.
    body : str
        The body of the email.
    to : str or list of str
        The email or emails to send the email to.
    bcc : str or list of str
        The email or emails to send the email to as a blind cc.
    cc : str or list of str
        The email or emails to send the email to as a cc.
    attachments : str or list of str
        The paths of the local files to attach to the email.
    debug : bool
        Print debugging information
    """

    to = _to_list(to)
    cc = _to_list(cc)
    bcc = _to_list(bcc)
    attachments = _to_list(attachments)
    msg = email.mime.Multipart.MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = username
    if to:
        msg['To'] = ', '.join(to)
    if cc:
        msg['CC'] = ', '.join(cc)
    
    body = email.mime.Text.MIMEText(body)
    msg.attach(body)

    for filename in attachments:
        with open(filename, 'rb') as f:
            att = email.mime.application.MIMEApplication(f.read())
        att.add_header('Content-Disposition','attachment',filename=filename)
        msg.attach(att)
    
    if debug:
        print(msg.as_string())
    else:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to+cc+bcc, msg.as_string())
        server.quit()