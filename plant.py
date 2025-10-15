#!/usr/bin/env python3
"""
Fractal plant (L‑system) – Task 4 helper script.

Usage:
  python plant.py --iters 5 --angle 25 --step 6

Keys in the grammar:
  F: draw forward
  f: move forward without drawing
  +: turn right by <angle> degrees
  -: turn left by <angle> degrees
  [: push state (position, heading, pen size)
  ]: pop state
  X: non-drawing symbol used in productions

Default rules = classic “fractal plant”:
  axiom: X
  rules:
    X -> F+[[X]-X]-F[-FX]+X
    F -> FF
  angle: 25°

You can tweak --iters (depth), --angle and --step to suit your screen.
"""

from __future__ import annotations
import argparse
import turtle
from dataclasses import dataclass
from typing import Dict, Tuple, List

@dataclass
class LSystem:
    axiom: str
    rules: Dict[str, str]

    def derive(self, n: int) -> str:
        s = self.axiom
        for _ in range(n):
            s = ''.join(self.rules.get(ch, ch) for ch in s)
        return s

def draw_turtle(program: str, *, angle: float = 25.0, step: float = 6.0) -> None:
    # Fast drawing
    turtle.tracer(False, 0)
    t = turtle.Turtle(visible=False)
    t.speed(0)
    t.penup()
    # Start near bottom center, pointing up
    t.setheading(90)
    t.setpos(0, -turtle.window_height() // 2 + 20)
    t.pendown()

    stack: List[Tuple[Tuple[float, float], float, int]] = []  # (pos, heading, pensize)
    t.pensize(2)

    for ch in program:
        if ch in ('F', 'G'):
            t.forward(step)
        elif ch == 'f':
            t.penup(); t.forward(step); t.pendown()
        elif ch == '+':
            t.right(angle)
        elif ch == '-':
            t.left(angle)
        elif ch == '[':
            stack.append((t.position(), t.heading(), t.pensize()))
            # Optional: taper branches a bit
            t.pensize(max(1, t.pensize() - 1))
        elif ch == ']':
            if stack:
                pos, heading, width = stack.pop()
                t.penup()
                t.setpos(pos); t.setheading(heading); t.pensize(width)
                t.pendown()
        # X and others: no drawing action

    turtle.update()
    # Keep window open until clicked
    turtle.Screen().exitonclick()

def main():
    parser = argparse.ArgumentParser(description="Draw a fractal plant using an L-system.")
    parser.add_argument("--iters", type=int, default=5, help="Number of derivation steps (depth).")
    parser.add_argument("--angle", type=float, default=25.0, help="Turn angle in degrees.")
    parser.add_argument("--step", type=float, default=6.0, help="Forward step length in pixels.")
    args = parser.parse_args()

    # Classic fractal plant grammar
    system = LSystem(
        axiom="X",
        rules={
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF",
        },
    )

    # Generate command string and draw
    program = system.derive(args.iters)
    draw_turtle(program, angle=args.angle, step=args.step)

if __name__ == "__main__":
    main()
