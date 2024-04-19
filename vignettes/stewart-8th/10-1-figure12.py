from manim import *
from manim.utils.file_ops import open_file as open_media_file


# NOTE: This gives a different pattern than the one shown in the textbook.
class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        surface = ParametricFunction(
            lambda t: np.array(
                [
                    # x = f(t)
                    2.3 * np.sin(10 * t) + np.cos(23 * t),
                    # y = g(t)
                    2.3 * np.sin(10 * t) - np.sin(23 * t),
                    # z = h(t)
                    0,
                ]
            ),
            color=RED,
            t_range=np.array([0, TAU, 0.001]),
            stroke_width=3,
        )
        axes = ThreeDAxes()
        self.add(axes)
        self.play(Create(surface), run_time=10)
        self.wait(2)


if __name__ == "__main__":
    scene = AnimateParametricFunction()
    scene.render()  # That's it!

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
