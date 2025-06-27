from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from app.okta_client import (
    get_user_schema, get_group_schema,
    get_user, list_users, get_group, list_groups
)
from .context_models import (
    build_mcp_user_schema, build_mcp_group_schema
)

app = FastAPI(title="Okta MCP Proxy")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/model-context/describe")
def describe(resource: str = Query("User"), tenant: str = Query(None)):
    if resource.lower() == "user":
        okta_schema = get_user_schema()
        model = build_mcp_user_schema(okta_schema, context=tenant)
        return model
    elif resource.lower() == "group":
        okta_schema = get_group_schema()
        model = build_mcp_group_schema(okta_schema, context=tenant)
        return model
    else:
        return JSONResponse({"error": f"Unknown resource '{resource}'"}, status_code=404)

@app.get("/users")
def users():
    return list_users()

@app.get("/users/{user_id}")
def user_detail(user_id: str):
    return get_user(user_id)

@app.get("/groups")
def groups():
    return list_groups()

@app.get("/groups/{group_id}")
def group_detail(group_id: str):
    return get_group(group_id)