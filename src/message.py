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
        name_width: int,
        password_width: int,
        comments_width: int,
    ) -> None:
        id_width = 5
        print(
            termcolor.colored(
                f"{'ID':<{id_width}} {'NAME':<{name_width}} {'PASSWORD':<{password_width}} {'COMMENTS':<{comments_width}}",
                "light_yellow",
            )
        )
        print(
            termcolor.colored(
                f"{id:<{id_width}} {name:<{name_width}} {password:<{password_width}} {comments:<{comments_width}}",
                "light_green",
            ),
        )
