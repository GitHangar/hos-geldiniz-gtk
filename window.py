# Bu dosya "GNU/Linux'a Hoş Geldiniz Uygulaması" programının bir parçasıdır.

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

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio


class MainWindow:
    def __init__(self, app):
        self.builder = Gtk.Builder()

        self.builder.add_from_file("window.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.window.set_application(app)
        
        self.window.show_all()

        self.stk_win = self.builder.get_object("stk_window")
        self.stk_head = self.builder.get_object("stk_header")

    # İlk Sayfa: Hoş geldiniz
    def on_btn_baslat_clicked(self, button):
        self.stk_win.set_visible_child_name("etkinlik")
        self.stk_head.set_visible_child_name("etkinlik")

    def on_btn_kalsin_clicked(self, button):
        self.window.get_application().quit()

    # 2. sayfa: Etkinliklere göz atın
    def on_btn_etkinlik_geri_clicked(self, button):
        self.stk_win.set_visible_child_name("hosgeldiniz")
        self.stk_head.set_visible_child_name("hosgeldiniz")

    def on_btn_etkinlik_ileri_clicked(self, button):
        self.stk_win.set_visible_child_name("yazilim")
        self.stk_head.set_visible_child_name("yazilim")

    # 3. Sayfa: Yazılım indir
    def on_btn_yazilim_geri_clicked(self, button):
        self.stk_win.set_visible_child_name("etkinlik")
        self.stk_head.set_visible_child_name("etkinlik")

    def on_btn_yazilim_ileri_clicked(self, button):
        self.stk_win.set_visible_child_name("ozellestir")
        self.stk_head.set_visible_child_name("ozellestir")

    # 4. Sayfa: Özelleştir
    def on_btn_ozellestir_geri_clicked(self, button):
        self.stk_win.set_visible_child_name("yazilim")
        self.stk_head.set_visible_child_name("yazilim")

    def on_btn_ozellestir_ileri_clicked(self, button):
        self.stk_win.set_visible_child_name("bitti")
        self.stk_head.set_visible_child_name("bitti")

    def on_btn_ozellestir_ontanimli_clicked(self, button):
        os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Orchis'")
        os.system("gsettings set org.gnome.desktop.interface icon-theme 'Flat-Remix-Blue-Light'")

    def on_btn_ozellestir_acik_clicked(self, button):
        os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Orchis-light'")
        os.system("gsettings set org.gnome.desktop.interface icon-theme 'Flat-Remix-Blue-Light'")

    def on_btn_ozellestir_koyu_clicked(self, button):
        os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Orchis-dark'")
        os.system("gsettings set org.gnome.desktop.interface icon-theme 'Flat-Remix-Blue-Dark'")

    # 5. Sayfa: Tamamlandı!
    def on_btn_tamam_geri_clicked(self, button):
        self.stk_win.set_visible_child_name("ozellestir")
        self.stk_head.set_visible_child_name("ozellestir")

    def on_btn_cik_clicked(self, button):
        self.window.get_application().quit()
