# Coding Examples for I Suck at Coding writups

This repo holds all the code examples for [isuckatcoding.net](https://www.isuckatcoding.net).

Shockingly this is also exactly why the pyproject.toml has an absurd line-length of 58 - so that code written will be broken up to fit in a single column for ease of reading. side-by-side with an editor.

## Contents

### Development Tools - `./dev_tools`

#### [Making a Live Dev Environment in DPG](https://www.isuckatcoding.net/docs/development_environment/)

[First section code](https://www.isuckatcoding.net/docs/development_environment/#code):
* `./dev_tools/execution_window.py`
  * `example_one` creates execution window
  * `example_two` are commands to write in window from `example_one`
  * `malicious_code` is an example of `exec` as a security flaw

[A More Complex Example](https://www.isuckatcoding.net/docs/development_environment/#a-more-complex-example)
* `./dev_tools/more_complex_execution.py`
  * `Direction` - a simple enum class for selecting shape direction
  * `Number` a 'digital' drawn display with execution window built in

#### [Creating a Dev Tool Module for DPG](https://www.isuckatcoding.net/docs/development_module/)
* `./dev_tools/development_tool_kit.py`
  * Dev kit class with execution window, logger, and helper methods