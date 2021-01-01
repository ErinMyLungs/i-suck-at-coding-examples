"""
The code examples for :
https://www.isuckatcoding,net/docs/development_module/
"""
import functools
import typing as ty

import dearpygui.core as c
import dearpygui.simple as s


class DevKit:
    def __init__(
        self,
        logger: str = "",
        exec_command = None
    ):
        self.logger = logger
    def internal_log(func):
        """
        An internal class log decorator that dumps a function
        return value into the logger.

        This requires the function to be within the class itself.
        """

        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self.log_info(result)
            return result

        return wrap

    def external_log(self, func):
        """
        An external decorator for dumping a function
        return value into the decorator.

        This works for all functions outside of the class
        """

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            self.log_info(result)
            return result

        return wrap

    def init_windows(self, external_exec_command=None):
        """
        Creates and arranges our windows for the kit
        """
        self.logger_window()
        self.create_execution_window(exec_command=external_exec_command)
        c.set_main_window_size(1000, 850)
        c.set_main_window_pos(x=2400, y=0)

    def execute(self, *_args):
        """
        Executes arbitrary command input in running program
        :param _args: This catches sender and data arguments
         that we aren't using here
        :return: None, executes command
        """
        command = c.get_value("command##input")
        exec(command)

    def create_execution_window(self, exec_command = None):
        """
        Creates execution window with execute callback
        """
        callback = self.execute if exec_command is None else exec_command
        with s.window(
            name="command##window",
            autosize=True,
            x_pos=485,
            y_pos=0,
        ):
            c.add_input_text(
                name="command##input",
                width=500,
                height=300,
                multiline=True,
                on_enter=True,
                callback=callback
            )

    def logger_window(self):
        """
        Right now we use just a basic c.show_logger
        """
        with s.window(
            name=self.logger.replace("_", " ").title()
            + "##window",
            width=500,
            height=500,
            x_pos=500,
            y_pos=350,
            no_scrollbar=True,
        ):
            c.add_logger(
                name=self.logger,
                autosize_x=True,
                autosize_y=True,
            )

    def log(self, message):
        """
        Convenience method because log_info
        is just too many letters to type.
        """
        self.log_info(message=message)

    def log_info(self, message):
        """
        Logs at info level
        """
        c.log_info(message=message, logger=self.logger)

    def log_debug(self, message):
        """
        Logs at debug level
        """
        c.log_debug(message=message, logger=self.logger)

    def log_warning(self, message):
        """
        Logs at warning level
        """
        c.log_warning(
            message=message, logger=self.logger
        )

    def log_error(self, message):
        """
        Logs at error level
        """
        c.log_error(message=message, logger=self.logger)

    @internal_log
    def internal_log_example(self):
        print("A result")
        return "A result"

    def run(self):
        """
        Simple run method
        """
        self.init_windows()
        c.start_dearpygui()

dev = DevKit('an_example_logger')
if __name__ == "__main__":
    @dev.external_log
    def external_log_example():
        """
        A test function to log and wrap
        """
        import random

        random_number = random.randint(0, 10)
        print(random_number)
        return random_number

    dev.run()
