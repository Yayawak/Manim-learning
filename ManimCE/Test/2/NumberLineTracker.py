from manim import *

class ValueTrackerExample(Scene):
      def construct(self):
            number_line = NumberLine()
            pointer = Vector(DOWN)
            label = MathTex("x")
            always(label.next_to,pointer,UP)

            tracker = ValueTracker(0)
            
            #! always is not always better!
            # always(
            #       pointer.next_to, number_line.n2p(tracker.get_value()), UP
            # )
            pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                        )
            )
            
            self.wait()
            self.add(number_line, pointer,label)
            tracker += 1.5
            self.wait(1)
            tracker -= 4
            self.wait(0.5)
            self.play(tracker.animate.set_value(5)),
            self.wait(0.5)
            self.play(tracker.animate.set_value(3))
            self.play(tracker.animate.increment_value(-2))
            self.wait(0.5)