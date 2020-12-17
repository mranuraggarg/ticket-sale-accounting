#!/usr/bin/env python3.4

from gi.repository import Gtk
import sqlite3 as sql

class MainWindow(Gtk.Window):

	def setupHeader( self ):
		hb = Gtk.HeaderBar()
		hb.props.show_close_button = True
		hb.props.title = "OCCUPANCY STATEMENT"
		self.set_titlebar( hb ) 
	
	def CreateTable( self ):
		self.table = Gtk.Table( 8, 12, False )
	
	def CreateLabel( self ):
		self.date_label = Gtk.Label()
		self.date_entry = Gtk.Entry()
		self.sno_label = Gtk.Label()
		self.tktno_label = Gtk.Label()
		self.from_label = Gtk.Label()
		self.to_label = Gtk.Label()
		self.tktsold_label = Gtk.Label()
		self.rate_label = Gtk.Label()
		self.rate1_label = Gtk.Label()
		self.rate2_label = Gtk.Label()
		self.rate3_label = Gtk.Label()
		self.rate4_label = Gtk.Label()
		self.rate5_label = Gtk.Label()
		self.rate6_label = Gtk.Label()
		self.amount_label = Gtk.Label()
		self.total_label = Gtk.Label()
		self.s1_label = Gtk.Label()
		self.s2_label = Gtk.Label()
		self.s3_label = Gtk.Label()
		self.s4_label = Gtk.Label()
		self.s5_label = Gtk.Label()
		self.s6_label = Gtk.Label()
		self.show1_label = Gtk.Label()
		self.show2_label = Gtk.Label()
		self.show3_label = Gtk.Label()
		self.show4_label = Gtk.Label()
		self.show5_label = Gtk.Label()
		self.show6_label = Gtk.Label()

	def SetLabel( self ):	
		self.date_label.set_markup( "<b>Date:</b>" )
		self.date_entry.set_text( "dd.mm.yyyy" )
		self.sno_label.set_markup( "<b>S. No.</b>" )
		self.tktno_label.set_markup( "<b>Ticket No.</b>" )
		self.from_label.set_markup( "<b>From</b>" )
		self.to_label.set_markup( "<b>To</b>" )
		self.tktsold_label.set_markup( "<b>Tkts\nSold</b>" )
		self.rate_label.set_markup( "<b>Rate\nPer Head</b>" )
		self.rate1_label.set_markup( "@50" )
		self.rate2_label.set_markup( "@30" )
		self.rate3_label.set_markup( "@50" )
		self.rate4_label.set_markup( "@30" )
		self.rate5_label.set_markup( "@50" )
		self.rate6_label.set_markup( "@30" )
		self.amount_label.set_markup( "<b>Amount</b>" )
		self.total_label.set_markup( "<b>Total</b>" )
		self.s1_label.set_markup( "1." )
		self.s2_label.set_markup( "2." )
		self.s3_label.set_markup( "3." )
		self.s4_label.set_markup( "4." )
		self.s5_label.set_markup( "5." )
		self.s6_label.set_markup( "6." )
		self.show1_label.set_markup( "11:30 AM Adult" )
		self.show2_label.set_markup( "11:30 AM Child" )
		self.show3_label.set_markup( "12:30 PM Adult" )
		self.show4_label.set_markup( "12:30 PM Child" )
		self.show5_label.set_markup( "05:00 PM Adult" )
		self.show6_label.set_markup( "05:00 PM child" )

	def CreateEntry( self ):		
		self.amnt3_entry = Gtk.Entry()
		self.amnt4_entry = Gtk.Entry()
		self.amnt5_entry = Gtk.Entry()
		self.amnt6_entry = Gtk.Entry()
		self.from1_entry = Gtk.Entry()
		self.from2_entry = Gtk.Entry()
		self.from3_entry = Gtk.Entry()
		self.from4_entry = Gtk.Entry()
		self.from5_entry = Gtk.Entry()
		self.from6_entry = Gtk.Entry()
		self.to1_entry = Gtk.Entry()
		self.to2_entry = Gtk.Entry()
		self.to3_entry = Gtk.Entry()
		self.to4_entry = Gtk.Entry()
		self.to5_entry = Gtk.Entry()
		self.to6_entry = Gtk.Entry()
		self.tktsold1_entry = Gtk.Entry()
		self.tktsold2_entry = Gtk.Entry()
		self.tktsold3_entry = Gtk.Entry()
		self.tktsold4_entry = Gtk.Entry()
		self.tktsold5_entry = Gtk.Entry()
		self.tktsold6_entry = Gtk.Entry()
		self.amnt1_entry = Gtk.Entry()
		self.amnt2_entry = Gtk.Entry()
		self.amnt3_entry = Gtk.Entry()
		self.amnt4_entry = Gtk.Entry()
		self.amnt5_entry = Gtk.Entry()
		self.amnt6_entry = Gtk.Entry()
		self.date_entry = Gtk.Entry()

	def CreateButton( self ):		
		self.calc = Gtk.Button( "Calculate" )
		self.save = Gtk.Button( "Save" )
	
	def SetPosition( self ):
		self.table.attach( self.date_label, 0, 1, 1, 2 )
		self.table.attach( self.date_entry, 1, 2, 1, 2 )
		self.table.attach( self.tktno_label, 2, 4, 2, 3 )
		self.table.attach( self.from_label, 2, 3, 3, 4)
		self.table.attach( self.to_label, 3, 4, 3, 4)
		self.table.attach( self.tktsold_label, 4, 5, 2, 4 )
		self.table.attach( self.rate_label, 5, 6, 2, 4 )
		self.table.attach( self.rate1_label, 5, 6, 4, 5 )
		self.table.attach( self.rate2_label, 5, 6, 5, 6 )
		self.table.attach( self.rate3_label, 5, 6, 6, 7 )
		self.table.attach( self.rate4_label, 5, 6, 7, 8 )
		self.table.attach( self.rate5_label, 5, 6, 8, 9 )
		self.table.attach( self.rate6_label, 5, 6, 9, 10 )
		self.table.attach( self.amount_label, 6, 7, 2, 3 )
		self.table.attach( self.sno_label, 0, 1, 2, 3)
		self.table.attach( self.s1_label, 0, 1, 4, 5)
		self.table.attach( self.s2_label, 0, 1, 5, 6)
		self.table.attach( self.s3_label, 0, 1, 6, 7)
		self.table.attach( self.s4_label, 0, 1, 7, 8)
		self.table.attach( self.s5_label, 0, 1, 8, 9)
		self.table.attach( self.s6_label, 0, 1, 9, 10)	
		self.table.attach( self.show1_label, 1, 2, 4, 5)
		self.table.attach( self.show2_label, 1, 2, 5, 6)
		self.table.attach( self.show3_label, 1, 2, 6, 7)
		self.table.attach( self.show4_label, 1, 2, 7, 8)
		self.table.attach( self.show5_label, 1, 2, 8, 9)
		self.table.attach( self.show6_label, 1, 2, 9, 10)	
		self.table.attach( self.from1_entry, 2, 3, 4, 5)
		self.table.attach( self.from2_entry, 2, 3, 5, 6)
		self.table.attach( self.from3_entry, 2, 3, 6, 7)
		self.table.attach( self.from4_entry, 2, 3, 7, 8)
		self.table.attach( self.from5_entry, 2, 3, 8, 9)
		self.table.attach( self.from6_entry, 2, 3, 9, 10)	
		self.table.attach( self.to1_entry, 3, 4, 4, 5)
		self.table.attach( self.to2_entry, 3, 4, 5, 6)
		self.table.attach( self.to3_entry, 3, 4, 6, 7)
		self.table.attach( self.to4_entry, 3, 4, 7, 8)
		self.table.attach( self.to5_entry, 3, 4, 8, 9)
		self.table.attach( self.to6_entry, 3, 4, 9, 10)	
		self.table.attach( self.calc, 5, 6, 10, 11 )
		self.table.attach( self.save, 6, 7, 10, 11 )

	def opendb( self ):
		from os.path import isfile, getsize
		
		if not isfile( 'occ' ):
			self.db = sql.connect('occ')
			self.cur = self.db.cursor()
			self.cur.execute('''
				CREATE TABLE data(date TEXT PRIMARY KEY, 
				show TEXT, tktfrom INTEGER, 
				tktto INTEGER, sold INTEGER, Ammount INTEGER, 
				Total INTEGER)
				''')
			self.db.commit()
		
			self.dialog = Gtk.MessageDialog(
            			self, 0, Gtk.MessageType.INFO, 
				Gtk.ButtonsType.OK, "Database Created")
			self.dialog.format_secondary_text( "datebase name: occ"
				"\ntable name: data" )
			self.dialog.run()
		
			self.dialog.destroy()

		else:
			fd = open( 'occ', 'rb' )
			Header = fd.read( 100 )
			fd.close()
			
			if Header[0:16] == 'SQLite format 3\000':
				self.conn = sql.connect('occ')
				self.dialog = Gtk.MessageDialog(
            			self, 0, Gtk.MessageType.INFO, 
					Gtk.ButtonsType.OK, "Database Connected")
				self.dialog.format_secondary_text( "datebase name: occ"
					"\ntable name: data" )
				self.dialog.run()
		
				self.dialog.destroy()
				return True
			
			else:
				print( "not working" )
				return False
		

	def on_save_clicked( self, button ):
		self.dialog = Gtk.MessageDialog(
            		self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
            		"Occupancy Statement Saved")
		self.date_entry = self.date_entry.get_text()
		self.filename = self.date_entry + '.html'
		self.dialog.format_secondary_text( "file name of the file: " + self.filename  )
		self.dialog.run()
		
		self.dialog.destroy()


	def on_calc_clicked( self, button):
		self.opendb()
		self.cur = self.db.cursor()
		date1 = self.date_entry.get_text()
		show1 = self.show1_label.get_text()
		print( date1, show1 )

	def __init__( self ):
		Gtk.Window.__init__( self, title="Occupancy Statement" )
		self.set_border_width( 10 )
		self.setupHeader()
		self.CreateTable()
		self.add( self.table )
		self.CreateLabel()
		self.CreateEntry()
		self.CreateButton()	
		self.SetLabel()
		
		self.calc.connect( "clicked", self.on_calc_clicked )
		self.save.connect( "clicked", self.on_save_clicked )
				
		self.SetPosition()	
		

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
