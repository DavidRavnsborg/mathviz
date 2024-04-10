from manim import *


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        a = 23
        b = 1
        axes = ThreeDAxes(
            x_range=(-10, 10, 5),
            y_range=(-10, 10, 5),
            #
        )
        self.add(axes)
        self.play(
            Create(
                ParametricFunction(
                    lambda t: np.array(
                        [
                            # x = f(t)
                            (a - b) * np.cos(t) + b * np.cos(((a - b) / b) * t),
                            # y = g(t)
                            (a - b) * np.sin(t) - b * np.sin(((a - b) / b) * t),
                            # z = h(t)
                            -100,
                        ]
                    ),
                    color=RED,
                    t_range=np.array([0, TAU, 0.01]),
                    stroke_width=3,
                )
            ),
            run_time=10,
        )
        self.wait(2)
