from manim import *
from manim.utils.file_ops import open_file as open_media_file


class ParametricCurveExample(Scene):
    def construct(self):
        axes = Axes()
        cardioid = axes.plot_parametric_curve(
            lambda t: np.array(
                [
                    np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                    np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                    0,
                ]
            ),
            t_range=[0, 2 * PI],
            color="#0FF1CE",
        )
        self.add(axes, cardioid)
        self.wait(1)


if __name__ == "__main__":
    scene = ParametricCurveExample()
    scene.render()

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
