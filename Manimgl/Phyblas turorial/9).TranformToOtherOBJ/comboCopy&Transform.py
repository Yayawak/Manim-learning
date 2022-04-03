import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.VGroup(
            mnm.Text('อีวุย',color='#f8c991',size=1.8),
            mnm.Text('เชาเวอร์ส',color='#91c6f8',size=2.2),
            mnm.Text('ธันเดอร์ส',color='#f8f491',size=2.2),
            mnm.Text('บูสเตอร์',color='#f8a291',size=2.2),
        )

        text.arrange(mnm.DOWN)
        self.add(text[0])
        self.play(
            mnm.Transform(text[0].copy(),text[1])
        )
        self.play(

            mnm.Transform(text[1].copy(),text[2])
        )
        self.play(

            mnm.Transform(text[2].copy(),text[3])
        )
