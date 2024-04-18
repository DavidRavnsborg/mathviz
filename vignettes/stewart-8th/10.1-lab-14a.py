from manim import *


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.play(
            Create(
                ParametricFunction(
                    lambda t: np.array(
                        [
                            # x = f(t)
                            4 * np.sin(t),
                            # y = g(t)
                            2 * np.cos(t),
                            # z = h(t)
                            0,
                        ]
                    ),
                    color=RED,
                    t_range=np.array([0, TAU, 0.01]),
                    stroke_width=3,
                )
            ),
            Create(
                ParametricFunction(
                    lambda t: np.array(
                        [
                            # x = f(t)
                            -4 + np.cos(t),
                            # y = g(t)
                            1 + np.sin(t),
                            # z = h(t)
                            0,
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
