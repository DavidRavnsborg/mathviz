from manim import *


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        surface = ParametricFunction(
            lambda t: np.array(
                [
                    # x = f(t)
                    np.sin(9 * t),
                    # y = g(t)
                    np.sin(10 * t),
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
