"""
The code examples for :
https://www.isuckatcoding,net/docs/development_module/
"""
import functools

import dearpygui.core as c
import dearpygui.simple as s


class DevKit:
    def __init__(
        self,
        logger: str = "",
    ):
        self.logger = logger

    def log_return(self, func):
        """
        An external decorator for dumping a function
        return value into the logger.
        """

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            self.log_info(
                f"{func.__name__} return value:"
            )
            self.log_info(result)
            self.log_info("-" * 20)
            return result

        return wrap

    def log_function(self, func):
        """
        A decorator for dumping a function's
        arguments and result into a logger
        """

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            name = func.__name__

            # Logging Arguments
            self.log_info(f"{name} Arguments:")
            for argument in args:
                self.log(f"\t{argument}")

            # Logging kwargs if exist
            if len(kwargs) > 0:
                self.log(f"{name} Key Word Arguments:")
                for key, value in kwargs.items():
                    self.log(f"\t {key} : {value}")

            # Logging Return Value
            result = func(*args, **kwargs)
            self.log(f"{name} Return Value:")
            self.log(f"\t{result}")
            self.log("-" * 20)
            return result

        return wrap

    def init_windows(self, external_exec_command=None):
        """
        Creates and arranges our windows for the kit
        """
        self.logger_window()
        self.create_execution_window(
            exec_command=external_exec_command
        )
        c.add_debug_window(
            "Debugger", x_pos=0, y_pos=350, width=500
        )
        c.end()
        c.set_main_window_size(1000, 850)
        c.set_main_window_pos(x=280, y=0)

    @property
    def command(self) -> str:
        """
        A simple property to make fetching command
        input way easier.
        :return: String of command to exec
        """
        return c.get_value("command##input")

    def execute(self, *_args):
        """
        Executes arbitrary command input in running program
        :param _args: This catches sender and data arguments
         that we aren't using here
        :return: None, executes command
        """
        exec(self.command)

    def create_execution_window(self, exec_command=None):
        """
        Creates execution window with execute callback
        """
        callback = (
            self.execute
            if exec_command is None
            else exec_command
        )
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
                callback=callback,
            )

    def logger_window(self):
        """
        Creating our logger window
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

    def run(self, external_exec_command=None):
        """
        Simple run method
        """
        self.init_windows(
            external_exec_command=external_exec_command
        )
        c.start_dearpygui()


dev = DevKit("an_example_logger")
if __name__ == "__main__":

    @dev.log_return
    def external_log_example():
        """
        This picks a random number, prints it in console
        and returns the picked value.

        You should be able to see the same value in console
        and in the logger.
        """
        import random

        random_number = random.randint(0, 10)
        print(random_number)
        return random_number

    @dev.log_function
    def echo_scream(string_to_echo, scream=True):
        """
        An example function to show args/Kwargs
        :param string_to_echo: string to echo back
        :param scream: if True run .upper() on string
        :return: string echoed response
        """
        if scream is True:
            string_to_echo = string_to_echo.upper()
        print(string_to_echo)
        return string_to_echo

    dev.run()
