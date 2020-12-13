import logging
from typing import Any, Dict, List, Optional, Tuple

from .calls import make_request
from .data import BugoutGroup, Method

logger = logging.getLogger(__name__)


class GroupNotFound(Exception):
    """
    Raised on actions that involve group which are not present in the database.
    """


class Group:
    """
    Represent a group from Bugout.
    """

    def __init__(self, url) -> None:
        self.url = url

    def _call(self, method: Method, path: str, **kwargs):
        url = f"{self.url.rstrip('/')}/{path.rstrip('/')}"
        result = make_request(method=method, url=url, **kwargs)
        return result

    def get_group(self, group_id: str, token: str) -> BugoutGroup:
        get_group_path = f"groups/{group_id}"
        headers = {
            "Authorization": f"Bearer {token}",
        }
        result = self._call(method=Method.get, path=get_group_path, headers=headers)
        return BugoutGroup(
            id=result.get("id"),
            name=result.get("name"),
            autogenerated=result.get("autogenerated"),
        )
