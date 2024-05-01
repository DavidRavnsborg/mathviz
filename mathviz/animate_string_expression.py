from mathviz.validate_and_parse import validate_and_parse
from manim import (
    ThreeDAxes,
    ThreeDScene,
    MathTex,
    ParametricFunction,
    Write,
    RED,
    BLUE,
    WHITE,
)
from manim.utils.file_ops import open_file as open_media_file
import numpy as np
from sympy import symbols, lambdify
from typing import Mapping, Tuple


class MathExpressionScene(ThreeDScene):
    """Take a text expression, converts it to a sympify expression, converts that to a function,
    and renders it with manim."""

    def __init__(self, input_expressions: Tuple[Mapping]):
        if len(input_expressions) < 2:
            print(input_expressions)
            raise Exception("Not enough input expressions.")
        elif len(input_expressions) > 3:
            print(input_expressions)
            raise Exception("Too many input expressions.")
        self.input_expressions = input_expressions
        super().__init__()

    def construct(self):
        indepedent_var = symbols(self.input_expressions[0]["symbol"])
        funcs = []

        axes = self.get_axes()
        self.add(axes)
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
        curve = axes.plot_parametric_curve(
            function=self.get_parametric_lambda(funcs),
            t_range=[
                self.input_expressions[0]["domain"][0],
                self.input_expressions[0]["domain"][1],
            ],
            color=RED,
        )
        self.play(Write(curve), run_time=5)
        self.wait(2)

    def get_parametric_lambda(self, funcs):
        """Returns a function with the appropriate number of dimensions. i is the independent
        variable in the first dimension (the canonical indepdent/x-axis)."""
        if len(funcs) == 1:
            return lambda i: np.array([i, funcs[0](i), 0])
        elif len(funcs) == 2:
            return lambda i: np.array([i, funcs[0](i), funcs[1](i)])
        else:
            raise NotImplementedError()

    def get_axes(self):
        if len(self.input_expressions) == 2:
            return ThreeDAxes(
                x_range=self.input_expressions[0]["domain"],
                y_range=self.input_expressions[1]["range"],
                axis_config={"color": WHITE},
            )
        elif len(self.input_expressions) == 3:
            return ThreeDAxes(
                x_range=self.input_expressions[0]["domain"],
                y_range=self.input_expressions[1]["range"],
                z_range=self.input_expressions[2]["range"],
                axis_config={"color": WHITE},
            )
        else:
            raise NotImplementedError()


if __name__ == "__main__":
    scene = MathExpressionScene(
        input_expressions=(
            {"symbol": "t", "expression": "t=t", "domain": [-10, 15, 1]},
            {"symbol": "y", "expression": "(t - 2)^2 - 1", "range": [-10, 10, 1]},
        )
    )
    scene.render()

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
