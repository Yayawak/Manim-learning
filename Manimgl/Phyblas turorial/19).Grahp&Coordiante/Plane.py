import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        axes = mnm.NumberPlane()
        axes.add_coordinate_labels()
        self.wait()
        self.play(
            mnm.Write(axes),
            run_time=2
        )