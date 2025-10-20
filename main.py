from db.connection import create_table
from ui.manu import main_manu


def main():
    create_table()
    main_manu()


if __name__ == '__main__':
    main()

