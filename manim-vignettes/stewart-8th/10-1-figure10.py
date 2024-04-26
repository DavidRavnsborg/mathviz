from manim import *
from manim.utils.file_ops import open_file as open_media_file


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        surface = ParametricFunction(
            lambda t: np.array(
                [
                    # x = f(t)
                    t + np.sin(5 * t),
                    # y = g(t)
                    t + np.sin(6 * t),
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


if __name__ == "__main__":
    scene = AnimateParametricFunction()
    scene.render()  # That's it!

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
