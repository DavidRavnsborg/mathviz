from mathviz.validate_and_parse import validate_and_parse
from manim import MathTex, Scene, Write
from manim.utils.file_ops import open_file as open_media_file


class MathExpressionScene(Scene):
    def construct(self):
        # Assume input_expr is the user input that has been validated
        input_expr = "x^2 + 3*x + 1"  # Example expression
        parsed_expr = validate_and_parse(input_expr)

        # Convert the sympy expression to a string that Manim can render
        manim_expr = MathTex(str(parsed_expr))

        self.play(Write(manim_expr))
        self.wait(2)


if __name__ == "__main__":
    scene = MathExpressionScene()
    scene.render()  # That's it!

    # Now, open the .mp4 file!
    open_media_file(scene.renderer.file_writer.movie_file_path)
