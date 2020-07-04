import GUI
import wx
import configparser
import os
import sys
import Sender
from distutils.util import strtobool
from base64 import urlsafe_b64encode, urlsafe_b64decode

# For i18n support
_ = wx.GetTranslation


class AppMainFrame(GUI.main_frame):
    """
    Class for handling main_frame GUI event
    """
    config: configparser.ConfigParser = None  # config obj
    lists = None  # vendor list
    zip_password: str = None  # password for compressing
    false_negative_content: str = None  # mail content for fn
    false_positive_content: str = None  # main content for fp
    progress_bar: wx.ProgressDialog = None  # sending progress dialog

    def __init__(self, parent, config, lists):
        """
        Initialize the main window
        :param parent: wxframe
        :param config: config file
        :param lists: vendor list
        """
        GUI.main_frame.__init__(self, parent)
        self.SetIcon(wx.Icon(app_path('mail.ico'), wx.BITMAP_TYPE_ICO))
        self.config = config
        self.lists = lists
        self._ini_setting()
        self._ini_lists()
        self._ini_file_drop()

    def password_but_click(self, event):
        """Config Zip password"""
        ps_input = wx.TextEntryDialog(self, _('Enter password for compressing'),
                                      caption=_('Set Zip Password'),
                                      value=self.zip_password,
                                      style=wx.OK | wx.CANCEL)
        while True:
            if ps_input.ShowModal() == wx.ID_OK:
                ps = ps_input.GetValue()
                if ps == '':
                    wx.MessageBox(message=_('Password Cannot be Empty'),
                                  caption=_('ERROR'),
                                  style=wx.OK | wx.ICON_ERROR)
                    continue
                self.zip_password = ps_input.GetValue()
                break
            break
        ps_input.Destroy()

    def reme_ps_check_click(self, event):
        """Save email password to local file"""
        if self.reme_ps_check.GetValue():
            result = wx.MessageBox(message=_('Password will be stored in the local config file. Continue?'),
                                   caption=_('WARNING'),
                                   style=wx.OK | wx.CANCEL | wx.ICON_WARNING)
            if result != wx.OK:
                self.reme_ps_check.SetValue(False)

    def add_but_click(self, event):
        """Add item to selected list from vendor list"""
        cur_index = self.vendor_list.GetSelection()
        if cur_index is wx.NOT_FOUND:
            return
        self.selected_vendors.Append(self.vendor_list.GetString(cur_index))
        self.vendor_list.Delete(cur_index)

    def remove_but_click(self, event):
        """Remove item from selected list and send back to vendor list"""
        cur_index = self.selected_vendors.GetSelection()
        if cur_index is wx.NOT_FOUND:
            return
        self.vendor_list.Append(self.selected_vendors.GetString(cur_index))
        self.selected_vendors.Delete(cur_index)

    def vendor_edit_but_click(self, event):
        """Edit vendor list"""
        vendor_input = wx.TextEntryDialog(self, _('Use ";" to separate name and email.'),
                                          caption=_('Edit Vendor List'),
                                          value=str(self.selected_vendors.GetStrings() + self.vendor_list.GetStrings()),
                                          style=wx.OK | wx.CANCEL | wx.TE_MULTILINE)
        while True:
            if vendor_input.ShowModal() == wx.ID_OK:
                try:
                    self.vendor_list.Set(eval(vendor_input.GetValue()))  # transfer str to dict
                    self.selected_vendors.Clear()  # reset vendor list
                    break
                except:
                    wx.MessageBox(message=_('Incorrect Data Format'),
                                  caption=_('ERROR'),
                                  style=wx.OK | wx.ICON_ERROR)
                    continue
            else:
                break
        vendor_input.Destroy()

    def content_but_click(self, event):
        """Build mail content frame"""
        AppEmailContentFrame(parent=self).Show(True)
        return

    def submit_but_click(self, event):
        """Submit sample"""
        self.progress_bar = wx.ProgressDialog(title=_('Sending Samples...'),
                                              message='N/A',
                                              maximum=100,
                                              parent=self,
                                              style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE)
        Sender.SendingThread(self)  # initialize sending thread

    def pack_but_click(self, event):
        """Pack samples to desktop path"""
        pack = Sender.SampleFiles(self.file_input.GetValue(), self.zip_password)  # compressing samples
        try:
            pack.compress_to_desktop()
        except Exception as e:
            wx.MessageBox(message=_('Cannot Access Sample File(s). Check paths.\n') +
                                  'Error: {error}\nInfo: {info}'.format(error=e.__class__.__name__, info=str(e)),
                          caption=_('ERROR'),
                          style=wx.OK | wx.ICON_ERROR)
            pack.delete_zip()
            return

        wx.MessageBox(message=_('Pack to Desktop succeed!'),
                      caption=_('INFO'),
                      style=wx.OK | wx.ICON_INFORMATION)

    def close_but_click(self, event):
        """Operation before main_frame close"""
        self._save_setting()
        self._save_list()
        self.Destroy()

    def lang_select(self, event):
        """Select language and restart App"""
        self._save_setting()
        self._save_list()
        os.startfile(sys.argv[0])  # restart
        self.Destroy()

    def _ini_file_drop(self):
        """Set file drop target"""
        drop_target = FileDropTarget(self)
        self.file_input.SetDropTarget(drop_target)

    def _ini_lists(self):
        """Initialize vendor list"""
        if self.lists is not None:
            self.vendor_list.Set(self.lists['vendor_list'])
            self.selected_vendors.Set(self.lists['selected_list'])

    def _ini_setting(self):
        """parse all settings to GUI """
        cf = self.config
        sec_str = 'main_frame_string'
        sec_bool = 'main_frame_boolean'
        sec_int = 'main_frame_int'
        sec_txt = 'main_frame_txt'
        # iterate to apply all settings
        if cf.has_section(sec_str):
            for key in cf[sec_str]:
                getattr(self, key).SetValue(cf[sec_str][key])
            for key in cf[sec_bool]:
                getattr(self, key).SetValue(bool(strtobool(cf[sec_bool][key])))
            for key in cf[sec_int]:
                getattr(self, key).SetSelection(int(cf[sec_int][key]))
            for key in cf[sec_txt]:
                setattr(self, key, cf[sec_txt][key])
            data = self.password_input.GetValue()
            # decode email password
            self.password_input.SetValue(urlsafe_b64decode(data[2:len(data) - 1]).decode('utf-8'))
        else:
            # Ini setting if no previous setting found
            cf.add_section(sec_str)
            cf.add_section(sec_bool)
            cf.add_section(sec_int)
            cf.add_section(sec_txt)
            self.zip_password = 'infected'
            self.false_negative_content = _("Hello,\n\nThe attached files may contain threats. Require for the further "
                                            "analysis.\n\nPassword: {password} \n\nThanks! ")
            self.false_positive_content = _("Hello,\n\nThe attached files may be clean. Require for the further "
                                            "analysis.\n\nPassword: {password} \n\nThanks! ")

    def _save_list(self):
        """Save vendor list"""
        self.lists = {
            'vendor_list': self.vendor_list.GetStrings(),
            'selected_list': self.selected_vendors.GetStrings()
        }

    def _save_setting(self):
        """Save GUI settings to config obj"""
        cf = self.config
        sec = 'main_frame_string'
        cf.set(sec, 'email_account', self.email_account.GetValue())
        # convert password to base64 for basic obfuscation
        cf.set(sec, 'password_input', str(urlsafe_b64encode(bytes(self.password_input.GetValue(), 'utf-8'))))
        cf.set(sec, 'smtp_input', self.smtp_input.GetValue())
        cf.set(sec, 'port_input', self.port_input.GetValue())
        if self.reme_ps_check.GetValue() is False:
            cf.set(sec, 'password_input', '')

        sec = 'main_frame_boolean'
        cf.set(sec, 'reme_ps_check', str(self.reme_ps_check.GetValue()))
        cf.set(sec, 'false_neg_select', str(self.false_neg_select.GetValue()))
        cf.set(sec, 'false_positive_select', str(self.false_positive_select.GetValue()))

        sec = 'main_frame_int'
        cf.set(sec, 'language_choice', str(self.language_choice.GetCurrentSelection()))

        sec = 'main_frame_txt'
        cf.set(sec, 'zip_password', str(self.zip_password))
        cf.set(sec, 'false_negative_content', str(self.false_negative_content))
        cf.set(sec, 'false_positive_content', str(self.false_positive_content))


class AppEmailContentFrame(GUI.mail_content_frame):
    """
    Class for handing mail_content_frame event
    """
    parent_f: AppMainFrame = None  # parent frame

    def __init__(self, parent):
        """
        Initialize frame window
        :param parent: wxframe
        """
        GUI.mail_content_frame.__init__(self, parent)
        self.parent_f = parent
        self.parent_f.Disable()
        self.false_negative_content.SetValue(self.parent_f.false_negative_content)
        self.false_positive_content.SetValue(self.parent_f.false_positive_content)

    def return_to_parent(self):
        """Operation before closing this frame"""
        self.parent_f.Enable()
        self.parent_f.SetFocus()
        self.Destroy()

    def ok_but_click(self, event):
        self.parent_f.false_negative_content = self.false_negative_content.GetValue()
        self.parent_f.false_positive_content = self.false_positive_content.GetValue()
        self.return_to_parent()

    def cancel_but_click(self, event):
        self.return_to_parent()

    def close_but_click(self, event):
        self.return_to_parent()


class FileDropTarget(wx.FileDropTarget):
    """
    Config drop target obj
    """
    frame_p: AppMainFrame = None  # frame parameter

    def __init__(self, frame_p):
        wx.FileDropTarget.__init__(self)
        self.frame_p = frame_p

    def OnDropFiles(self, x, y, data: list):
        previous_txt = self.frame_p.file_input.GetValue()
        # Check if input textCtrl is empty or start with '#' (Default)
        if previous_txt == '' or previous_txt[0] == "#":
            previous_txt = ''
            self.frame_p.file_input.SetValue(previous_txt)
        else:
            previous_txt = previous_txt + '\n'
        self.frame_p.file_input.SetValue(previous_txt + '\n'.join(data))
        return True


def app_path(path):
    """
    Static method to get the abs path special for pyinstaller packing
    :param path: relative path
    :return: abs path
    """
    if getattr(sys, 'frozen', False):
        app_dir = sys._MEIPASS
    else:
        app_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(app_dir, path)


class BaseApp(wx.App):
    """
    Class for config wxApp; Loading config and language file
    """
    config_path = os.getenv('APPDATA') + "\\VirusSampleSubmitter"  # config file path
    config = configparser.ConfigParser()  # config obj
    lists = None  # vendor list

    def OnInit(self):
        """Load config and list file"""
        if os.path.exists(self.config_path) is False:
            os.mkdir(self.config_path)
        self.config.read(self.config_path + "\\config.ini")
        self._ini_language()
        if os.path.exists(self.config_path + "\\list.db") is False:
            return True
        with open(self.config_path + "\\list.db") as f:
            self.lists = eval(f.read())
            f.close()
        return True

    def OnExit(self):
        """Save config and list file"""
        self.lists = frame.lists
        with open(self.config_path + "\\config.ini", 'w') as config_w:
            self.config.write(config_w)
            config_w.close()
        with open(self.config_path + "\\list.db", "w") as f:
            f.write(str(self.lists))
            f.close()
        return True

    def _ini_language(self):
        """Initialize program language"""
        self.locale = None
        if not self.config.has_section('main_frame_int'):
            return
        lang = int(self.config['main_frame_int']['language_choice'])
        if lang == 1:  # Change to zh-cn
            self.locale = wx.Locale(wx.LANGUAGE_CHINESE_SIMPLIFIED)
            if self.locale.IsOk():
                self.locale.AddCatalogLookupPathPrefix(app_path('locale'))
                self.locale.AddCatalog('lang_zh_CN')
            else:
                self.locale = None


if __name__ == '__main__':
    app = BaseApp(redirect=False)
    frame = AppMainFrame(None, app.config, app.lists)
    frame.Show(True)
    app.MainLoop()
