import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        samliam = mnm.Triangle(color='#FF6622')
        samakan = mnm.Tex(r'4 \times 3 = 12',color='#22FF99')
        khokhwam = mnm.Text('มณีมาลา',color='#8888FF')
        self.add(khokhwam,samliam,samakan)
