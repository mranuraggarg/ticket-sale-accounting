#!/usr/bin/env python3
# vim: set fileencoding=utf-8
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2013-2020, Ticket Sale Accounting

## Credits: Anurag Garg

## License: GNU GPL v3.0
## Version: 0.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: alpha
####################################################################################################
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
import math
from datetime import datetime, timezone


class Default:
    def gtk_main_quit(self, window):
        Gtk.main_quit()

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("occupancy.glade")
        self.window = self.builder.get_object("window1")
        self.builder.connect_signals(self)

    def on_save_clicked(self, window, data=None):
        htmlname = datetime.now(timezone.utc).strftime("%d.%m.%Y.html")
        h = open(htmlname, 'w')

        date = self.builder.get_object("date_entry")
        label_date = date.get_text()

        h.write('<!DOCTYPE html>\n<html>\n\n')
        h.write('<head>\n<style>\ntable, th, td\n{\n')
        h.write('border-collapse:collapse;\nborder:1px solid black;\n}\n')
        h.write('{\ntext-align:center;\n}\n</style>\n</head>\n\n')

        h.write('<table>\n\t')
        h.write('<tr>\n\t\t')
        h.write('<th colspan="6" hight="4">\n\t\t\t')
        h.write('<h3>OCCUPANCY STATEMENT</h3>\n\t\t')
        h.write('</th>\n\t')
        h.write('</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<th colspan="6">\n\t\t\t')
        h.write('<h4>Nehru Planetarium</h4>\n\t\t')
        h.write('</th>\n\t')
        h.write('</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1"col width="150">\n\t\t\t')
        h.write('<b><center>Date</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1"> \n\t\t\t<center>')
        h.write(label_date)
        h.write('</center>\n\t\t</td>')
        h.write('\n\t</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('<b><center>Show Time</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="2" col width="240">\n\t\t\t')
        h.write('<b><center>Ticket No.</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Tkts Sold</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Rate</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Amount</b></center>\n\t\t')
        h.write('</td>\n')
        h.write('\t</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>From</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>To</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('<b><center>(per Head)</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t')
        h.write('</tr>')

        for i in [1, 2, 3, 4, 5, 6]:
            time_entry = 'time_' + str(i)
            time = self.builder.get_object(time_entry)
            label1 = time.get_text()

            j = 2 * i - 2
            entry_read = 'entry' + str(j)
            entry = self.builder.get_object(entry_read)
            label2 = entry.get_text()

            k = 2 * i - 1
            if not k == j:
                entry_read = 'entry' + str(k)
                entry = self.builder.get_object(entry_read)
                label3 = entry.get_text()

            tktsold_entry = 'tktsold_result' + str(i)
            tktsold = self.builder.get_object(tktsold_entry)
            label4 = tktsold.get_text()

            head_entry = 'head' + str(i)
            head = self.builder.get_object(head_entry)
            label5 = head.get_text()

            amount_entry = 'amount' + str(i)
            amount = self.builder.get_object(amount_entry)
            label6 = amount.get_text()

            h.write('\n\n\t<tr>\n\t\t')
            h.write('<td colspan="1">\n\t\t\t<center><b>')
            h.write(label1)
            h.write('</center></b>\n\t\t</td>\n\t\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label2)
            h.write('</center>\n\t\t</td>\n\t\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label3)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label4)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label5)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label6)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('</tr>')

        total = self.builder.get_object("total_result")
        label_total = total.get_text()

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="2" col width="240">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Total</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>')
        h.write(label_total)
        h.write('</b></center>\n\t\t')
        h.write('</td>\n')
        h.write('\t</tr>\n\n\t')

        h.write('\n\n</table>')

        h.write('<br><br><br><br><br><br>')

        h.write('<table>\n\t')
        h.write('<tr>\n\t\t')
        h.write('<th colspan="6" hight="4">\n\t\t\t')
        h.write('<h3>OCCUPANCY STATEMENT</h3>\n\t\t')
        h.write('</th>\n\t')
        h.write('</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<th colspan="6">\n\t\t\t')
        h.write('<h3>Nehru Planetarium</h3>\n\t\t')
        h.write('</th>\n\t')
        h.write('</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1"col width="150">\n\t\t\t')
        h.write('<b><center>Date</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1"> \n\t\t\t<center>')
        h.write(label_date)
        h.write('</center>\n\t\t</td>')
        h.write('\n\t</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('<b><center>Show Time</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="2" col width="240">\n\t\t\t')
        h.write('<b><center>Ticket No.</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Tkts Sold</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Rate</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Amount</b></center>\n\t\t')
        h.write('</td>\n')
        h.write('\t</tr>\n\n\t')

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>From</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>To</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('<b><center>(per Head)</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t')
        h.write('</tr>')

        for i in [1, 2, 3, 4, 5, 6]:
            time_entry = 'time_' + str(i)
            time = self.builder.get_object(time_entry)
            label1 = time.get_text()

            j = 2 * i - 2
            entry_read = 'entry' + str(j)
            entry = self.builder.get_object(entry_read)
            label2 = entry.get_text()

            k = 2 * i - 1
            if not k == j:
                entry_read = 'entry' + str(k)
                entry = self.builder.get_object(entry_read)
                label3 = entry.get_text()

            tktsold_entry = 'tktsold_result' + str(i)
            tktsold = self.builder.get_object(tktsold_entry)
            label4 = tktsold.get_text()

            head_entry = 'head' + str(i)
            head = self.builder.get_object(head_entry)
            label5 = head.get_text()

            amount_entry = 'amount' + str(i)
            amount = self.builder.get_object(amount_entry)
            label6 = amount.get_text()

            h.write('\n\n\t<tr>\n\t\t')
            h.write('<td colspan="1">\n\t\t\t<center><b>')
            h.write(label1)
            h.write('</center></b>\n\t\t</td>\n\t\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label2)
            h.write('</center>\n\t\t</td>\n\t\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label3)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label4)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label5)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('<td colspan="1">\n\t\t\t<center>')
            h.write(label6)
            h.write('</center>\n\t\t</td>\n\t')
            h.write('</tr>')

        total = self.builder.get_object("total_result")
        label_total = total.get_text()

        h.write('<tr>\n\t\t')
        h.write('<td colspan="1">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="2" col width="240">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>Total</b></center>\n\t\t')
        h.write('</td>\n\t\t')
        h.write('<td colspan="1" col width="120">\n\t\t\t')
        h.write('<b><center>')
        h.write(label_total)
        h.write('</b></center>\n\t\t')
        h.write('</td>\n')
        h.write('\t</tr>\n\n\t')

        h.write('\n\n</table>')

        h.close()

        import webbrowser as wb
        wb.open(htmlname)

    def on_dat_clicked(self, window, data=None):
        date = self.builder.get_object("date_entry")
        tdate = datetime.now(timezone.utc).strftime("%d/%m/%Y")
        date.set_text(tdate)

    def on_calc_clicked(self, window, data=None):
        global amount_result
		inname = [0 for i in range(13)]
        outname = [0 for i in range(13)]
        total_sum = 0.0

        for i in range(0, 12):
            inname[i] = 'entry' + str(i)
            entry = self.builder.get_object(inname[i])
            if not entry.get_text() == '':
                outname[i] = int(entry.get_text())

        result = 'amount' + str(i + 1)

        for j in [0, 2, 4, 6, 8, 10]:
            entry = self.builder.get_object(inname[j])
            if not entry.get_text() == '':

                val = outname[j + 1] - outname[j] + 1

                if j in [0, 4, 8]:
                    amount_result = float(val) * 50.0

                if j in [2, 6, 10]:
                    amount_result = float(val) * 30.0

                tkt_sold_result = 'tktsold_result' + str(j - int(j / 2) + 1)
                tktsold = self.builder.get_object(tkt_sold_result)
                tktsold.set_text(str(val))

                result = 'amount' + str(j - int(j / 2) + 1)
                amt = self.builder.get_object(result)
                amt.set_text(str(amount_result))

                total_sum = total_sum + amount_result

            total = self.builder.get_object("total_result")
            total.set_text(str(total_sum))


if __name__ == "__main__":
    win = Default()
    win.window.show_all()
    Gtk.main()
