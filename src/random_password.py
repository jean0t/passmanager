import string
import secrets as sc
from src.message import Message
from argparse import ArgumentParser
import os


class Password:
    def __init__(self):
        # avaiable chars to be used in the password
        self.letters_lc = string.ascii_lowercase
        self.letters_uc = string.ascii_uppercase
        self.digits = string.digits
        self.special = string.punctuation

    def _secure_shuffle(self, elements: list) -> list:
        """Helper function used to shuffle the password after it is generated"""
        last_index = len(elements) - 1
        for i in range(last_index, 0, -1):
            j = sc.randbelow(i + 1)
            elements[i], elements[j] = elements[j], elements[i]

        return elements

    def Random_password(
        self, length: int, uppercase=False, lowercase=False, digits=False, special=False
    ) -> str:
        """Generates random password according to the preferrence, guarantees at least 1 character
        from each type if the length is valid"""

        password = []
        all_chars = ""
        if lowercase and len(password) < length:
            password.append(sc.choice(self.letters_lc))
            all_chars += self.letters_lc

        if uppercase and len(password) < length:
            password.append(sc.choice(self.letters_uc))
            all_chars += self.letters_uc

        if digits and len(password) < length:
            password.append(sc.choice(self.digits))
            all_chars += self.digits

        if special and len(password) < length:
            password.append(sc.choice(self.special))
            all_chars += self.special

        for i in range(length - len(password)):
            password.append(sc.choice(all_chars))

        password = self._secure_shuffle(password)

        return "".join(password)

    def Clipboard_copy(self, passwd: str) -> None:
        """Copies the resulting password to the clipboard"""
        try:
            pyperclip.copy(passwd)
            Message.Success("[*] Password Copied to Clipboard")

        except:
            Message.Failure("[!] An Error Occurred When Copying The Password")


def main():
    try:
        # cli argument
        parser = ArgumentParser(prog="Password generator")
        parser.add_argument(
            "-l",
            "--length",
            type=int,
            default=12,
            action="store",
            help="Length of the password",
        )
        parser.add_argument(
            "-lc",
            "--lower-case",
            action="store_true",
            help="Includes lower case letters",
        )
        parser.add_argument(
            "-uc",
            "--upper-case",
            action="store_true",
            help="Includes upper case letters",
        )
        parser.add_argument(
            "-d", "--digits", action="store_true", help="Includes digits"
        )
        parser.add_argument(
            "-s", "--special", action="store_true", help="Includes special characters"
        )
        parser.add_argument(
            "-c",
            "--copy",
            action="store_true",
            help="Copy the password to the clipboard",
        )
        args = parser.parse_args()

        if args.length > 0:
            passwd = Password()
            random_passwd = passwd.Random_password(
                args.length, args.upper_case, args.lower_case, args.digits, args.special
            )

            Message.Success(f"Password: {random_passwd}")

            if args.copy:
                passwd.Clipboard_copy(passwd)
        else:
            Message.Failure(
                "[!] No Password Was Generated, Use --help To See The Options"
            )

    except:
        pass


if __name__ == "__main__":
    main()
