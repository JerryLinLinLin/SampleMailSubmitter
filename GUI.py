# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = wx.GetTranslation

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Sample Mail Submitter"), pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.Size( 500,600 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Choose File(s)") ), wx.VERTICAL )

		self.file_input = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, _(u"#Drag all file(s) here. One line per file."), wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.HSCROLL|wx.VSCROLL )
		sbSizer1.Add( self.file_input, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer1, 1, 0, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"EMail Account") ), wx.VERTICAL )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Email Adress: "), wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_LEFT )
		self.m_staticText2.Wrap( -1 )

		wSizer1.Add( self.m_staticText2, 0, wx.ALL, 8 )

		self.email_account = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 360,-1 ), 0 )
		wSizer1.Add( self.email_account, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Password: "), wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_LEFT )
		self.m_staticText3.Wrap( -1 )

		wSizer1.Add( self.m_staticText3, 0, wx.ALL, 8 )

		self.password_input = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), wx.TE_PASSWORD )
		wSizer1.Add( self.password_input, 0, wx.ALL, 5 )

		self.reme_ps_check = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Remember"), wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.reme_ps_check, 0, wx.ALL, 8 )

		self.m_staticText4 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"SMTP Adress: "), wx.DefaultPosition, wx.Size( 80,-1 ), wx.ALIGN_LEFT )
		self.m_staticText4.Wrap( -1 )

		wSizer1.Add( self.m_staticText4, 0, wx.ALL, 8 )

		self.smtp_input = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		wSizer1.Add( self.smtp_input, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Port: "), wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_LEFT )
		self.m_staticText5.Wrap( -1 )

		wSizer1.Add( self.m_staticText5, 0, wx.ALL, 8 )

		self.port_input = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 113,-1 ), 0 )
		wSizer1.Add( self.port_input, 0, wx.ALL, 5 )


		sbSizer2.Add( wSizer1, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Submission Type") ), wx.VERTICAL )

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.false_neg_select = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"False Negative"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.false_neg_select.SetValue( True )
		wSizer3.Add( self.false_neg_select, 0, wx.ALL, 5 )

		self.false_positive_select = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"False Positive"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer3.Add( self.false_positive_select, 0, wx.ALL, 5 )

		self.password_but = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"Zip Password"), wx.Point( -1,-1 ), wx.Size( 120,25 ), 0 )
		wSizer3.Add( self.password_but, 0, wx.ALL, 0 )

		self.email_content = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, _(u"Customize..."), wx.Point( -1,-1 ), wx.Size( 100,-1 ), 0 )
		self.email_content.SetMinSize( wx.Size( 120,25 ) )

		wSizer3.Add( self.email_content, 0, wx.ALL, 0 )


		sbSizer3.Add( wSizer3, 1, wx.EXPAND, 0 )


		bSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Vendors") ), wx.VERTICAL )

		wSizer4 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText6 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"Selected Vendors: "), wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )

		wSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"Vendor List: "), wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )

		wSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )

		selected_vendorsChoices = []
		self.selected_vendors = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 190,100 ), selected_vendorsChoices, 0|wx.VSCROLL )
		wSizer4.Add( self.selected_vendors, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.add_but = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"<<"), wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer5.Add( self.add_but, 0, wx.ALL, 5 )

		self.remove_but = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u">>"), wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer5.Add( self.remove_but, 0, wx.ALL, 5 )

		self.vendor_edit_but = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, _(u"..."), wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer5.Add( self.vendor_edit_but, 0, wx.ALL, 5 )


		wSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )

		vendor_listChoices = [ _(u"Avira;virus@avira.com"), _(u"Avira;novirus@avira.com"), _(u"Kaspersky;newvirus@kaspersky.com"), _(u"Kaspersky;apac-virussample@kaspersky.com"), _(u"ESET;samples@eset.sk"), _(u"ESET;samples@eset.com"), _(u"Huorong;seclab@huorong.cn"), _(u"BitDefender;oemsamples@bitdefender.com"), _(u"BitDefender;virus_submission@bitdefender.com") ]
		self.vendor_list = wx.ListBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,100 ), vendor_listChoices, 0|wx.VSCROLL )
		wSizer4.Add( self.vendor_list, 0, wx.ALL, 5 )


		sbSizer4.Add( wSizer4, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer4, 1, wx.EXPAND, 5 )

		wSizer5 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, _(u"Other Settings: ") ), wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, _(u"Program Language: "), wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )

		sbSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )

		language_choiceChoices = [ _(u"English"), _(u"Chinese Simplified") ]
		self.language_choice = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), language_choiceChoices, 0 )
		self.language_choice.SetSelection( 0 )
		sbSizer5.Add( self.language_choice, 0, wx.ALL, 5 )


		wSizer5.Add( sbSizer5, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.pack_but = wx.Button( self, wx.ID_ANY, _(u"Pack All to Desktop"), wx.DefaultPosition, wx.Size( 250,30 ), 0 )
		bSizer7.Add( self.pack_but, 0, wx.ALL, 3 )

		self.submit_but = wx.Button( self, wx.ID_ANY, _(u"Pack and Submit All"), wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer7.Add( self.submit_but, 0, wx.ALL, 3 )


		wSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer2.Add( wSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		bSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_but_click )
		self.reme_ps_check.Bind( wx.EVT_CHECKBOX, self.reme_ps_check_click )
		self.password_but.Bind( wx.EVT_BUTTON, self.password_but_click )
		self.email_content.Bind( wx.EVT_BUTTON, self.content_but_click )
		self.add_but.Bind( wx.EVT_BUTTON, self.add_but_click )
		self.remove_but.Bind( wx.EVT_BUTTON, self.remove_but_click )
		self.vendor_edit_but.Bind( wx.EVT_BUTTON, self.vendor_edit_but_click )
		self.language_choice.Bind( wx.EVT_CHOICE, self.lang_select )
		self.pack_but.Bind( wx.EVT_BUTTON, self.pack_but_click )
		self.submit_but.Bind( wx.EVT_BUTTON, self.submit_but_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close_but_click( self, event ):
		event.Skip()

	def reme_ps_check_click( self, event ):
		event.Skip()

	def password_but_click( self, event ):
		event.Skip()

	def content_but_click( self, event ):
		event.Skip()

	def add_but_click( self, event ):
		event.Skip()

	def remove_but_click( self, event ):
		event.Skip()

	def vendor_edit_but_click( self, event ):
		event.Skip()

	def lang_select( self, event ):
		event.Skip()

	def pack_but_click( self, event ):
		event.Skip()

	def submit_but_click( self, event ):
		event.Skip()


###########################################################################
## Class mail_content_frame
###########################################################################

class mail_content_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Custom Mail Content"), pos = wx.DefaultPosition, size = wx.Size( 500,270 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		wSizer6 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"False Negative Text"), wx.DefaultPosition, wx.Size( 250,20 ), 0 )
		self.m_staticText10.Wrap( -1 )

		wSizer6.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"False Positive Text"), wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.m_staticText11.Wrap( -1 )

		wSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer6, 1, wx.EXPAND, 5 )

		wSizer7 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.false_negative_content = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,150 ), wx.TE_MULTILINE|wx.VSCROLL )
		wSizer7.Add( self.false_negative_content, 0, wx.ALL, 5 )

		self.false_positive_content = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 230,150 ), wx.TE_MULTILINE|wx.VSCROLL )
		wSizer7.Add( self.false_positive_content, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer7, 1, wx.EXPAND, 5 )

		wSizer8 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.ok_but = wx.Button( self, wx.ID_ANY, _(u"OK"), wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer8.Add( self.ok_but, 0, wx.ALL, 5 )

		self.cancel_but = wx.Button( self, wx.ID_ANY, _(u"Cancel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer8.Add( self.cancel_but, 0, wx.ALL, 5 )


		bSizer4.Add( wSizer8, 1, wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.close_but_click )
		self.ok_but.Bind( wx.EVT_BUTTON, self.ok_but_click )
		self.cancel_but.Bind( wx.EVT_BUTTON, self.cancel_but_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close_but_click( self, event ):
		event.Skip()

	def ok_but_click( self, event ):
		event.Skip()

	def cancel_but_click( self, event ):
		event.Skip()


