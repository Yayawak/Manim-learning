import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        text = mnm.Text('oooooooo\noooooooo\noooooooo\noooooooo',size=3)
        text.set_color_by_gradient('#ff0000','#00ff00','#0000ff')
        self.add(text)

        self.play(
            text.animate.set_color_by_gradient('#00ffff','#ff00ff','#ffff00'),
            lag_ratio=0.9,
            run_time=4
        )
