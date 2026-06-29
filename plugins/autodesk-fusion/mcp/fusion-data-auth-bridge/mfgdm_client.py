from __future__ import annotations

from typing import Any
from urllib import request, error
import json

from schemas import BridgeConfig, blocked, ok


class MFGDMClient:
    def __init__(self, config: BridgeConfig, token_getter):
        self.config = config
        self.token_getter = token_getter

    def _graphql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        if not self.config.mfgdm_graphql_url:
            return blocked(
                "mfgdm_endpoint_not_configured",
                "Set mfgdm_graphql_url in local bridge config after confirming the official Autodesk MFGDM GraphQL endpoint and schema."
            )
        token = self.token_getter()
        if not token:
            return blocked("missing_access_token", "Run bridge login before MFGDM queries.")
        body = json.dumps({"query": query, "variables": variables}).encode()
        req = request.Request(
            self.config.mfgdm_graphql_url,
            data=body,
            method="POST",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"}
        )
        try:
            with request.urlopen(req, timeout=self.config.request_timeout_sec) as resp:
                return ok({"status": resp.status, "data": json.loads(resp.read().decode())})
        except error.HTTPError as exc:
            detail = exc.read().decode(errors="replace")[:1200]
            return blocked("mfgdm_http_error", "Check endpoint, schema, scopes, project permissions, and token audience.", status=exc.code, detail=detail)
        except Exception as exc:  # noqa: BLE001
            return blocked("mfgdm_request_failed", str(exc))

    def design_summary(self, design_id: str) -> dict[str, Any]:
        if not design_id:
            return blocked("missing_design_id")
        query = "query DesignSummary($id: ID!) { node(id: $id) { id __typename } }"
        return self._graphql(query, {"id": design_id})

    def component_hierarchy(self, design_id: str) -> dict[str, Any]:
        if not design_id:
            return blocked("missing_design_id")
        query = "query ComponentHierarchy($id: ID!) { node(id: $id) { id __typename } }"
        return self._graphql(query, {"id": design_id})
