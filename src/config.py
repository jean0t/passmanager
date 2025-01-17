from pathlib import Path


class Config:
    app_path = Path().home() / ".passmng"
    database_path = app_path / "database.db"

    @staticmethod
    def configure_environment(app_path):
        if not Path(app_path.__str__()).exists():
            Path(app_path).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    Config.configure_environment(Config.app_path)
