from vignettes.context import mathviz
from mathviz.validate_and_parse import validate_and_parse
from manim import Scene, ThreeDScene, MathTex, ParametricFunction, Write, Axes, RED
from manim.utils.file_ops import open_file as open_media_file
import numpy as np
from sympy import symbols, lambdify, sympify


class MathExpressionScene(ThreeDScene):
    def construct(self):
        input_expr = "t**2 + 3*t + 1"  # Example user-provided expression

        # Create a symbolic variable
        t = symbols("t")
        # Parse the expression using sympy
        expr = validate_and_parse(input_expr)

        # Create a lambda function for the expression
        f = lambdify(t, expr, "numpy")

        # Define the parametric function using the lambda
        def parametric_func(t):
            return np.array([t, f(t), 0])  # z-coordinate is 0 for 2D graph

        # Create the ParametricFunction object
        curve = ParametricFunction(
            parametric_func, t_range=[-10, 10], color=RED  # Define the range of t
        )

        # Create an axes object
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-20, 110, 10],  # axis_config={"color": WHITE}
        )

        # Add axes to the scene
        self.add(axes)
        # Animate the curve
        self.play(Write(curve))
        # Wait to view the result
        self.wait(2)

        # Display the expression
        math_expr = MathTex(input_expr.replace("**", "^"))
        # math_expr.to_edge(UP)
        self.play(Write(math_expr))
        self.wait(2)


if __name__ == "__main__":
    scene = MathExpressionScene()
    scene.render()  # That's it!

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
