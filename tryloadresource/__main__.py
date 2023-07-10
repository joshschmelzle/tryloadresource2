import sys
from . import app


def main():
    app.run()


def init():
    """Handle main init."""
    if __name__ == "__main__":
        main()
        sys.exit(0)


init()
