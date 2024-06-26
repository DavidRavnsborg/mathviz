from manim import *
from manim.utils.file_ops import open_file as open_media_file


class AnimateParametricFunction(ThreeDScene):
    def construct(self):
        a = 5
        b = 2
        axes = ThreeDAxes()
        self.add(axes)
        self.play(
            Create(
                ParametricFunction(
                    lambda t: np.array(
                        [
                            # x = f(t)
                            a * np.cos(t),
                            # y = g(t)
                            a * np.sin(t),
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
                            b * np.cos(t),
                            # y = g(t)
                            b * np.sin(t),
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
                            a * np.cos(t),
                            # y = g(t)
                            b * np.sin(t),
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


if __name__ == "__main__":
    scene = AnimateParametricFunction()
    scene.render()  # That's it!

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
