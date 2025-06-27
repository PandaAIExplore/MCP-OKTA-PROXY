import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OKTA_ORG_URL = os.getenv("OKTA_SCIM_BASE", "")
    OKTA_TOKEN = os.getenv("OKTA_TOKEN", "")
