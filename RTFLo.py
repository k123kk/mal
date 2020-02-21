import appex, ui
import os
from math import ceil, floor


#=========================================




COLS = 3
ROWS = 3








print('تنويه : لست مسئول عن الاستخدامات المسيئه + تشمل الاداة تحديثات مستمره كل 3 ايام يعني لاحاجة الي تحميلها من اخري ♥️  ')

print('==========================================')

print('لتشغيل الاداة اضغط انتر')

y = input('')



SHORTCUTS = [
{'title': 'ارسل لي اميل', 'url': 'mailto://flaaah777@gmail.com', 'color': '#5e96ff', 'icon': 'iow:email_24'},
{'title': 'ارسل لي رسالة', 'url': 'WhatsApp://send?phone=+966596880836', 'color': '#5ec0ff', 'icon': 'iow:chatbox_24'},

{'title': 'snapchat', 

'url': 'snapchat://add/flaah999', 


'color': '#ffe652', 'icon': 'iow:chevron_right_24'},

{'title': 'بطاقات فيزا', 'url': 'http://flaah999.byethost7.com/flo.txt', 'color': '#4dd19d'},

{'title': ' تسريبات', 'url': 'http://flaah999.byethost7.com/flo1.txt', 'color': '#5ab8ff' },

{'title': 'برامج بلس', 'url': 'https://www.emad1saleh.com/iphone', 'color': '#ffd026' },
{'title': 'جلبريك', 'url': 'https://1174829.site123.me', 'color': '#ff8e13'},
{'title': 'مواقع مصابه', 'url': 'http://flaah999.byethost7.com/flo2.txt', 'color': '#ff4a09'},

{'title': 'pc ادوات', 'url': 'http://flaah999.byethost7.com/flo3.txt', 'color': '#ffb5b5'},

]



class LauncherView (ui.View):
	def __init__(self, shortcuts, *args, **kwargs):
		row_height = 110 / ROWS
		super().__init__(self, frame=(0, 0, 300, ceil(len(shortcuts) / COLS) * row_height), *args, **kwargs)
		self.buttons = []
		for s in shortcuts:
			btn = ui.Button(title=' ' + s['title'], image=ui.Image(s.get('icon', 'iow:social_apple_32')), name=s['url'], action=self.button_action, bg_color=s.get('color', '#55bcff'), tint_color='#000000', corner_radius=9)
			self.add_subview(btn)
			self.buttons.append(btn)
	
	def layout(self):
		bw = self.width / COLS
		bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
		for i, btn in enumerate(self.buttons):
			btn.frame = ui.Rect(i%COLS * bw, i//COLS * bh, bw, bh).inset(2, 2)
			btn.alpha = 1 if btn.frame.max_y < self.height else 0
	
	def button_action(self, sender):
		import webbrowser
		webbrowser.open(sender.name)

def main():
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	v = appex.get_widget_view()
	# Optimization: Don't create a new view if the widget already shows the launcher.
	if v is None or v.name != widget_name:
		v = LauncherView(SHORTCUTS)
		v.name = widget_name
		appex.set_widget_view(v)


if __name__ == '__main__':
	main()
