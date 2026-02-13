from stationeers_pytrapic.symbols import *

# Available compiler options
# name              Default    Description
# compact           False      labels, evaluates hashes (if shorter), use numbers for logic types etc.,
#                              also implies remove-labels and inline-functions
# inline-functions  True       Inline function calls if possible
# remove-labels     False      removes jump labels
# append-version    True       add comment with PyTrapIC version

# Usage is demonstated below. Prepend "no-" for negating options.
# The options can appear anywhere in the code and will be applied globally.

# pytrapic: compact
# pytrapic: no-append-version
# pytrapic: no-inline-functions


def some_function():
    display = ConsoleLED1x2(d0)
    display.Mode = DisplayMode.String
    display.Setting = STR("Hi")


while True:
    some_function()
