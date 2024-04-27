from manim import (
    DashedLine,
    Line,
    ThreeDAxes,
    ThreeDScene,
    DEGREES,
    ORIGIN,
    OUT,
    RED,
)
from manim.utils.file_ops import open_file as open_media_file
import numpy as np


class ThreeDAxesTest(ThreeDScene):

    def construct(self):
        axes_3d = ThreeDAxes(
            # unit_size=1 in Z axis
            z_range=(-3, 3, 1),
            z_length=6,
        )
        self.set_camera_orientation(phi=70 * DEGREES, theta=240 * DEGREES)

        main_line = Line(ORIGIN, axes_3d.c2p(4, 3) + 2 * OUT, color=RED)
        vertical_line = DashedLine(axes_3d.c2p(4, 0), axes_3d.c2p(4, 3))
        horizontal_line = DashedLine(axes_3d.c2p(0, 3), axes_3d.c2p(4, 3))
        fall_line = DashedLine(axes_3d.c2p(4, 3), axes_3d.c2p(4, 3) + OUT * 2)
        self.add(axes_3d)
        self.add(main_line)
        self.add(vertical_line)
        self.add(horizontal_line)
        self.add(fall_line)
        self.wait(1)


if __name__ == "__main__":
    scene = ThreeDAxesTest()
    scene.render()

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
