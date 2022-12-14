from functools import lru_cache

from sqlalchemy import select

from carnage.database.models.dungeon import DungeonSchemaModel
from carnage.database.repository.base import BaseRepository


class DungeonSchemaRepository(BaseRepository):
    def __init__(
        self,
        model: type[DungeonSchemaModel] = DungeonSchemaModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)

    @lru_cache
    def select_by_dungeon_difficulty(
        self,
        dungeon_difficulty_id: str,
    ) -> list[DungeonSchemaModel]:
        """Get results from database filtering by dungeon difficulty id.

        :param dungeon_difficulty_id: Dungeon difficulty id to be used in the
            filter.
        """
        statement = select(self.model).where(
            self.model.dungeon_difficulty_id == dungeon_difficulty_id
            and self.deleted_at == None,  # type: ignore # noqa
        )

        with self.session() as session:
            return session.execute(statement=statement).scalars().all()
