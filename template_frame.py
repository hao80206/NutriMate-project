# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,530 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"NutriMate"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        self.m_staticText1.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_LIGHT, False, "Bookman Old Style" ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Search for food"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Bookman Old Style" ) )

        bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Keywords :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, _(u" "), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Nutrients Range Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Nutrients :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Min :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_textCtrl3, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 0, 0, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, _(u"Max :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer6.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_textCtrl4, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )


        bSizer7.Add( bSizer4, 0, 0, 5 )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        m_radioBox1Choices = [ _(u"Low"), _(u"Mid"), _(u"High") ]
        self.m_radioBox1 = wx.RadioBox( self.m_panel1, wx.ID_ANY, _(u"Nutrients Range Level"), wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
        self.m_radioBox1.SetSelection( 0 )
        bSizer9.Add( self.m_radioBox1, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )


        bSizer2.Add( bSizer7, 0, wx.EXPAND, 5 )

        self.m_grid1 = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer2.Add( self.m_grid1, 0, wx.ALL, 5 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        self.m_notebook1.AddPage( self.m_panel1, _(u"Food Search"), True )
        self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Food Name :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer11.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Caloric Value  :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer11.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Fat :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        bSizer11.Add( self.m_staticText14, 0, wx.ALL, 5 )

        self.m_staticText15 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Protein :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        bSizer11.Add( self.m_staticText15, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Carbohydrate :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer11.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Sugars :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer11.Add( self.m_staticText17, 0, wx.ALL, 5 )

        self.m_staticText18 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Calories per serving :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer11.Add( self.m_staticText18, 0, wx.ALL, 5 )


        bSizer10.Add( bSizer11, 1, 0, 5 )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText19 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Nutrition Breakdown:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        bSizer12.Add( self.m_staticText19, 0, wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12.Add( self.m_panel4, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText20 = wx.StaticText( self.m_panel2, wx.ID_ANY, _(u"Bar Chart :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer12.Add( self.m_staticText20, 0, wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12.Add( self.m_panel5, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer10.Add( bSizer12, 0, 0, 5 )


        self.m_panel2.SetSizer( bSizer10 )
        self.m_panel2.Layout()
        bSizer10.Fit( self.m_panel2 )
        self.m_notebook1.AddPage( self.m_panel2, _(u"Nutrition Info Display"), False )
        self.m_panel3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText21 = wx.StaticText( self.m_panel3, wx.ID_ANY, _(u"Food Calculator :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        self.m_staticText21.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer15.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText22 = wx.StaticText( self.m_panel3, wx.ID_ANY, _(u"Food Product:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer15.Add( self.m_staticText22, 0, wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

        self.m_staticText23 = wx.StaticText( self.m_panel3, wx.ID_ANY, _(u"Weight (in grams) :"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer15.Add( self.m_staticText23, 0, wx.ALL, 5 )

        self.m_textCtrl6 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self.m_panel3, wx.ID_ANY, _(u"Calculate"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_button2, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer15 )
        self.m_panel3.Layout()
        bSizer15.Fit( self.m_panel3 )
        self.m_notebook1.AddPage( self.m_panel3, _(u"Food Calculator"), False )

        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnSearch )
        self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.RangeLevel )
        self.m_button2.Bind( wx.EVT_BUTTON, self.Calculate )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnSearch( self, event ):
        event.Skip()

    def RangeLevel( self, event ):
        event.Skip()

    def Calculate( self, event ):
        event.Skip()


