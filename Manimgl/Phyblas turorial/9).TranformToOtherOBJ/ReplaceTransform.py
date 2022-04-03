import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.VGroup(
            mnm.Text('๑',color='#f6b3c9',size=4),
            mnm.Text('๒',color='#beb3f6',size=4),
            mnm.Text('๓',color='#b3f6cb',size=4),
            mnm.Text('๔',color='#f6f4b3',size=4),
        )

        text.arrange_in_grid(n_cols=2)
        self.add(text[0])

        self.wait(2)
        self.play(
            mnm.ReplacementTransform(text[0],text[1])
        )
        self.play(
            mnm.ReplacementTransform(text[1],text[2])
        )
        self.play(
            mnm.ReplacementTransform(text[2],text[3])
        )
        self.play(
            mnm.ReplacementTransform(text[3],text[4])
        )
