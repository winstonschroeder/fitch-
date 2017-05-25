import gettext
#en = gettext.translation(None, localedir='locale', languages=['en'])
#en.install()

import sys
import os

import appinfo
import app


def parse_commandline():
    """Parses the command line; returns options and filenames.
    If --version, --help or invalid options were given, the application will
    exit.
    """
    import argparse
#    argparse._ = _ # let argparse use our translations
    parser = argparse.ArgumentParser(conflict_handler="resolve",
        description = "{description}".format(description=appinfo.description))
    parser.add_argument('-v', '--version', action="version",
        version="{0} {1}".format(appinfo.appname, appinfo.version),
        help="show program's version number and exit")
    parser.add_argument('-V', '--version-debug', action="store_true", default=False,
        help="show version numbers of {appname} and its supporting modules "
               "and exit".format(appname=appinfo.appname))

    # Make sure debugger options are recognized as valid. These are passed automatically
    # from PyDev in Eclipse to the inferior process.
    if "pydevd" in sys.modules:
        parser.add_argument('--vm_type', '-v')
        parser.add_argument('-a', '--client')
        parser.add_argument('-p', '--port')
        parser.add_argument('-f', '--file')
        parser.add_argument('-o', '--output')
    args = [os.path.abspath(sys.argv[0])] + sys.argv[1:]
    if os.name == 'nt':
        while args:
            if os.path.basename(args[0]).lower().startswith(appinfo.name):
                break
            args.pop(0)
    return parser.parse_args(args[1:])

def main():
    """Main function."""
    args = parse_commandline()

    if args.version_debug:
        import debuginfo
        sys.stdout.write(debuginfo.version_info_string() + '\n')
        sys.exit(0)

