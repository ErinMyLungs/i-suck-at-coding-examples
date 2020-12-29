""" Shows more complex execution usage"""
from enum import Enum

import dearpygui.core as c
import dearpygui.simple as s


class Direction(str, Enum):
    """
    An enum to indicate which of the 5 line types should be rendered
    """
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    center = "center"


class Number:
    """
    Class for creating a single 'digital' number display
    """

    def __init__(self, color=None):
        self.name = "Canvas"
        if not color:
            self.color = [120, 255, 120]
        else:
            self.color = color

    def clear(self):
        """
        Clears the canvas drawing
        """
        c.clear_drawing(self.name)

    def regular_line(
            self,
            x_offset=0,
            y_offset=0,
            direction: Direction = Direction.left,
            tag: str = None,
    ):
        """
        Creates a line in the number box in the digital clock format
        :param x_offset: x translation magnitude, as x gets larger, the line shifts right
        :param y_offset: y translation magnitude, as y increases the line shifts down
        :param direction: Which type of line to render
        :param tag: string to tag the line with
        :return: drawn polygon on self.canvas
        """
        if tag is None:
            tag = str(direction.value)
        translate = lambda coords: [coords[0] + x_offset, coords[1] + y_offset]

        if direction == Direction.left:
            position = [(0.0, 0.0), (20.0, 20.0), (20.0, 60.0), (0.0, 80.0)]
        elif direction == Direction.up:
            position = [(0.0, 0.0), (20.0, 20.0), (60.0, 20.0), (80.0, 0.0)]
        elif direction == Direction.down:
            position = [(80.0, 20.0), (60.0, 0.0), (20.0, 0.0), (0.0, 20.0)]
        elif direction == Direction.right:
            position = [(20.0, 0.0), (0.0, 20.0), (0.0, 60.0), (20.0, 80.0)]
        else:
            position = [
                (0.0, 10.0),
                (10.0, 0.0),
                (50.0, 0.0),
                (60.0, 10.0),
                (50.0, 20.0),
                (10.0, 20.0),
                (0.0, 10.0),
            ]

        c.draw_polygon(
            self.name,
            points=list(map(translate, position)),
            color=[255, 255, 255, 0],
            fill=self.color,
            tag=tag,
        )

    def execute(self, *_args):
        """
        Our execution callback again
        :param _args: catching sender/data
        :return: executed command
        """
        command = c.get_value("command##input")
        exec(command)

    def run(self):
        """
        A very basic stand-aloen run method to show what this looks like by default
        :return: General number display example
        """

        window_args = dict(
            autosize=False,
            height=200,
            width=200,
            x_pos=0,
            y_pos=0,
        )
        with s.window("Drawing", **window_args):
            c.add_drawing(self.name, width=90, height=150, )

        with s.window("command##window", autosize=True, y_pos=200, x_pos=0):
            c.add_input_text(name="command##input", width=600, height=300, multiline=True, on_enter=True,
                             callback=self.execute)

        c.start_dearpygui()


if __name__ == '__main__':
    num = Number()
    num.run()
