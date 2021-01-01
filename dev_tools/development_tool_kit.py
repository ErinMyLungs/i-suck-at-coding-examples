"""
The code examples for :
https://www.isuckatcoding,net/docs/development_module/
"""
import dearpygui.core as c
import dearpygui.simple as s

class DevKit:
    def __init__(self, logger=""):
        self.logger = logger
        self.init_windows()


    def init_windows(self):
        self.logger_window()
        self.create_execution_window()
        c.set_main_window_size(1000,800)
        c.set_main_window_pos(x=1120, y=0)

    def execute(*_args):
        """
        Executes arbitrary command input in running program
        :param _args: This catches sender and data arguments that we aren't using here
        :return: None, executes command
        """
        command = c.get_value("command##input")
        exec(command)
    def create_execution_window(self):
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
                callback=self.execute,
            )

    def logger_window(self):
        c.show_logger()

    def log_info(self, message):
        c.log_info(message=message, logger=self.logger)

    def log_debug(self, message):
        c.log_debug(message=message, logger=self.logger)

    def log_warning(self, message):
        c.log_warning(message=message, logger=self.logger)

    def log_error(self, message):
        c.log_error(message=message, logger=self.logger)

    @log
    def test_func(self):
        import random
        random_number = random.randint(0,10)
        print(random_number)
        return random_number


    def run(self):
        c.start_dearpygui()

if __name__ == '__main__':
    dev = DevKit()
    dev.run()
