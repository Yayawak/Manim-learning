import manimlib as mnm

class GridTextSize(mnm.Scene):
    def construct(self):
        list_text = []
        for j in range(4):
            for i in range(3):
                s = i+j #size value
                fs = (j+1)*12 #font size val
                text = mnm.Text(f'{s},{fs}',size=s,font_size=fs)
                list_text.append(text)
        vg = mnm.VGroup(*list_text,buff=0)
        vg.arrange_in_grid(n_cols=3)
        self.play(
            mnm.Write(vg),
            run_time=4
        )
class SetHeight(mnm.Scene):
    def construct(self):
        ss =['a','b','a','b','a']
        vg = mnm.VGroup(*[mnm.Text(s,height=3,color='#aaffdd') for s in ss])
        vg.arrange(mnm.RIGHT)
        self.play(
            mnm.FadeIn(vg),run_time=4
        )
