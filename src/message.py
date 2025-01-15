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
