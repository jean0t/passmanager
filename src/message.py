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
    def Query_result(id: int, name: str, password: str, comments: str):
        print(termcolor.colored("id:\t", "light_yellow"), termcolor.colored(f"{id}", "light_green"))
        print(termcolor.colored("name:\t", "light_yellow"), termcolor.colored(f"{name}", "light_green"))
        print(termcolor.colored("password:\t", "light_yellow"), termcolor.colored(f"{password}", "light_green"))
        print(termcolor.colored("comments:\n\t", "light_yellow"), termcolor.colored(f"{comments}", "light_green"))
