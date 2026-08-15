from llm.call import execute


def _get_user_input() -> str:
    q = ''
    while not q:
        q = input('ask something: ')
    return q


def main() -> None:
    while True:
        interaction = _get_user_input()
        execute(interaction)


if __name__ == '__main__':
    main()