from src.controllers.interfaces.natural_person_deleter_controller import (
    NaturalPersonDeleterControllerInterface
    )
from src.models.sqlite.interfaces.natural_person_repository import NaturalPersonRepositoryInterface


class NaturalPersonDeleterController(NaturalPersonDeleterControllerInterface):
    def __init__(self, natural_person_repository: NaturalPersonRepositoryInterface) -> None:
        self.__natural_person_repository = natural_person_repository

    def delete(self, name: str) -> None:
        self.__natural_person_repository.delete_natural_person(name)
