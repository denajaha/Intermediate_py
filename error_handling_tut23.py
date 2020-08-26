import sys  # we can access traceback of the error
import logging

def error_handling():
    print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))


try:
    a + b
except Exception as e:

    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
    # the same thing but much more useful and nicely written in terminal output
    print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

# using function from above
print('using function')
try:
    a + b
except Exception as e:
    logging.error(error_handling())

