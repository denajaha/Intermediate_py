def add_wrapping_with_style(style):
    def add_wrapping(item):
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style, str(item()))

        return wrapped_item

    return add_wrapping


@add_wrapping_with_style('beautifully')
def new_gpu():
    return 'a new tesla p100 GPU'


# @add_wrapping_with_style
def new_bicycle():
    return 'a new bicycle'


print(new_gpu())
# print(new_bicycle())
