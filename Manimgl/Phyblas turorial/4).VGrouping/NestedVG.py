import manimlib as mnm

class AAAA(mnm.Scene):
    def construct(self):
        text1 = mnm.Text('ขวาล่าง',color='#aaeeaa',size=2.5)
        text2 = mnm.Text('ขวาบน',color='#eeaaaa',size=3.5)
        text3 = mnm.Text('ซ้าย',color='#aaaaee',size=4.5)

        vg = mnm.VGroup(text1,text2)
        vg.arrange()

        vg2 = mnm.VGroup(vg,text3)
        vg2.arrange(mnm.UP)

        self.add(vg2)
