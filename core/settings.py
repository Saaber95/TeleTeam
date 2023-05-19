from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bots: Bots

    API_GPT: str
    API_GGD: str


    TT_oficial: str
    TT_profile: str
    TT_projects: str
    TT_flood: str
    oficial: int
    profile: int
    projects: int
    flood: int

def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        API_GPT =env.str("API_GPT"),
        API_GGD  =env.str("API_GGD"),

        TT_oficial =env.str("TT_oficial"),
        TT_profile =env.str("TT_profile"),
        TT_projects=env.str("TT_projects"),
        TT_flood=env.str("TT_flood"),
        oficial = env.int("oficial"),
        profile= env.int("oficial"),
        projects= env.int("oficial"),
        flood= env.int("oficial"),

        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID")
        )

    )

settings = get_settings('input.ini')
print(settings)