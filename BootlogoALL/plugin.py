from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox
from Screens.Console import Console
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.AVSwitch import AVSwitch
from Components.config import config, configfile, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection, ConfigNumber, ConfigText, ConfigInteger
from Components.ConfigList import ConfigListScreen
from Components.Label import Label
from Components.Language import language
from os import environ, listdir, remove, rename, system
from skin import parseColor
from Components.Pixmap import Pixmap
from Components.Label import Label
import gettext
from enigma import ePicLoad
from Tools.Directories import fileExists, resolveFilename, SCOPE_LANGUAGE, SCOPE_PLUGINS
from enigma import ePicLoad, getDesktop, eConsoleAppContainer
from Components.Sources.StaticText import StaticText

#############################################################

DESKTOP_WIDTH = getDesktop(0).size().width()

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("BootlogosALL", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/BootlogoALL/locale/"))

def _(txt):
	t = gettext.dgettext("BootlogosALL", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

def translateBlock(block):
	for x in TranslationHelper:
		if block.__contains__(x[0]):
			block = block.replace(x[0], x[1])
	return block

#############################################################
#############################################################
config.plugins.BootlogosALL = ConfigSubsection()
config.plugins.BootlogosALL.active = ConfigSelection(default="Bootlogo12", choices = [
				("Bootlogo1", _("Bootlogo1")),
				("Bootlogo2", _("Bootlogo2")),
				("Bootlogo3", _("Bootlogo3")),
				("Bootlogo4", _("Bootlogo4")),
				("Bootlogo5", _("Bootlogo5")),
				("Bootlogo6", _("Bootlogo6")),
				("Bootlogo7", _("Bootlogo7")),
				("Bootlogo8", _("Bootlogo8")),
				("Bootlogo9", _("Bootlogo9")),
				("Bootlogo10", _("Bootlogo10")),
				("Bootlogo11", _("Bootlogo11")),
				("Bootlogo12", _("Bootlogo12"))
				])
#############################################################
#############################################################

class BootlogosALL(ConfigListScreen, Screen):

	if DESKTOP_WIDTH <= 1280:
	  skin = """
<screen name="Bootlogo-Setup" position="0,0" size="1280,720" flags="wfNoBorder" backgroundColor="#00000000">
  <widget backgroundColor="#0003001E" source="title" render="Label" font="Regular;34" foregroundColor="#00ffffff" position="70,7" size="1000,46" transparent="1" halign="left" valign="center" />
  <widget source="global.CurrentTime" render="Label" backgroundColor="#0003001E" foregroundColor="#00ffffff" position="1138,17" size="100,28" font="Regular;26" halign="right" transparent="1" valign="center">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget backgroundColor="#00000000" name="config" position="70,80" size="708,30" font="Regular;22" foregroundColor="#00ffffff" foregroundColorSelected="#00ffffff" backgroundColorSelected="#000E0C3F" itemHeight="30" transparent="1" />
  <widget backgroundColor="#00000000" source="previewtext" render="Label" font="Regular;26" foregroundColor="#00ffffff" position="70,130" size="708,32" transparent="1" zPosition="1" />
  <widget backgroundColor="#00000000" name="bootlogohelperimage" position="257,180" size="334,188" zPosition="1" />
  <widget source="session.VideoPicture" render="Pig" position="822,80" size="416,234" zPosition="3" backgroundColor="#ffffffff" />
  <ePixmap backgroundColor="#00000000" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/logo_1280.png" position="902,349" size="256,256" alphatest="blend" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/ibar_1280.png" position="0,640" size="1280,80" zPosition="-9" alphatest="blend" />
  <eLabel position="0,640" size="1280,2" backgroundColor="#001B1775" zPosition="-8" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/ibaro_1280.png" position="0,0" size="1280,59" zPosition="-9" alphatest="blend" />
  <eLabel position="0,58" size="1280,2" backgroundColor="#001B1775" zPosition="-8" />
  <eLabel backgroundColor="#00E61805" position="65,697" size="150,5" />
  <eLabel backgroundColor="#005FE500" position="315,697" size="150,5" />
  <eLabel backgroundColor="#00E5DD00" position="565,697" size="150,5" />
  <eLabel backgroundColor="#000082E5" position="815,697" size="150,5" />
  <widget backgroundColor="#0003001E" source="key_red" render="Label" font="Regular;20" foregroundColor="#00ffffff" position="70,670" size="220,26" transparent="1" zPosition="1" />
  <widget backgroundColor="#0003001E" source="key_green" render="Label" font="Regular;20" foregroundColor="#00ffffff" position="320,670" size="220,26" transparent="1" zPosition="1" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/key_ok_1280.png" position="1145,675" size="43,22" alphatest="blend" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/key_exit_1280.png" position="1195,675" size="43,22" alphatest="blend" />
</screen>
"""
	else:
	  skin = """
<screen name="Bootlogo-Setup" position="0,0" size="1920,1080" flags="wfNoBorder" backgroundColor="#00000000">
  <widget backgroundColor="#0003001E" source="title" render="Label" font="Regular;51" foregroundColor="#00ffffff" position="105,10" size="1500,69" transparent="1" halign="left" valign="center" />
  <widget source="global.CurrentTime" render="Label" backgroundColor="#0003001E" foregroundColor="#00ffffff" position="1707,25" size="150,42" font="Regular;39" halign="right" transparent="1" valign="center">
    <convert type="ClockToText">Default</convert>
  </widget>
  <widget backgroundColor="#00000000" name="config" position="105,120" size="1062,45" font="Regular;32" foregroundColor="#00ffffff" foregroundColorSelected="#00ffffff" backgroundColorSelected="#000E0C3F" itemHeight="45" transparent="1" />
  <widget backgroundColor="#00000000" source="previewtext" render="Label" font="Regular;38" foregroundColor="#00ffffff" position="105,195" size="1062,48" transparent="1" zPosition="1" />
  <widget backgroundColor="#00000000" name="bootlogohelperimage" position="386,270" size="500,282" zPosition="1" />
  <widget source="session.VideoPicture" render="Pig" position="1233,120" size="624,351" zPosition="3" backgroundColor="#ffffffff" />
  <ePixmap backgroundColor="#00000000" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/logo_1920.png" position="1353,523" size="384,384" alphatest="blend" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/ibar_1920.png" position="0,960" size="1920,120" zPosition="-9" alphatest="blend" />
  <eLabel position="0,960" size="1920,3" backgroundColor="#001B1775" zPosition="-8" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/ibaro_1920.png" position="0,0" size="1920,88" zPosition="-9" alphatest="blend" />
  <eLabel position="0,87" size="1920,3" backgroundColor="#001B1775" zPosition="-8" />
  <eLabel backgroundColor="#00E61805" position="97,1045" size="225,7" />
  <eLabel backgroundColor="#005FE500" position="472,1045" size="225,7" />
  <eLabel backgroundColor="#00E5DD00" position="847,1045" size="225,7" />
  <eLabel backgroundColor="#000082E5" position="1222,1045" size="225,7" />
  <widget backgroundColor="#0003001E" source="key_red" render="Label" font="Regular;30" foregroundColor="#00ffffff" position="105,1005" size="330,39" transparent="1" zPosition="1" />
  <widget backgroundColor="#0003001E" source="key_green" render="Label" font="Regular;30" foregroundColor="#00ffffff" position="480,1005" size="330,39" transparent="1" zPosition="1" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/key_ok_1920.png" position="1717,1012" size="65,33" alphatest="blend" />
  <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/images/key_exit_1920.png" position="1792,1012" size="65,33" alphatest="blend" />
</screen>
"""

	def __init__(self, session, args = None, picPath = None):
		self.config_lines = []
		Screen.__init__(self, session)
		self.session = session
		self.bootlogosourcepath = "/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/logos/"
		self.picPath = picPath
		self.Scale = AVSwitch().getFramebufferScale()
		self.PicLoad = ePicLoad()
		self["bootlogohelperimage"] = Pixmap()
		list = []
		list.append(getConfigListEntry(_("Select Bootlogo:"), config.plugins.BootlogosALL.active))
		ConfigListScreen.__init__(self, list)
		self["actions"] = ActionMap(["OkCancelActions","DirectionActions", "InputActions", "ColorActions"], {"left": self.keyLeft,"down": self.keyDown,"up": self.keyUp,"right": self.keyRight,"red": self.exit,"green": self.save,"cancel": self.exit}, -1)
		self["title"] = StaticText(_("Bootlogos-SDG"))
		self["previewtext"] = StaticText(_("Preview") + ":")
		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self.onLayoutFinish.append(self.UpdatePicture)

	def GetPicturePath(self):
		try:
			returnValue = self["config"].getCurrent()[1].value
			path = "/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/preview/" + returnValue + ".png"
			return path
		except:
			return "/usr/lib/enigma2/python/Plugins/Extensions/BootlogoALL/preview/nopreview.png"

	def UpdatePicture(self):
		self.PicLoad.PictureData.get().append(self.DecodePicture)
		self.onLayoutFinish.append(self.ShowPicture)

	def ShowPicture(self):
		self.PicLoad.setPara([self["bootlogohelperimage"].instance.size().width(),self["bootlogohelperimage"].instance.size().height(),self.Scale[0],self.Scale[1],0,1,"#20000000"])
		self.PicLoad.startDecode(self.GetPicturePath())

	def DecodePicture(self, PicInfo = ""):
		ptr = self.PicLoad.getData()
		self["bootlogohelperimage"].instance.setPixmap(ptr)

	def keyLeft(self):
		ConfigListScreen.keyLeft(self)
		self.ShowPicture()

	def keyRight(self):
		ConfigListScreen.keyRight(self)
		self.ShowPicture()

	def keyDown(self):
		self["config"].instance.moveSelection(self["config"].instance.moveDown)
		self.ShowPicture()

	def keyUp(self):
		self["config"].instance.moveSelection(self["config"].instance.moveUp)
		self.ShowPicture()
		restartbox.setTitle(_("Restart STB"))

	def save(self):
		for x in self["config"].list:
			if len(x) > 1:
					x[1].save()
			else:
					pass
		configfile.save()
		self.changebootlogo()
		configfile.save()

		#self.session.open(MessageBox, _("Configuration files successfully generated!.\nTo apply changes reboot your Box and start OscamSmartcard in Softcampanel!"), MessageBox.TYPE_INFO)
		restartbox = self.session.openWithCallback(self.restartSTB,MessageBox,_("Your STB needs a restart to apply the new bootlogo.\nDo you want to Restart you STB now?"), MessageBox.TYPE_YESNO)
		restartbox.setTitle(_("Restart STB"))

	def changebootlogo(self):
		try:
			self.bootlogoactive = (config.plugins.BootlogosALL.active.value + ".mvi")
			self.bootlogosource = (self.bootlogosourcepath + self.bootlogoactive)
			self.bootlogotarget = "/usr/share/bootlogo.mvi"
			self.bootlogocommand = (self.bootlogosource + " " + self.bootlogotarget)
			#print "[Bootlogo] ", self.bootlogocommand
			system('cp -f ' + self.bootlogocommand)
			self.config_lines = []
		except:
			self.session.open(MessageBox, _("Error setting Bootlogo!"), MessageBox.TYPE_ERROR)
			self.config_lines = []

	def restartSTB(self, answer):
		if answer is True:
			configfile.save()
			system('reboot')
		else:
			self.close()

	def exit(self):
		for x in self["config"].list:
			if len(x) > 1:
					x[1].cancel()
			else:
					pass
		self.close()

#############################################################

def main(session, **kwargs):
	session.open(BootlogosALL)

def Plugins(**kwargs):
	screenwidth = getDesktop(0).size().width()
	if screenwidth and screenwidth == 1920:
		return [PluginDescriptor(name="Bootlogo", description=_("Configuration tool for Bootlogo"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='pluginfhd.png', fnc=main)]
	else:
		return [PluginDescriptor(name="Bootlogo", description=_("Configuration tool for Bootlogo"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='plugin.png', fnc=main)]
