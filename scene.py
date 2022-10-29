from manim import *
# from manim import Scene, Circle, PINK

class CreateCircle(Scene):  # Scene에서 파생된 클래스 내부에 construct()
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)  # 불투명도
        self.play(Create(circle))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))  # square into circles
        self.play(FadeOut(square))  # 천천히 사라지게

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)  # 오른쪽으로 0.5 간격
        self.play(Create(circle), Create(square))
