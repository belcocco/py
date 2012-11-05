#!/usr/bin/python
# -*- coding: latin-1 -*-

# pygtk_studio.py
# Copyright (C) 2012 raga <raga.muffin@virgilio.it>
# 
# pygtk-studio is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pygtk-studio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#import module
import gtk
import os, sys, ftplib
import gobject
import time

class MainWin(gtk.Window):
    def __init__(self):
        super(MainWin, self).__init__()
        
        self.set_title("Main")
        self.set_size_request(100, 260)		#dimensione della finestra per 4 button (100,180)
#        self.set_size_request(1000, 480)
#        self.set_position(gtk.WIN_POS_CENTER)
#        self.connect("destroy", self.on_destroy)

#######################################

        fixed = gtk.Fixed()

        git = gtk.Button("Git")
        git.connect("clicked", self.on_clicked_git)
        git.set_size_request(80, 40)
        fixed.put(git, 10, 10)

        ftp = gtk.Button("FTP")
        ftp.connect("clicked", self.on_clicked_ftp)
        ftp.set_size_request(80, 40)
        fixed.put(ftp, 10, 50)

        hack = gtk.Button("Hack")
        hack.connect("clicked", self.on_clicked_hack)
        hack.set_size_request(80, 40)
        fixed.put(hack, 10, 90)

        lista = gtk.Button("List")
        lista.connect("clicked", self.on_clicked_lista)
        lista.set_size_request(80, 40)
        fixed.put(lista, 10, 130)
        
        lista = gtk.Button("Editor")
        lista.connect("clicked", self.on_clicked_editor)
        lista.set_size_request(80, 40)
        fixed.put(lista, 10, 170)

        comando = gtk.Button("Comando")
        comando.connect("clicked", self.on_clicked_comando)
        comando.set_size_request(80, 40)
        fixed.put(comando, 10, 210)

        self.add(fixed)

#        self.show_all()
        
#    def on_destroy(self, widget):
#        gtk.main_quit()
        
    def on_clicked_git(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
        app = GUI_git()						#si apre la finestra dell'applicazione
#       app.show_all()
#       gtk.main_quit()

    def on_clicked_ftp(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del ftp-button
        app = GUI_ftp()						#si apre la finestra dell'applicazione
        app.show_all()
#       gtk.main_quit()

    def on_clicked_hack(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del hack-button
        app = GUI_hack()						#si apre la finestra dell'applicazione
#       gtk.main_quit()
#Da questo punto importa applicazioni fatte da altri
    def on_clicked_lista(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		import lista
#		app = ListaWin()
#		gtk.main_quit()

    def on_clicked_editor(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		import editor

#		gtk.main_quit()

    def on_clicked_comando(self, widget):
		#INSERIRE la procedura di apertura della finestra GUI() al click del git-button
		import eseguicmd

#		gtk.main_quit()


#######################################
UI_FILE_GIT = "src/pygtk_studio_git.ui"
UI_FILE_FTP = "src/pygtk_studio_ftp.ui"
UI_FILE_HACK = "src/pygtk_studio_hack.ui"

class Presentazione(gtk.Window):
    def __init__(self):
        super(Presentazione, self).__init__()
        
#        self.connect("destroy", gtk.main_quit)
        self.set_default_size(472,365)
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)

        # the scrolledwindow
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        # there is always the scrollbar (otherwise: AUTOMATIC - only if needed - or NEVER)
#        scrolled_window.set_policy(gtk.PolicyType.ALWAYS, gtk.PolicyType.ALWAYS)

        # an image - slightly larger than the window...
        image = gtk.Image()
        image.set_from_file("/home/raga/py/Raga-auto421x316.png")

        # add the image to the scrolledwindow
        scrolled_window.add_with_viewport(image)

        # add the scrolledwindow to the window
        self.add(scrolled_window)

    def on_destroy(self, widget):
        gtk.main_quit()
		
#Window per GitHub.com (Upload e Download Repository)
class GUI_git():
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Git")
		self.win.set_default_size(200,80)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)

#		self.vbox = gtk.VBox()

		self.vbox = gtk.VBox(gtk.TRUE, 3)
		self.win.add(self.vbox)
		self.vbox.show()

#2 ToggleButton per le attività CLONE e PUSH
		self.tog_button_clone = gtk.ToggleButton("CLONE")
		self.tog_button_clone.connect("clicked", self.tog_clone, "Download")
		self.tog_button_push = gtk.ToggleButton("PUSH")
		self.tog_button_push.connect("clicked", self.tog_push, "Upload")

		self.vbox.pack_start(self.tog_button_clone, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.tog_button_push, gtk.TRUE, gtk.TRUE, 5)

#Spazio per inserire il comando (git clone .... oppure git push.....
		self.entry = gtk.Entry(100)
#		self.entry.set_text("git clone http://github.com/belcocco/py.git")
		self.vbox.pack_start(self.entry, gtk.TRUE, gtk.TRUE, 0)

#Bottone Esegui
		self.button_exec = gtk.Button(None, gtk.STOCK_EXECUTE)
		self.button_exec.connect("clicked", self.changeText)
		self.vbox.pack_start(self.button_exec, gtk.TRUE, gtk.TRUE, 0)

		self.win.show_all()

	def changeText(self, widget):
		self.entry.set_text("Nuovo testo!")
	def tog_clone(self, widget, data=None):
		self.entry.set_text("git clone http://github.com/belcocco/py.git")
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
	def tog_push(self, widget, data=None):
		self.entry.set_text("git push http://github.com/belcocco/py.git")
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()
#	def main(self):
#		gtk.main()

class GUI_ftp():
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("FTP")
		self.win.set_default_size(400,95)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)

######### FTP Client ############################
#		if __name__ == '__main__':
#		nick = raw_input('Nick:')
#		pwd = raw_input('Password:')
#		site = raw_input('Sito:')
#		obj = ClientFTP(site,nick,pwd)
#		while obj.online: #while True
#			command = raw_input('pyFTP >>> ')
#			obj.controlla_cmd(command)      
#################################################

        
#        self.connect("destroy", gtk.main_quit)
#        self.win.set_default_size(800,95)
#        self.set_size_request(250, 150)
#        self.win.set_position(gtk.WIN_POS_CENTER)
#        fixed = gtk.Fixed()
#        git = gtk.Button("Download")
#        fixed.put(git, 10, 10)

#        blog = gtk.Button("Upload")
#        fixed.put(blog, 10, 50)

#        self.add(fixed)
 
class GUI_hack:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Hack")
		self.win.set_default_size(400,95)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)

#		self.vbox = gtk.VBox()

		self.vbox = gtk.VBox(gtk.TRUE, 3)
		self.win.add(self.vbox)
		self.vbox.show()

#		self.entry = gtk.Entry(100)
#		self.entry.set_text("git clone http://github.com/belcocco/py.git")
#		self.vbox.pack_start(self.entry, gtk.TRUE, gtk.TRUE, 0)
#		self.button = gtk.Button(None, gtk.STOCK_EXECUTE)
#		self.button.connect("clicked", self.changeText)
#		self.vbox.pack_start(self.button, gtk.TRUE, gtk.TRUE, 0)
#		self.win.add(self.vbox)
#		self.win.show_all()


		self.button_r1 = gtk.RadioButton(None, "primo", gtk.FALSE)
		self.button_r1.connect("toggled", self.tog, "primo")
		self.button_r2 = gtk.RadioButton(self.button_r1, "secondo")
		self.button_r2.connect("toggled", self.tog, "secondo")
		self.button_r3 = gtk.RadioButton(self.button_r1, "terzo")
		self.button_r3.connect("toggled", self.tog, "terzo")

		self.button_t1 = gtk.ToggleButton("primo toggle")
		self.button_t1.connect("toggled", self.tog, "primo toggle")
		self.button_t2 = gtk.ToggleButton("secondo toggle")
		self.button_t2.connect("toggled", self.tog, "secondo toggle")
		self.button_dl = gtk.Button("Download")
		self.button_dl.connect("clicked", self.tog, "Download")
		self.button_ul = gtk.Button("Upload")
		self.button_ul.connect("clicked", self.tog, "Upload")

		self.buttonQuit = gtk.Button(None, gtk.STOCK_QUIT)
		self.buttonQuit.connect("clicked", self.destroy)

		self.vbox.pack_start(self.button_r1, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_r2, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_r3, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_t1, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_t2, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_dl, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.button_ul, gtk.TRUE, gtk.TRUE, 5)
		self.vbox.pack_start(self.buttonQuit, gtk.TRUE, gtk.TRUE, 5)
		
		self.win.show_all()
	def changeText(self, widget):
		self.entry.set_text("Nuovo testo!")
	def tog(self, widget, data=None):
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return #gtk.main_quit()
#	def main(self):
#		gtk.main()

#Window per clonare in locale un repo su GitHub.com (Download Repository)
class GIT_clone_push:
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Git")
		self.win.set_default_size(400,95)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.set_resizable(gtk.TRUE)
		self.win.set_border_width(10)

		self.win.connect("delete_event", self.delete_event)
		self.win.connect("destroy", self.destroy)

		self.vbox = gtk.VBox()

#		self.vbox = gtk.VBox(gtk.TRUE, 3)
#		self.win.add(self.vbox)
#		self.vbox.show()

		self.entry = gtk.Entry(100)
		self.entry.set_text("git clone http://github.com/belcocco/py.git")
		self.vbox.pack_start(self.entry, gtk.TRUE, gtk.TRUE, 0)
		self.button = gtk.Button(None, gtk.STOCK_EXECUTE)
		self.button.connect("clicked", self.changeText)
		self.vbox.pack_start(self.button, gtk.TRUE, gtk.TRUE, 0)
		self.win.add(self.vbox)
		self.win.show_all()


#		self.button_r1 = gtk.RadioButton(None, "primo", gtk.FALSE)
#		self.button_r1.connect("toggled", self.tog, "primo")
#		self.button_r2 = gtk.RadioButton(self.button_r1, "secondo")
#		self.button_r2.connect("toggled", self.tog, "secondo")
#		self.button_r3 = gtk.RadioButton(self.button_r1, "terzo")
#		self.button_r3.connect("toggled", self.tog, "terzo")

#		self.button_t1 = gtk.ToggleButton("primo toggle")
#		self.button_t1.connect("toggled", self.tog, "primo toggle")
#		self.button_t2 = gtk.ToggleButton("secondo toggle")
#		self.button_t2.connect("toggled", self.tog, "secondo toggle")
#		self.button_dl = gtk.Button("Download")
#		self.button_dl.connect("clicked", self.tog, "Download")
#		self.button_ul = gtk.Button("Upload")
#		self.button_ul.connect("clicked", self.tog, "Upload")

#		self.buttonQuit = gtk.Button(None, gtk.STOCK_QUIT)
#		self.buttonQuit.connect("clicked", self.destroy)

#		self.vbox.pack_start(self.button_r1, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.button_r2, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.button_r3, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.button_t1, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.button_t2, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.button_dl, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.button_ul, gtk.TRUE, gtk.TRUE, 5)
#		self.vbox.pack_start(self.buttonQuit, gtk.TRUE, gtk.TRUE, 5)
		
#		self.win.show_all()
	def changeText(self, widget):
		self.entry.set_text("Nuovo testo!")
	def tog(self, widget, data=None):
		print "%s e' ora %s" % (data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self, widget, event, data=None):
		return gtk.FALSE
	def destroy(self, widget, data=None):
		return gtk.main_quit()
#	def main(self):
#		gtk.main()

class ClientFTP(object):
        """Client FTP da linea di comando
           Funzioni:               Comandi associati         Parametri: 
              -Connessione              None                      site,nick,password
              -Disconnessione           None                      None
              -Lista File               LIST                      None
              -Ricerca File             SEARCH                    nome_file
              -Rinomina File            REN                       nome_file, directory, nuovoNome
              -Elimina File             DEL                       nome_file, directory
              -Download file            DW                        directory, filename, directory_di_uscita
              -Download all file        DWA                       directory_remota, filename, directory_uscita
              -Invio file               UPL                       nomeFile, directory_uscita 
              -Cambio directory         CD                        place,  nome
              -Informazione sulla
               directory locale/remota   LD->Local Directory      None
                                         RD->Remote Directory
              """
        def __init__(self,site ,nick, pwd):
                self.online = None
                self.comandi = ['RD', 'LD', 'CD', 'DW','DWA','LIST','SEARCH','REN','DEL','UPL','QUIT','HELP','INFO']
                self.site = site
                self.nick = nick
                self.pwd = pwd
                self.user = self.connection(self.site,self.nick,self.pwd)

        def connection(self,site,nick,pwd):
                """Comando: None    Parametri: Site, nick, password
                   Compito: Si connette al server alla porta:21 in modalità passiva"""
                try:
                        user = ftplib.FTP(site,nick,pwd)
                        self.online = True
                        print user.getwelcome()
                        return user 
                except ftplib.all_errors,error:
                        print '[FATAL]Connessione fallita!\n %s' %(error)
                        self.online = False
                        return None  #self.user = None
                        
        
        def disconnect(self):
                """Si disconnette dal server e termina il programma"""
                self.user.quit()
                self.online = False
                sys.exit('Programma terminato')

        def local_directory(self):
                """Comando: LD    Parametri: None
                   Computo: restiruisce informazioni sulla directory locale corrente"""
                print 'Direcory locale corrente: %s' %(os.getcwd())
        
        def remote_directory(self):
                """Comando: RD   Parametri: None
                   Compito: Restituisce informazioni sulla directory remota corrente"""
                print 'Directory remota corrente: %s' %(self.user.pwd())
        
        def change_directory(self,place,path):
                """Comando CD Parametri: place (Valori possibili: R,L.R = remoto,L = locale. path(Nome della nuova directory)
                   Compito: Cambio directory """
                if place.upper() == 'R':
                        try:
                                self.user.cwd(path)
                                print 'Directory remota cambiata in : %s' %(self.user.pwd())
                                return True
                        except ftplib.all_errors ,e:
                                print '[!!]%s' %(e) 
                elif place.upper() == 'L':
                        try:
                                os.chdir(path)
                                print 'Directory locale cambiata in: %s' %(os.getcwd())
                                return True
                        except os.error,e:
                                print '[!!]%s' %(e) 
                else:
                        print 'Error, place non supportato!\nPlace supportati: R,L\nR = remote\nL = local'
                        return False

        def search_file(self,filename,directory):
                """Comando: Search        Parametri: filename, directory
                   Compito: Cerca un file"""
                try:
                        self.change_directory('R',directory)
                        list_file = self.user.mlsd(facts=['type','size'])
                        _file=[x for x in list_file if filename in x]
                        if _file == []:
                                print '[!!]File %s non trovato!' %(filename)
                                return False
                        else:
                                print _file
                                return True
                except ftplib.error_temp,e:
                        print '[ERROR]%s'%(e)
                        print 'Connessione...'
                        self.user.connect(self.site)
                        self.user.login(self.nick,self.pwd)
                        
                        
        
        def download(self,directory,filename,directory_uscita = os.getcwd(),from_all_file = False):
                """Comando: DW  Parametri: Directory(Directory  remota del file), filename(nome del file remoto), directory_uscita(Directory locale dove verrà salvato il file.
                                                                                                                    il valore predefinito è la directory corrente)
                   Compito: Scarica un file dal server"""
                try:
                        if from_all_file:
                                file_remoto = open(filename,'wb')
                                self.user.retrbinary('RETR %s' %(str(filename)),file_remoto.write)
                                file_remoto.close()
                                print 'Scaricato in %s' %(os.getcwd())
                        else:
                                if self.search_file(filename,directory):
                                        file_remoto = open(filename,'wb')
                                        self.user.retrbinary('RETR %s' %(str(filename)),file_remoto.write)
                                        file_remoto.close()
                                        print 'Scaricato in %s' %(os.getcwd())
                                else:
                                        print '[!!]File %s non trovato!' %(filename)
                except ftplib.error_perm as e:
                        file_remoto.close()
                        print '[ERROR] %s' %(e) #Error 500-599
                        os.remove(filename)
                        print 'Download interrotto'
                except IOError as e:
                        print '[ERROR]%s' %(e)
                        print '[!!]Sintassi corretta del comando DW: DW directory_remoto file_remoto directory_uscita esempio: DW / favicon.ico C:\Users\normal_user\Desktop'
                        print 'Per maggiori informazioni usare il comando HELP'
                        
                    
        def download_all_file(self,directory_remota,directory_uscita = os.getcwd()):
                """Comando: DWA Parametri: directory_remota, directory_uscita

                   Compito: prende tutti i nomi di file di directory_remota e li scarica uno ad uno tramite il metodo download nella cartella d'uscita"""
                try:
                        self.change_directory('R',directory_remota)
                        for x in self.user.mlsd(facts = ['type']):
                                if x[1]['type'] == 'file':
                                        self.download(directory_remota, x[0], directory_uscita)
                except ftplib.error_perm as e:
                        print '[ERROR] %s' %(e) #Error 500-599
                except ftplib.error_temp as e:
                        print '[ERROR] %s' %(e) #Error 400-499
                        
                
        def lista_file(self):
                """Comando: LIST    Parametri: //
                   Compito: Stampa la lista di file nella directory remota corrente"""
                try:
                        list_file = self.user.mlsd(facts=['type','size'])
                        files = []
                        for x in list_file:
                                files.append(x.strip('),('))
                        for x in files:
                                print x
                                print
                                
                except ftplib.error_temp,e:
                        print '[ERROR]%s'%(e)
                        print 'Connessione...'
                        self.user.connect(self.site)
                        self.user.login(self.nick,self.pwd)

        
        def rename_file(self,filename,directory,nuovoNome):
                """Comando:REN         Paramentri: filename, directory, nuovoFile
                   Compito:Rinominare un file"""

                if self.search_file(filename,directory):
                        self.user.rename(filename,nuovoName)
                        print 'File: %s cambiato in: %s' %(filename,nuovoNome)
                        return True
                else:
                        print '[!!]Nessuna corrispondenza trovata!'
                        return False

        def delete_file (self,filename,directory):
                if self.search_file(filename,directory):
                        self.user.delete(filename)
                        print 'File %s cancellato!' %(filename)
                else:
                        print '[!!]File non trovato'
                        
                
        def upload(self,filename,directory_uscita):
                """Comando: UPL    Parametri: nameFile(Nome del file con relativo percorso), directory_uscita(Directory remota di uscita.
                   Compito: Invia un file al server                                          Il valore predefinito è la directory remota corrente).
                 """
                try:
                        self.change_directory('R',directory_uscita)
                        file_locale = open(filename,'rb')
                        self.user.storbinary('STOR %s' %(str(filename)), file_locale)
                        print 'File inviato in %s' %(self.user.pwd())
                except ftplib.error_perm,e:
                        print '[ERROR] %s' %(e)
                except IOError,e:
                        print '[ERROR]%s' %(e)
                        print '[!!]Sintassi corretta del comando UPL: UPL  file_remoto directory_uscita esempio: UPL  favicon.ico C:\Users\normal_user\Desktop\Eggs'
        
        def controlla_cmd(self,comando):
                """Controlla se il  comando è valido"""
                comando = comando.split()
                comando_trovato = False
                for x in comando:
                        if x.upper() in self.comandi:
                                comando_trovato = True
                                cmd = x.upper()
                                self.avvia_cmd(cmd,[y for y in comando if y != x])
                                break
                        else:
                                continue
                if not comando_trovato:
                        print 'Usare help per una lista completa dei comandi'

                
        def avvia_cmd(self,cmd, argv):
                """Avvia il comando passato come parametro"""
                argv =  list(argv)
                numero_parametri = len(argv)
                if cmd == self.comandi[0]:
                        self.remote_directory()
                elif cmd == self.comandi[1]:
                        self.local_directory()
                elif cmd == self.comandi[2]:
                        if numero_parametri < 2:
                                print '[ERROR]Parametri insufficenti!\nSintassi corretta: CD R NomeDirectory. CD L NomeDirectory.R=remote, L = Local.\nPer maggiori info usare il comando HELP\n'
                                return False
                        else:
                                self.change_directory(argv[0],argv[1])
                elif cmd == self.comandi[3]:
                        if numero_parametri < 2:
                                print '[ERROR]Parametri non sufficienti'
                                return False
                        elif numero_parametri < 3:
                                print '[!!]Attenzione non è stata specificata la directory di uscita.Il file verrà salvato nelle directory corrente'
                                self.download(argv[0],argv[1])                                
                        else:
                                self.download(argv[0],argv[1],argv[2])
                elif cmd == self.comandi[4]:
                        if numero_parametri < 1:
                                print '[ERROR]Parametri non sufficienti'
                        elif numero_parametri < 2:
                                print '[!!]Attenzione non è stata specificata la directory di uscita.I files verranno salvati nelle directory corrente'
                                self.download_all_file(argv[0])
                        else:
                                self.download_all_file(argv[0],argv[1])
                elif cmd == self.comandi[5]:
                        self.lista_file()
                elif cmd == self.comandi[6]:
                        if numero_parametri < 2:
                                print '[ERROR]Parametri non sufficienti'
                        else:
                                self.search_file(argv[0],argv[1])
                elif cmd == self.comandi[7]:
                        if numero_parametri < 3:
                                print '[ERROR]Parametri non sufficienti'
                        else:
                                self.rename_file(argv[0],argv[1],argv[2])
                elif cmd ==  self.comandi[8]:
                        if numero_parametri < 2:
                                print'[ERROR]Parametri non sufficienti'
                        else:
                                self.delete_file(argv[0],argv[1])
                elif cmd == self.comandi[9]:                                        
                        if numero_parametri < 2:
                                print '[ERROR]Parametri non sufficienti'
                        else:
                                self.upload(argv[0],argv[1])
                elif cmd == self.comandi[10]:
                        self.disconnect()
                elif cmd == self.comandi[11]:
                        help(Client)
                elif cmd == self.comandi[12]:
                        self.info()



######## MAIN LOOP ########################
pres = Presentazione()
#pres.connect("delete-event", gtk.main_quit) 
		#Se tolgo o metto il commento influisco sulla chiusura delle finestre
		#Se c'è: con il click in alto a destro chiudo solo la Presentazione()
		# ovvero si chiude solo lei e non la finestra dei button o la GUI dell'applicazione
		#se NON c'è: le finestre si chiudono tutte eseguendo un click in alto a destra.
		#comunque tutto dipende dal LOOP PRINCIPALE [Gtk.mail()] se è unico o no
pres.show_all()
#time.sleep(4)
#pres.hide()

#Questa è la finestra principale con i bottoni per startare le attività.
#Si chiude con la 'X' in alto a destra 
start = MainWin()
start.show_all()

######### FTP Client ############################
#if __name__ == '__main__':
#        nick = raw_input('Nick:')
#        pwd = raw_input('Password:')
#        site = raw_input('Sito:')
#        obj = ClientFTP(site,nick,pwd)
#        while obj.online: #while True
#                command = raw_input('pyFTP >>> ')
#                obj.controlla_cmd(command)      
#################################################

gtk.main()
