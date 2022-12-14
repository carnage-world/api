from carnage.database.models.spell import SpellRangeTypeModel
from carnage.database.repository.base import BaseRepository


class SpellRangeTypeRepository(BaseRepository):
    def __init__(
        self,
        model: type[SpellRangeTypeModel] = SpellRangeTypeModel,
    ) -> None:
        """Default constructor for repository.

        :param model: The model used in the repository.
        """
        super().__init__(model)
