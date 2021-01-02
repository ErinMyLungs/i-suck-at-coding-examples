"""
Shows using the dev kit on class-based GUI components
"""
from development_tool_kit import dev
import dearpygui.core as c
import dearpygui.simple as s

class ExampleComponent:


    def __init__(self):
        ...

    execute = lambda self, *args: exec(dev.command)

    @dev.external_log
    def foo(self):
        an_item = "foo"
        return an_item

    def bar(self):
        print('bar')

    def run(self):
        # dev.init_windows(external_exec_command=self.execute)
        dev.init_windows()
        c.start_dearpygui()


if __name__ == '__main__':

    # dev.init_windows(external_exec_command=lambda *args: exec(dev.command))
    ex = ExampleComponent()
    ex.run()