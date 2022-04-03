import manimlib as mnm

class Manimala(mnm.Scene):
    def construct(self):
        mat = [[1.2,3.5,3.4],
        [5.2,1.2,4.3]]

        mat1 = mnm.DecimalMatrix(mat)
        mat1.set_color('#ddf2a9')
        mat1.set_width(12)

        # mat2 = [[1,2,3],[3,5,6]]
        mat2 = mnm.IntegerMatrix(mat)
        mat2.set_color('#caa0f2')
        mat2.set_width(12)

        self.play(
            mnm.Transform(mat1,mat2),
            run_time=2
        )