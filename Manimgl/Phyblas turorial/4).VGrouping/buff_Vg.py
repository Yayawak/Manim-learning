import manimlib as mnm

class ABBB(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('ก',color='#aaeeaa',size=6)
        text2 = mnm.Text('ข',color='#eeaaaa',size=5)
        text3 = mnm.Text('ค',color='#aaaaee',size=7)

        vg = mnm.VGroup(text1,text2,text3)
        vg.arrange(mnm.RIGHT,buff=2)

        self.add(vg)
