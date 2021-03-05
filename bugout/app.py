from typing import Any, Dict, List, Optional, Union
import uuid

from . import data
from .calls import ping
from .group import Group
from .journal import Journal
from .user import User
from .settings import BUGOUT_BROOD_URL, BUGOUT_SPIRE_URL, REQUESTS_TIMEOUT


class InvalidParameters(ValueError):
    """
    Raised when provided invalid parameters.
    """


class Bugout:
    def __init__(
        self,
        brood_api_url: str = BUGOUT_BROOD_URL,
        spire_api_url: str = BUGOUT_SPIRE_URL,
    ) -> None:
        self.brood_api_url = brood_api_url
        self.spire_api_url = spire_api_url

        self.user = User(self.brood_api_url)
        self.group = Group(self.brood_api_url)
        self.journal = Journal(self.spire_api_url)

    @property
    def brood_url(self):
        return self.brood_api_url

    @property
    def spire_url(self):
        return self.spire_api_url

    def brood_ping(self) -> Dict[str, str]:
        return ping(self.brood_api_url)

    def spire_ping(self) -> Dict[str, str]:
        return ping(self.spire_api_url)

    # User handlers
    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        timeout: float = REQUESTS_TIMEOUT,
        **kwargs: Dict[str, Any],
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.create_user(
            username=username, email=email, password=password, **kwargs
        )

    def get_user(
        self, token: Union[str, uuid.UUID], timeout: float = REQUESTS_TIMEOUT
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.get_user(token=token)

    def get_user_by_id(
        self,
        token: Union[str, uuid.UUID],
        user_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.get_user_by_id(token=token, user_id=user_id)

    def find_user(
        self,
        username: str,
        token: Union[str, uuid.UUID] = None,
        timeout: float = REQUESTS_TIMEOUT,
        **kwargs: Dict[str, Any],
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.find_user(username=username, token=token, **kwargs)

    def confirm_email(
        self,
        token: Union[str, uuid.UUID],
        verification_code: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.confirm_email(token=token, verification_code=verification_code)

    def restore_password(
        self, email: str, timeout: float = REQUESTS_TIMEOUT
    ) -> Dict[str, str]:
        self.user.timeout = timeout
        return self.user.restore_password(email=email)

    def reset_password(
        self,
        reset_id: Union[str, uuid.UUID],
        new_password: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.reset_password(reset_id=reset_id, new_password=new_password)

    def change_password(
        self,
        token: Union[str, uuid.UUID],
        current_password: str,
        new_password: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.change_password(
            token=token, current_password=current_password, new_password=new_password
        )

    def delete_user(
        self,
        token: Union[str, uuid.UUID],
        user_id: Union[str, uuid.UUID],
        password: Optional[str] = None,
        timeout: float = REQUESTS_TIMEOUT,
        **kwargs: Dict[str, Any],
    ) -> data.BugoutUser:
        self.user.timeout = timeout
        return self.user.delete_user(
            token=token, user_id=user_id, password=password, **kwargs
        )

    # Token handlers
    def create_token(
        self, username: str, password: str, timeout: float = REQUESTS_TIMEOUT
    ) -> data.BugoutToken:
        self.user.timeout = timeout
        return self.user.create_token(username=username, password=password)

    def create_token_restricted(
        self,
        token: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutToken:
        self.user.timeout = timeout
        return self.user.create_token_restricted(token=token)

    def revoke_token(
        self, token: Union[str, uuid.UUID], timeout: float = REQUESTS_TIMEOUT
    ) -> uuid.UUID:
        self.user.timeout = timeout
        return self.user.revoke_token(token=token)

    def revoke_token_by_id(
        self, token: Union[str, uuid.UUID], timeout: float = REQUESTS_TIMEOUT
    ) -> uuid.UUID:
        self.user.timeout = timeout
        return self.user.revoke_token_by_id(token=token)

    def update_token(
        self,
        token: Union[str, uuid.UUID],
        token_type: Optional[Union[str, data.TokenType]] = None,
        token_note: Optional[str] = None,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutToken:
        self.user.timeout = timeout
        return self.user.update_token(
            token=token,
            token_type=data.TokenType(token_type) if token_type is not None else None,
            token_note=token_note,
        )

    def get_token_types(
        self, token: Union[str, uuid.UUID], timeout: float = REQUESTS_TIMEOUT
    ) -> List[str]:
        self.user.timeout = timeout
        return self.user.get_token_types(token=token)

    def get_user_tokens(
        self,
        token: Union[str, uuid.UUID],
        active: Optional[bool] = None,
        token_type: Optional[Union[str, data.TokenType]] = None,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutUserTokens:
        self.user.timeout = timeout
        return self.user.get_user_tokens(
            token=token,
            active=active,
            token_type=data.TokenType(token_type) if token_type is not None else None,
        )

    # Group handlers
    def get_group(
        self,
        token: Union[str, uuid.UUID],
        group_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroup:
        self.group.timeout = timeout
        return self.group.get_group(token=token, group_id=group_id)

    def find_group(
        self,
        token: Union[str, uuid.UUID],
        group_id: Optional[Union[str, uuid.UUID]] = None,
        name: Optional[str] = None,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroup:
        self.user.timeout = timeout
        return self.group.find_group(token=token, group_id=group_id, name=name)

    def get_user_groups(
        self, token: Union[str, uuid.UUID], timeout: float = REQUESTS_TIMEOUT
    ) -> data.BugoutUserGroups:
        self.group.timeout = timeout
        return self.group.get_user_groups(token=token)

    def create_group(
        self,
        token: Union[str, uuid.UUID],
        group_name: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroup:
        self.group.timeout = timeout
        return self.group.create_group(token=token, group_name=group_name)

    def set_user_group(
        self,
        token: Union[str, uuid.UUID],
        group_id: Union[str, uuid.UUID],
        user_type: Union[str, data.Role],
        username: Optional[str] = None,
        email: Optional[str] = None,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroupUser:
        self.group.timeout = timeout
        return self.group.set_user_group(
            token=token,
            group_id=group_id,
            user_type=data.Role(user_type),
            username=username,
            email=email,
        )

    def delete_user_group(
        self,
        token: Union[str, uuid.UUID],
        group_id: Union[str, uuid.UUID],
        username: Optional[str] = None,
        email: Optional[str] = None,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroupUser:
        self.group.timeout = timeout
        return self.group.delete_user_group(
            token=token, group_id=group_id, username=username, email=email
        )

    def get_group_members(
        self,
        token: Union[str, uuid.UUID],
        group_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroupMembers:
        self.group.timeout = timeout
        return self.group.get_group_members(token=token, group_id=group_id)

    def update_group(
        self,
        token: Union[str, uuid.UUID],
        group_id: Union[str, uuid.UUID],
        group_name: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroup:
        self.group.timeout = timeout
        return self.group.update_group(
            token=token, group_id=group_id, group_name=group_name
        )

    def delete_group(
        self,
        token: Union[str, uuid.UUID],
        group_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutGroup:
        self.group.timeout = timeout
        return self.group.delete_group(token=token, group_id=group_id)

    # Journal scopes handlers
    def list_scopes(
        self, token: Union[str, uuid.UUID], api: str, timeout: float = REQUESTS_TIMEOUT
    ) -> data.BugoutScopes:
        self.journal.timeout = timeout
        return self.journal.list_scopes(token=token, api=api)

    def get_journal_scopes(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalScopeSpecs:
        self.journal.timeout = timeout
        return self.journal.get_journal_scopes(token=token, journal_id=journal_id)

    def update_journal_scopes(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        holder_type: Union[str, data.HolderType],
        holder_id: Union[str, uuid.UUID],
        permission_list: List[str],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalScopeSpecs:
        self.journal.timeout = timeout
        return self.journal.update_journal_scopes(
            token=token,
            journal_id=journal_id,
            holder_type=data.HolderType(holder_type),
            holder_id=holder_id,
            permission_list=permission_list,
        )

    def delete_journal_scopes(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        holder_type: Union[str, data.HolderType],
        holder_id: Union[str, uuid.UUID],
        permission_list: List[str],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalScopeSpecs:
        self.journal.timeout = timeout
        return self.journal.delete_journal_scopes(
            token=token,
            journal_id=journal_id,
            holder_type=data.HolderType(holder_type),
            holder_id=holder_id,
            permission_list=permission_list,
        )

    # Journal handlers
    def create_journal(
        self, token: Union[str, uuid.UUID], name: str, timeout: float = REQUESTS_TIMEOUT
    ) -> data.BugoutJournal:
        self.journal.timeout = timeout
        return self.journal.create_journal(token=token, name=name)

    def list_journals(
        self, token: Union[str, uuid.UUID], timeout: float = REQUESTS_TIMEOUT
    ) -> data.BugoutJournals:
        self.journal.timeout = timeout
        return self.journal.list_journals(token=token)

    def get_journal(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournal:
        self.journal.timeout = timeout
        return self.journal.get_journal(token=token, journal_id=journal_id)

    def update_journal(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        name: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournal:
        self.journal.timeout = timeout
        return self.journal.update_journal(
            token=token, journal_id=journal_id, name=name
        )

    def delete_journal(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournal:
        self.journal.timeout = timeout
        return self.journal.delete_journal(token=token, journal_id=journal_id)

    # Journal entries
    def create_entry(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        title: str,
        content: str,
        tags: List[str] = [],
        context_url: Optional[str] = None,
        context_id: Optional[str] = None,
        context_type: Optional[str] = None,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntry:
        self.journal.timeout = timeout
        return self.journal.create_entry(
            token=token,
            journal_id=journal_id,
            title=title,
            content=content,
            tags=tags,
            context_url=context_url,
            context_id=context_id,
            context_type=context_type,
        )

    def get_entry(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntry:
        self.journal.timeout = timeout
        return self.journal.get_entry(
            token=token, journal_id=journal_id, entry_id=entry_id
        )

    def get_entries(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntries:
        self.journal.timeout = timeout
        return self.journal.get_entries(token=token, journal_id=journal_id)

    def get_entry_content(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntryContent:
        self.journal.timeout = timeout
        return self.journal.get_entry_content(
            token=token, journal_id=journal_id, entry_id=entry_id
        )

    def update_entry_content(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        title: str,
        content: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntryContent:
        self.journal.timeout = timeout
        return self.journal.update_entry_content(
            token=token,
            journal_id=journal_id,
            entry_id=entry_id,
            title=title,
            content=content,
        )

    def delete_entry(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntry:
        self.journal.timeout = timeout
        return self.journal.delete_entry(
            token=token, journal_id=journal_id, entry_id=entry_id
        )

    # Tags
    def get_most_used_tags(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> List[Any]:
        self.journal.timeout = timeout
        return self.journal.get_most_used_tags(token=token, journal_id=journal_id)

    def create_tags(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        tags: List[str],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> List[Any]:
        self.journal.timeout = timeout
        return self.journal.create_tags(
            token=token, journal_id=journal_id, entry_id=entry_id, tags=tags
        )

    def get_tags(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntryTags:
        self.journal.timeout = timeout
        return self.journal.get_tags(
            token=token, journal_id=journal_id, entry_id=entry_id
        )

    def update_tags(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        tags: List[str],
        timeout: float = REQUESTS_TIMEOUT,
    ) -> List[Any]:
        self.journal.timeout = timeout
        return self.journal.update_tags(
            token=token, journal_id=journal_id, entry_id=entry_id, tags=tags
        )

    def delete_tag(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        entry_id: Union[str, uuid.UUID],
        tag: str,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutJournalEntryTags:
        self.journal.timeout = timeout
        return self.journal.delete_tag(
            token=token, journal_id=journal_id, entry_id=entry_id, tag=tag
        )

    # Search
    def search(
        self,
        token: Union[str, uuid.UUID],
        journal_id: Union[str, uuid.UUID],
        query: str,
        limit: int = 10,
        offset: int = 0,
        content: bool = True,
        timeout: float = REQUESTS_TIMEOUT,
    ) -> data.BugoutSearchResults:
        self.journal.timeout = timeout
        return self.journal.search(token, journal_id, query, limit, offset, content)
