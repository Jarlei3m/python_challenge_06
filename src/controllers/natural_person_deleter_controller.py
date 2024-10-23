from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface


class NaturalPersonDeleterController:
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface) -> None:
        self.__natural_person_repository = natural_person_repository

    def delete(self, name: str) -> None:
        self.__natural_person_repository.delete_natural_person(name)
