"""
Shows using the dev kit on class-based GUI components
"""
from development_tool_kit import dev
import dearpygui.core as c
import dearpygui.simple as s

class ExampleComponent:


    def __init__(self):
        ...

    # def execute(self, *_args):
    #     command = c.get_value("command##input")
    #     exec(command)

    @dev.external_log
    def foo(self):
        an_item = "foo"
        return an_item

    def bar(self):
        print('bar')

    def run(self):
        # dev.init_windows(external_exec_command=self.execute)
        # dev.init_windows()
        c.start_dearpygui()


if __name__ == '__main__':
    # def execute(*args):
    #     command = c.get_value("command##input")
    #     exec(command)
    # dev.init_windows(external_exec_command=execute)
    ex = ExampleComponent()
    ex.run()