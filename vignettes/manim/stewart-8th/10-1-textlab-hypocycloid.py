from manim import *
from manim.utils.file_ops import open_file as open_media_file


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


if __name__ == "__main__":
    scene = AnimateParametricFunction()
    scene.render()  # That's it!

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
