"""
Shows using the dev kit on class-based GUI components
"""
import dearpygui.core as c
import dearpygui.simple as s
from development_tool_kit import dev


class ExampleComponent:
    """
    An example component to debug a table + graph
    """

    """
    We set this here so that the execute scope
    has full access to the ExampleComponent state
    and methods.
    """
    execute = lambda self, *args: exec(dev.command)

    def __init__(self):
        self.table_data = [[0, 0, 0], [1, 10, 20]]
        self.labels = ["idx", "x_val", "y_val"]
        self._table_name = "Example Table"
        self._plot_name = "Example Plot"

    @property
    def x_values(self):
        """
        Simple helper to extract x values from data
        :return: list of x values
        """
        return [val[1] for val in self.table_data]

    @property
    def y_values(self):
        """
        Simple helper to extract y values from data
        :return: list of y values
        """
        return [val[-1] for val in self.table_data]

    @dev.log_return
    def recalculate_plot_limits(self):
        """
        A simple method to recalculate plot limits
        with a padding of largest value //10
        :return: x_lim kwargs and y_lim kwargs as dicts
        """
        x_min = min(self.x_values)
        x_max = max(self.x_values)
        y_min = min(self.y_values)
        y_max = max(self.y_values)

        padding = max(
            [
                x_min // 10,
                x_max // 10,
                y_min // 10,
                y_max // 10,
            ],
            key=lambda val: abs(val),
        )

        x_limits = {
            "xmin": x_min - padding,
            "xmax": x_max + padding,
        }
        y_limits = {
            "ymin": y_min - padding,
            "ymax": y_max + padding,
        }
        # We return this to showcase the @dev.log_return decorator
        # It would likely be smarter to have the limits set in here
        return x_limits, y_limits

    def update_data(self):
        """
        Updates data in table and plot
        """
        dev.log_debug("Called update data")
        # Setting table data
        c.set_table_data(
            self._table_name, data=self.table_data
        )

        # Clearing plot and setting new scatter plot
        c.clear_plot(self._plot_name)
        c.add_scatter_series(
            self._plot_name,
            name="Example Scatter",
            x=self.x_values,
            y=self.y_values,
        )
        # Updating plot limits
        x_lim, y_lim = self.recalculate_plot_limits()
        c.set_plot_xlimits(self._plot_name, **x_lim)
        c.set_plot_ylimits(self._plot_name, **y_lim)

    def add_data_option(self, sender, data):
        """
        Creates the data input window for the add data window
        """

        with s.window(
            "Add Data Window",
            autosize=True,
            x_pos=0,
            y_pos=350,
        ):
            # Title text
            c.add_text("Add a new data row:")
            c.add_text(
                name=f"Idx: \t{len(self.table_data)}",
                tip="This is created automatically",
            )
            # Text divider
            c.add_text("-" * 30)
            # input sliders
            c.add_slider_int(name=": x_val")
            c.add_slider_int(name=": y_val")

            # Action buttons
            c.add_button(
                "Cancel",
                callback=lambda *args: c.delete_item(
                    "Add Data Window"
                ),
            )
            c.add_same_line()
            c.add_button(
                "Add Row", callback=self.save_new_row
            )

    def save_new_row(self, sender, data):
        """
        Appends data from Add Data Window to table data
        and closes window
        """
        dev.log_debug("Adding new row -")
        self.table_data.append(
            [
                len(self.table_data),
                c.get_value(": x_val"),
                c.get_value(": y_val"),
            ]
        )
        self.update_data()
        c.delete_item("Add Data Window")

    @dev.log_all
    def reset_data(self, sender, data):
        """
        Resets table data to default values
        """
        self.table_data = [[0, 0, 0], [1, 10, 20]]
        self.update_data()

    def _create_menu(self):
        """
        Creates menu with add and reset data options
        """
        with s.menu_bar("MenuBar"):
            with s.menu("Data Operations"):
                c.add_menu_item(
                    "Add Data",
                    callback=self.add_data_option,
                )

                c.add_menu_item(
                    "Reset Data",
                    callback=self.reset_data,
                )

    def create_component(self):
        """
        Creates window with structure for component.
        Used when combining with multiple components
        before running c.start_dearpygui()
        """
        with s.window(
            "Example Component",
            width=485,
            height=335,
            x_pos=0,
            y_pos=0,
        ):
            self._create_menu()
            c.add_table(
                self._table_name,
                headers=self.labels,
                width=200,
            )
            c.add_same_line()
            c.add_plot(
                self._plot_name,
                width=200,
                height=200,
                no_legend=True,
            )
            self.update_data()

    def run(self):
        """
        Creates component and starts DearPyGui.
        """

        self.create_component()
        c.start_dearpygui()


if __name__ == "__main__":
    INTERNAL_SCOPE = True

    ex = ExampleComponent()

    if INTERNAL_SCOPE is True:
        """
        Here we set the execution command to be the
        internal execute command we defined in
        ExampleComponent.

        We can execute commands using self instead of ex
        """

        dev.init_windows(
            external_exec_command=ex.execute
        )
    else:
        """
        if we set the execution command here we could access
        the ExampleComponent as the ex variable instead of
        as self. Good for multi-component debugging
        """
        execute = lambda *args: exec(dev.command)
        dev.init_windows(external_exec_command=execute)

    ex.run()
