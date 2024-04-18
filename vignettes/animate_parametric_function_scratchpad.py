from manim import *


class AnimateParametricFunctionScratchPad(ThreeDScene):
    def construct(self):
        surface = ParametricFunction(
            lambda t: np.array(
                [
                    # x = f(t)
                    np.sin(0.5 * t),
                    # y = g(t)
                    np.cos(0.5 * t),
                    # z = h(t)
                    0,
                ]
            ),
            color=RED,
            t_range=np.array([-PI, PI, 0.01]),
            stroke_width=1,
        )
        axes = ThreeDAxes()
        self.add(axes)
        # Play animation for 20 seconds
        self.play(Create(surface), run_time=10)
        # Number of seconds to wait after animation.
        self.wait(2)
