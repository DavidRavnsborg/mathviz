from mathviz.validate_and_parse import validate_and_parse
from manim import Scene, ThreeDScene, MathTex, ParametricFunction, Write, Axes, RED
from manim.utils.file_ops import open_file as open_media_file
import numpy as np
from sympy import symbols, lambdify
from typing import Mapping, Tuple


class MathExpressionScene(ThreeDScene):
    """Take a text expression, converts it to a sympify expression, converts that to a function,
    and renders it with manim."""

    def __init__(self, input_expressions: Tuple[Mapping]):
        if len(input_expressions) < 2:
            raise Exception("Not enough input expressions.")
        elif len(input_expressions) > 3:
            raise Exception("Too many input expressions.")
        self.input_expressions = input_expressions
        super().__init__()

    def construct(self):
        """Called from self.render."""
        indepedent_var = symbols(self.input_expressions[0]["symbol"])
        funcs = []
        self.add(self.get_axes())
        for input_expr in self.input_expressions[1:]:
            # Parse the expression using sympy
            sympy_expr = validate_and_parse(input_expr["expression"])
            # Create a lambda function for the expression
            funcs.append(
                lambdify(args=indepedent_var, expr=sympy_expr, modules="numpy")
            )
            math_expr = MathTex(input_expr["expression"].replace("**", "^"))
            # math_expr.to_edge(UP)
            self.play(Write(math_expr))
        curve = ParametricFunction(
            function=self.get_parametric_lambda(funcs),
            t_range=[
                self.input_expressions[0]["domain"][0],
                self.input_expressions[0]["domain"][1],
            ],
            color=RED,  # Define the range of t
        )
        self.play(Write(curve))
        self.wait(2)

    def get_parametric_lambda(self, funcs):
        """Returns a function with the appropriate argument length. i is the independent variable."""
        if len(funcs) == 1:
            return lambda i: np.array([i, funcs[0](i), 0])
        elif len(funcs) == 2:
            return lambda i: np.array([i, funcs[0](i), funcs[1](i)])
        else:
            raise NotImplementedError()

    def get_axes(self):
        if len(self.input_expressions) == 2:
            return Axes(
                x_range=self.input_expressions[0]["domain"],
                y_range=self.input_expressions[1]["range"],
                # axis_config={"color": WHITE}
            )
        elif len(self.input_expressions) == 3:
            return Axes(
                x_range=self.input_expressions[0]["domain"],
                y_range=self.input_expressions[1]["range"],
                z_range=self.input_expressions[2]["range"],
                # axis_config={"color": WHITE}
            )
        else:
            raise NotImplementedError()


if __name__ == "__main__":
    scene = MathExpressionScene(
        input_expressions=(
            {"symbol": "t", "expression": "t=t", "domain": [-10, 10, 1]},
            {"symbol": "y", "expression": "(t - 2)^2 - 1", "range": [-10, 10, 1]},
            # {"symbol": "y", "expression": "t**2 - 1"},
        )
    )
    scene.render()

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
