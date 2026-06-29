from __future__ import annotations

from typing import Any
from urllib import request, parse, error
import json

from schemas import BridgeConfig, blocked, ok


class APSClient:
    def __init__(self, config: BridgeConfig, token_getter):
        self.config = config
        self.token_getter = token_getter

    def _request_json(self, path: str) -> dict[str, Any]:
        token = self.token_getter()
        if not token:
            return blocked("missing_access_token", "Run auth_status/start_login/complete_login_if_needed first.")
        url = self.config.api_base_url.rstrip("/") + path
        req = request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/json"})
        try:
            with request.urlopen(req, timeout=self.config.request_timeout_sec) as resp:
                raw = resp.read().decode()
                return ok({"url": url, "status": resp.status, "data": json.loads(raw) if raw else None})
        except error.HTTPError as exc:
            detail = exc.read().decode(errors="replace")[:1200]
            return blocked("aps_http_error", "Check Autodesk scopes, hub/project permissions, and token audience.", url=url, status=exc.code, detail=detail)
        except Exception as exc:  # noqa: BLE001
            return blocked("aps_request_failed", str(exc), url=url)

    def list_hubs(self) -> dict[str, Any]:
        return self._request_json("/project/v1/hubs")

    def list_projects(self, hub_id: str) -> dict[str, Any]:
        if not hub_id:
            return blocked("missing_hub_id")
        return self._request_json(f"/project/v1/hubs/{parse.quote(hub_id, safe='')}/projects")

    def list_top_folders(self, hub_id: str, project_id: str) -> dict[str, Any]:
        if not hub_id or not project_id:
            return blocked("missing_hub_or_project_id")
        return self._request_json(f"/project/v1/hubs/{parse.quote(hub_id, safe='')}/projects/{parse.quote(project_id, safe='')}/topFolders")

    def list_folder_contents(self, project_id: str, folder_id: str) -> dict[str, Any]:
        if not project_id or not folder_id:
            return blocked("missing_project_or_folder_id")
        return self._request_json(f"/data/v1/projects/{parse.quote(project_id, safe='')}/folders/{parse.quote(folder_id, safe='')}/contents")

    def get_item_versions(self, project_id: str, item_id: str) -> dict[str, Any]:
        if not project_id or not item_id:
            return blocked("missing_project_or_item_id")
        return self._request_json(f"/data/v1/projects/{parse.quote(project_id, safe='')}/items/{parse.quote(item_id, safe='')}/versions")

    def get_version_metadata(self, project_id: str, version_id: str) -> dict[str, Any]:
        if not project_id or not version_id:
            return blocked("missing_project_or_version_id")
        return self._request_json(f"/data/v1/projects/{parse.quote(project_id, safe='')}/versions/{parse.quote(version_id, safe='')}")
