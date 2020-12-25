from datetime import datetime
from enum import Enum, unique
from typing import Any, Dict, List, Optional
import uuid

from pydantic import BaseModel, Field


@unique
class Method(Enum):
    delete = "delete"
    get = "get"
    post = "post"
    put = "put"


@unique
class Role(Enum):
    owner = "owner"
    member = "member"


@unique
class TokenType(Enum):
    bugout = "bugout"
    slack = "slack"
    github = "github"


class BugoutUser(BaseModel):
    id: uuid.UUID = Field(alias="user_id")
    username: str
    email: str
    normalized_email: str
    verified: bool
    autogenerated: bool
    created_at: datetime
    updated_at: datetime


class BugoutUserShort(BaseModel):
    id: uuid.UUID
    username: str
    email: str
    user_type: Role


class BugoutToken(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    active: bool
    token_type: Optional[str]
    note: Optional[str]
    created_at: datetime
    updated_at: datetime


class BugoutUserTokens(BaseModel):
    user_id: uuid.UUID
    username: str
    tokens: List[BugoutToken] = Field(alias="token")


class BugoutGroup(BaseModel):
    id: uuid.UUID
    group_name: Optional[str]
    autogenerated: bool


class BugoutGroupUser(BaseModel):
    group_id: uuid.UUID
    user_id: uuid.UUID
    user_type: str
    autogenerated: Optional[bool] = None
    group_name: Optional[str] = None


class BugoutUserGroups(BaseModel):
    groups: List[BugoutGroupUser]


class BugoutGroupMembers(BaseModel):
    id: uuid.UUID
    name: str
    users: List[BugoutUserShort]


class BugoutJournal(BaseModel):
    id: uuid.UUID
    bugout_user_id: uuid.UUID
    holder_ids: List[uuid.UUID]
    name: str
    created_at: datetime
    updated_at: datetime
