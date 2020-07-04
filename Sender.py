import threading
import pyminizip
import os
import datetime
import smtplib
import ssl
import Main
import wx
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# for i18n support
_ = wx.GetTranslation


class SampleFiles:
    """
    Class represent sample Files for compressing
    """
    file_list: list = None  # All file paths
    password: str = None  # password for compressing
    output_path: str = None  # output path

    def __init__(self, file_list: str, password: str):
        """
        Initialize compressing
        :param file_list: file paths
        :param password: compress password
        """
        self.file_list = file_list.split('\n')
        self.password = password

    def compress(self):
        """
        Compress files to user dir
        :return: output path
        """
        cur_time = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S'))
        user_path = os.getenv('APPDATA') + "\\VirusSampleSubmitter"
        output_path = '{user_path}\\SamplePack[{time}].zip'.format(user_path=user_path, time=cur_time)
        self.output_path = output_path
        pyminizip.compress_multiple(self.file_list, [], output_path, self.password, 8)
        return output_path

    def delete_zip(self):
        """Delete self after compressing"""
        if self.output_path is not None:
            os.remove(self.output_path)

    def compress_to_desktop(self):
        """
        Compress files to user desktop
        :return: output path
        """
        cur_time = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S'))
        output_path = '{desktop_path}\\SamplePack[{time}].zip'.format(desktop_path=os.path.expanduser("~\\Desktop"),
                                                                      time=cur_time)
        self.output_path = output_path
        pyminizip.compress_multiple(self.file_list, [], output_path, self.password, 8)
        return output_path


class Mail:
    """
    Class represent email body
    """
    mail: MIMEMultipart = None  # mail body
    mail_dst_list: list = None  # vendor list

    def __init__(self, mail_src, mail_dst, mail_type, mail_content, attach_path):
        """
        Initialize mail obj
        :param mail_src: sender
        :param mail_dst: receivers
        :param mail_type: false negative or positive
        :param mail_content: content
        :param attach_path: sample pack path
        """
        mail = MIMEMultipart()
        mail['From'] = mail_src
        mail['To'] = ';'.join(self._extract_mails(mail_dst))
        mail['Subject'] = self._get_mail_title(mail_type)
        mail.attach(MIMEText(mail_content, 'plain', 'utf-8'))
        with open(attach_path, 'rb') as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header('Content-Disposition', 'attachment',
                                  filename=str(attach_path)[str(attach_path).rfind("\\") + 1:len(attach_path)])
            mail.attach(attachment)
        self.mail = mail
        self.mail_dst_list = self._extract_mails(mail_dst)
        return

    def _extract_mails(self, mails_string_array):
        """
        Extract email address from vendor list
        :param mails_string_array:
        :return:
        """
        result_list: list = []
        for mail_string in mails_string_array:
            address = mail_string[mail_string.find(";") + 1: len(mail_string)]
            result_list.append(address)
        return result_list

    def _get_mail_title(self, mail_type):
        """
        Get the title of mail based on type
        :param mail_type: fn or fp
        :return:
        """
        cur_time = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S'))
        if mail_type == 0:
            return '[Malware]{time}'.format(time=cur_time)
        else:
            return '[False Positive]{time}'.format(time=cur_time)

    def get_mail(self):
        return self.mail

    def get_mail_dst_list(self):
        return self.mail_dst_list


class SendingThread(threading.Thread):
    """
    Class for sending sample file
    """
    frame: Main.AppMainFrame = None  # main frame

    def __init__(self, frame):
        """
        Start thread
        :param frame: main frame
        """
        threading.Thread.__init__(self)
        self.frame = frame
        self.start()

    def run(self):
        """Sending sample"""
        status = self.frame.progress_bar

        if not self._basic_check():  # check if parameters are valid
            wx.MessageBox(message=_('Missing or incorrect parameters. Check if all info filled correctly.'),
                          caption=_('ERROR'),
                          style=wx.OK | wx.ICON_ERROR)
            status.Destroy()
            return

        # Compressing files
        status.Update(value=25,
                      newmsg=_('Compressing Files...'))
        sample = SampleFiles(self.frame.file_input.GetValue(), self.frame.zip_password)
        try:
            output_path = sample.compress()
        except Exception as e:
            wx.MessageBox(message=_('Cannot Access Sample File(s). Check paths.\n') +
                                  'Error: {error}\nInfo: {info}'.format(error=e.__class__.__name__, info=str(e)),
                          caption=_('ERROR'),
                          style=wx.OK | wx.ICON_ERROR)
            status.Destroy()
            return

        # Build email body
        status.Update(value=50,
                      newmsg=_('Composing Mail...'))
        mail = Mail(mail_src=self.frame.email_account.GetValue(),
                    mail_dst=self.frame.selected_vendors.GetStrings(),
                    mail_type=self._get_mail_type(),
                    mail_content=self._get_mail_content(),
                    attach_path=output_path)

        # Login to email account and send email
        status.Update(value=75,
                      newmsg=_('Login To Your Email...'))
        mail_body = mail.get_mail()
        mail_src = self.frame.email_account.GetValue()
        mail_password = self.frame.password_input.GetValue()
        mail_smtp = self.frame.smtp_input.GetValue()
        mail_port = self.frame.port_input.GetValue()

        try:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # use ssl
            mail_main = smtplib.SMTP(host=mail_smtp, port=mail_port)
            mail_main.ehlo()
            mail_main.starttls(context=context)
            mail_main.ehlo()
            mail_main.login(user=mail_src, password=mail_password)
            status.Update(value=90,
                          newmsg=_('Sending Email...'))
            mail_main.sendmail(from_addr=mail_src, to_addrs=mail.get_mail_dst_list(), msg=mail_body.as_string())
        except Exception as e:
            wx.MessageBox(message=_('Login Fail. Check Internet connection, your login info, or other config.\n') +
                                  'Error: {error}\nInfo: {info}'.format(error=e.__class__.__name__, info=str(e)),
                          caption=_('ERROR'),
                          style=wx.OK | wx.ICON_ERROR)
            status.Destroy()
            sample.delete_zip()
            return

        status.Update(value=100,
                      newmsg=_('SUCCEED!'))
        wx.MessageBox(message=_('Email Sent. You may login your email to check the status.'),
                      caption=_('INFO'),
                      style=wx.OK | wx.ICON_INFORMATION)
        status.Destroy()
        self.frame.file_input.SetValue(_(u"#Drag all file(s) here. One line per file."))
        sample.delete_zip()
        return

    def _get_mail_type(self):
        """Get mail type; 0 for fn, 1 for fp"""
        if self.frame.false_neg_select.GetValue():
            return 0
        if self.frame.false_positive_select.GetValue():
            return 1

    def _get_mail_content(self):
        """Get mail content based on type"""
        if self._get_mail_type() == 0:
            return self.frame.false_negative_content.format(password=self.frame.zip_password)
        if self._get_mail_type() == 1:
            return self.frame.false_positive_content.format(password=self.frame.zip_password)

    def _basic_check(self):
        """Check if parameters are valid"""
        f = self.frame
        if (f.email_account.GetValue() == '' or
                f.password_input.GetValue() == '' or
                f.smtp_input.GetValue() == '' or
                f.port_input.GetValue() == '' or
                f.zip_password == '' or
                f.selected_vendors.GetStrings() == []):
            return False
        return True
