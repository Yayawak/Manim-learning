import manimlib as mnm

class AAAA(mnm.Scene):
    def construct(self):
        t = mnm.Text('๑', color='#aacc55')
        grid = t.get_grid(n_rows=18,n_cols=8,buff=0.5)
        self.add(grid)
