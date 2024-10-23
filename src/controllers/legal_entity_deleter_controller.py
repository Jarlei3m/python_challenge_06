from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface


class LegalEntityDeleterController:
    def __init__(self, legal_entity_repository: LegalEntityRepositoryInterface) -> None:
        self.__legal_entity_repository = legal_entity_repository

    def delete(self, name: str) -> None:
        self.__legal_entity_repository.delete_legal_entity(name)
