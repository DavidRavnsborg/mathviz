from manim import (
    ThreeDAxes,
    ThreeDScene,
    ParametricFunction,
    Point,
    BLUE,
    RED,
    YELLOW,
)
from manim.utils.file_ops import open_file as open_media_file
import numpy as np


class ParabolaAlignmentTest(ThreeDScene):
    """This demonstrates why it's better to use plotting functions attached to the axes object. The
    RED curve uses this function and is properly aligned. The BLUE curve uses ParametricFunction and
    is misaligned.

    NOTE: The 2 YELLOW points are also misaligned with the axes (though they are aligned with the
    BLUE ParametricCurve)."""

    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.add(
            axes.plot_parametric_curve(
                lambda t: np.array([t, (t - 2) ** 2 - 1, 0]),
                t_range=[-1, 5],
                color=RED,
            )
        )
        self.add(
            ParametricFunction(
                lambda t: np.array([t, (t - 2) ** 2 - 1, 0]),
                t_range=[-1, 5],
                color=BLUE,
            )
        )
        self.add(Point([0, 3, 0], color=YELLOW))
        self.add(Point([2, -1, 0], color=YELLOW))
        self.wait(1)


if __name__ == "__main__":
    scene = ParabolaAlignmentTest()
    scene.render()

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
