import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        self.play(
            mnm.Write(
                mnm.VGroup(
                    mnm.Annulus(inner_radius=0.5,outer_radius=1,color='#5c2480'),
                    mnm.Annulus(inner_radius=2,outer_radius=1.5,color='#5c24aa'),
                    mnm.Annulus(inner_radius=5,outer_radius=7,color='#5cff80')
                )
            ),
            run_time=4

        )
