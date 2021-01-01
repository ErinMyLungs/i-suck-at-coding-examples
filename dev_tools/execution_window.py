"""
Holds code examples in http://www.isuckatcoding.net/docs/develpment_environment

Running this file as main will run example_one() and you can call example_two() in the text input.

The malicious code is not meant to be run but included.

"""
import dearpygui.core as c
import dearpygui.simple as s


def example_one():
    """
    Creates window plus execution callback ready to take input commands
    """

    def execute(*_args):
        """
        Executes arbitrary command input in running program
        :param _args: This catches sender and data arguments that we aren't using here
        :return: None, executes command
        """
        command = c.get_value("command##input")
        exec(command)

    with s.window(
        name="command##window",
        autosize=True,
        x_pos=0,
        y_pos=0,
    ):
        c.add_input_text(
            name="command##input",
            width=500,
            height=300,
            multiline=True,
            on_enter=True,
            callback=execute,
        )

    c.start_dearpygui()


def example_two():
    """
    Commands to put into input
    """
    with s.window("Hello World", autosize=True):
        c.add_text("Hello world!")

    c.show_logger()
    c.log_info("Foo")
    c.log_info("Check it out ma - no IDE!")

    with s.window(
        "Canvas", x_pos=0, y_pos=300, autosize=True
    ):
        c.add_drawing("Draw", width=300, height=300)
        c.draw_circle(
            "Draw",
            center=[150, 150],
            radius=50,
            color=[125, 125, 125],
            fill=[125, 125, 200],
        )


def malicious_code():
    """
    THe malicious code that will print out file names
    This is intentionally returned so that people hopefully won't brick their pcs
    """
    return
    from pathlib import Path

    # DON'T RUN THIS
    for file in Path("/").glob("**/*"):
        if file.is_file():
            print(f"{file} is deleted")
            # file.unlink()


import dearpygui.core as c
import dearpygui.simple as s



if __name__ == "__main__":
    example_one()
