def build_mcp_user_schema(okta_schema, context=None):
    """
    Only returns and describes profile fields for MCP model context.
    """
    # Okta stores user profile fields here:
    profile_props = (
        okta_schema.get("definitions", {})
        .get("profile", {})
        .get("properties", {})
    )
    required_fields = (
        okta_schema.get("definitions", {})
        .get("profile", {})
        .get("required", [])
    )

    mcp_model = {
        "resourceType": "UserProfile",  # Indicates this is just the profile, not the whole user object
        "description": okta_schema.get("title", "Okta User Profile"),
        "context": context or "default",
        "attributes": []
    }

    for name, field in profile_props.items():
        mcp_model["attributes"].append({
            "name": name,
            "type": field.get("type", "string"),
            "required": name in required_fields,
            "description": field.get("title", "") or field.get("description", "") or "",
            "multiValued": field.get("type") == "array"
        })

    # (Optional) Add extra context fields if you use that pattern
    if context == "tenant1":
        mcp_model["attributes"].append({
            "name": "tenant1CustomField",
            "type": "string",
            "required": False,
            "description": "Example tenant1-only custom field",
            "multiValued": False
        })

    return mcp_model

def build_mcp_group_schema(okta_schema, context=None):
    # A stub: Okta doesn't have as rich group schema. Fill as appropriate for your project.
    props = okta_schema["properties"]["profile"]["properties"]
    mcp_model = {
        "resourceType": "Group",
        "description": "Okta Group",
        "context": context or "default",
        "attributes": [
            {"name": k, "type": v["type"], "description": k, "required": False, "multiValued": False}
            for k,v in props.items()
        ]
    }
    return mcp_model