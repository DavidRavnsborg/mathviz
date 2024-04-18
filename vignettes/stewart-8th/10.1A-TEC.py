from manim import *


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        a, b, c, d = 1, 1, 1, 2
        surface = ParametricFunction(
            lambda t: np.array(
                [
                    # x = f(t)
                    a * np.cos(b * t),
                    # y = g(t)
                    c * np.sin(d * t),
                    # z = h(t)
                    0,
                ]
            ),
            color=RED,
            t_range=np.array([0, TAU, 0.01]),
            stroke_width=3,
        )
        axes = ThreeDAxes()
        self.add(axes)
        self.play(Create(surface), run_time=10)
        self.wait(2)
