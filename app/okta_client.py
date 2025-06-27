import requests
from app.config import Settings

BASE = Settings.OKTA_ORG_URL.rstrip("/")
HEADERS = {
    "Authorization": Settings.OKTA_TOKEN,
    "Accept": "application/json"
}

def get_user_schema():
    url = f"{BASE}/api/v1/meta/schemas/user/default"  # For Okta Classic
    resp = requests.get(url, headers=HEADERS, verify=False)
    resp.raise_for_status()
    return resp.json()

def get_group_schema():
    # Okta does not always have detailed group schema but here is a basic
    return {
        "id": "group",
        "name": "Group",
        "properties": {
            "id": {"type": "string"},
            "profile": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"}
                }
            }
        }
    }

def get_user(user_id):
    url = f"{BASE}/api/v1/users/{user_id}"
    resp = requests.get(url, headers=HEADERS, verify=False)
    resp.raise_for_status()
    return resp.json().get("profile")

def list_users():
    url = f"{BASE}/api/v1/users"
    resp = requests.get(url, headers=HEADERS, verify=False)
    resp.raise_for_status()
    return resp.json()

def get_group(group_id):
    url = f"{BASE}/api/v1/groups/{group_id}"
    resp = requests.get(url, headers=HEADERS, verify=False)
    resp.raise_for_status()
    return resp.json()

def list_groups():
    url = f"{BASE}/api/v1/groups"
    resp = requests.get(url, headers=HEADERS, verify=False)
    resp.raise_for_status()
    return resp.json()