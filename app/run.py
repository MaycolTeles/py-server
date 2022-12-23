"""
Run module. This is where the application starts.
"""

from src import Server


def main() -> None:
    """
    Main function. This is where the application starts.
    """
    server = Server()
    server.start()
    server.shut_down()


if __name__ == "__main__":
    main()
