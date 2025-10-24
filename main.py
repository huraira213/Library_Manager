from db.connection import initialize_database
from ui.manu import user_manu


def main():
    initialize_database()
    user_manu()


if __name__ == '__main__':
    main()

