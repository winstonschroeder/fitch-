import sys, os

def run():
	""" run app """
	return 0

def instantiate():
    args = [os.path.abspath(sys.argv[0])] + sys.argv[1:]
    if sys.version_info >= (3, 0):
        args = list(map(os.fsencode, args))

def excepthook(exctype, excvalue, exctb):
	"""Called when a Python exception goes unhandled."""
	from traceback import format_exception
	sys.stderr.write(''.join(format_exception(exctype, excvalue, exctb)))
