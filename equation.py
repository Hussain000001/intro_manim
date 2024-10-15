from manim import *

class QuadraticEquationAsAreas(Scene):
    def construct(self):
        # Create the title
        title = Text("Modeling a Quadratic Equation as Areas").scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Quadratic equation to model: x^2 + 3x + 2 = 0
        equation = MathTex("x^2", "+", "3x", "+", "2", "= 0").scale(0.8)
        equation.next_to(title, DOWN)
        self.play(Write(equation))

        # Square for x^2
        square_x2 = Square(side_length=2, color=BLUE)
        label_x2 = MathTex("x^2").move_to(square_x2.get_center())
        
        self.play(Create(square_x2), Write(label_x2))
        self.wait(1)

        # Rectangles for 3x (we'll use three rectangles)
        rect_1x = Rectangle(width=1, height=2, color=GREEN)
        rect_2x = rect_1x.copy().next_to(rect_1x, RIGHT, buff=0)
        rect_3x = rect_2x.copy().next_to(rect_2x, RIGHT, buff=0)
        rects = VGroup(rect_1x, rect_2x, rect_3x).next_to(square_x2, RIGHT, buff=0)

        labels_3x = VGroup(
            MathTex("x").move_to(rect_1x.get_center()),
            MathTex("x").move_to(rect_2x.get_center()),
            MathTex("x").move_to(rect_3x.get_center())
        )

        self.play(Create(rects), Write(labels_3x))
        self.wait(1)

        # Square for constant '2'
        small_square = Square(side_length=1, color=RED).next_to(rects, RIGHT, buff=0)
        label_const = MathTex("2").move_to(small_square.get_center())
        
        self.play(Create(small_square), Write(label_const))
        self.wait(1)

        # Show that areas combine to represent quadratic equation visually
        group = VGroup(square_x2, rects, small_square).center()
        self.play(group.animate.center())

        # Summarize
        final_equation = MathTex("x^2", "+", "3x", "+", "2", "= 0").next_to(group, DOWN)
        self.play(Write(final_equation))
        
        self.wait(2)
