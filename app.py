import dataclasses
from typing import NamedTuple, List
from collections import deque

import streamlit as st
from matplotlib import pyplot as plt


MAX_POINTS = 1000


class Point(NamedTuple):
    x: int
    y: int
    color: str


@st.cache(allow_output_mutation=True)
def get_points() -> deque:
    return deque()

# will persist
points = get_points()

while len(points) > MAX_POINTS:
    points.popleft()

COLORS = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "white"]

raw = st.text_input("enter point: x, y, each should be between 0 and 100")
color = st.selectbox("color", COLORS)

if st.button("add point"):
    try:
        x, y = raw.split(",")
        x = float(x)
        y = float(y)
        c = 'k' if color == "black" else color[0]

        if 0 <= x <= 100 and 0 <= y <= 100:
            points.append(Point(float(x), float(y), c))
        else:
            st.write("x and y should both be between 0 and 100")
    except ValueError:
        st.write("please enter your point like: 1, 2")

if points:
    xs, ys, cs = zip(*points)
    fig, ax = plt.subplots()
    ax.scatter(xs, ys, c=cs)
    st.pyplot(fig)
