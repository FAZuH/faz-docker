from __future__ import annotations
from typing import Any, TYPE_CHECKING

from ...base_repository import BaseRepository
from ..model import DiscordUser

if TYPE_CHECKING:
    from ...base_mysql_database import BaseMySQLDatabase


class DiscordUserRepository(BaseRepository[DiscordUser, Any]):

    def __init__(self, database: BaseMySQLDatabase) -> None:
        super().__init__(database, DiscordUser)
