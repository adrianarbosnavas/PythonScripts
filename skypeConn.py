#!/usr/bin/python
from skpy import SkypeEventLoop, SkypeNewMessageEvent
import os

class MySkype(SkypeEventLoop):
	def onEvent(self, event):
		if isinstance(event, SkypeNewMessageEvent) and not event.msg.userId == self.userId:
			# print(event.msg.raw.get('imdisplayname'))
			# print(event.msg.content)
			os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (1, 440))

sk = MySkype(tokenFile="token", autoAck=True)
sk.loop()

# Para generar un token primero se debe realizar una conexion importando Skype de skpy de la siguiente manera
# from skpy import Skype
# sk = Skype('usuario', 'pass', 'nombre_del_token')
