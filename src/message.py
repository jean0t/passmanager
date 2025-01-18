import termcolor


class Message:
    @staticmethod
    def Success(message: str) -> None:
        print(termcolor.colored(message, "light_green"))

    @staticmethod
    def Failure(message: str) -> None:
        print(termcolor.colored(message, "red"))

    @staticmethod
    def Info(message: str) -> None:
        print(termcolor.colored(message, "light_yellow"))

    @staticmethod
    def Query_result(
        id: int,
        name: str,
        password: str,
        comments: str,
    ) -> None:
        print(
            termcolor.colored("ID:\n", "light_yellow"),
            termcolor.colored(str(id), "light_green"),
        )
        print(
            termcolor.colored("NAME:\n", "light_yellow"),
            termcolor.colored(name, "light_green"),
        )
        print(
            termcolor.colored("PASSWORD:\n", "light_yellow"),
            termcolor.colored(password, "light_green"),
        )
        print(
            termcolor.colored("COMMENTS:\n", "light_yellow"),
            termcolor.colored(comments, "light_green"),
        )
