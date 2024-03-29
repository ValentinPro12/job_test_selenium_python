import os

from dotenv import load_dotenv

load_dotenv()


class Links:
    REGISTRATION_LINKS = os.getenv("REGISTRATION_LINKS")
    HOST = os.getenv("HOST")
    SITE_MAP_LINK = f'{HOST}/SiteMap.php'
    CONFIG_MAIN_LINK = f'{HOST}/Config/Main.php'
