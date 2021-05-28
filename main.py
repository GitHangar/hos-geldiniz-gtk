#!/usr/bin/env python3

# Bu dosya "GNU/Linux Hoş Geldiniz Uygulaması" programının bir parçasıdır.

# Copyright (C) 2021 Alperen İsa Nalbant

# Bu program özgür yazılımdır: Özgür Yazılım Vakfı tarafından 
# yayımlanan GNU Genel Kamu Lisansı’nın sürüm 3 ya da 
# (isteğinize bağlı olarak) daha sonraki sürümlerinin hükümleri 
# altında yeniden dağıtabilir ve/veya değiştirebilirsiniz.

# Bu program, yararlı olması umuduyla dağıtılmış olup, programın 
# BİR TEMİNATI YOKTUR; TİCARETİNİN YAPILABİLİRLİĞİNE VE ÖZEL BİR 
# AMAÇ İÇİN UYGUNLUĞUNA dair bir teminat da vermez. Ayrıntılar 
# için GNU Genel Kamu Lisansı’na göz atınız.

# Bu programla birlikte GNU Genel Kamu Lisansı’nın bir kopyasını 
# elde etmiş olmanız gerekir. Eğer elinize ulaşmadıysa 
# <http://www.gnu.org/licenses/> adresine bakınız.

import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

from window import MainWindow

class Uygulama(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
            application_id="ml.yapboz.libreos.welcome",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs)
    
    def do_activate(self):
        self.window = MainWindow(self)

app = Uygulama()
app.run(sys.argv)