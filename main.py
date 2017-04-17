#!/usr/bin/python3
import os.path


def globals_in_place():
    return os.path.isfile(".friends_shutdown_cache.txt")


def setup_globals():
    global_user_path = input("Where is friends directory?")
    with open(".friends_shutdown_cache.txt", "w") as f:
       f.write(global_user_path)
    """
       check_user_path()
       f.write(where to start)
    """


def load_next_to_play():
    pass


def update_next_to_play():
    pass


def shutdown_in(mins):
    pass


def start_friends():
    pass


def main():
    # Check if globals are in place
    """
    if not globals_in_place():
        setup_globals()
    """
    # Load specific data

    # Update data

    # Send shutdown

    # Start friends
    globals_in_place()
    setup_globals()
    globals_in_place()


if __name__ == "__main__":
    main()
