from manim import *


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        colors = ["#0000ff", "#8bff26", "#26e9ff", "#ff3c00", "#ffa600"]
        surface = ParametricFunction(
            lambda t: np.array(
                [
                    # x = f(t)
                    2.7 * np.cos(t) + np.sin(2 * t) * np.cos(60 * t),
                    # y = g(t)
                    np.sin(2 * t) + np.sin(60 * t),
                    # z = h(t)
                    # 5*np.cos(t)
                    1,
                ]
            ),
            color=RED,
            t_range=np.array([0, TAU, 0.01]),
            stroke_width=1,
        )
        surface.set_color_by_gradient(colors)
        axes = ThreeDAxes()
        self.add(axes)
        # Play animation for 20 seconds
        self.play(Create(surface), run_time=20)
        # Number of seconds to wait after animation.
        self.wait(2)
