from pydantic import BaseModel, ValidationError, constr

from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_request import HttpRequest

def natural_person_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        nome_completo: constr(min_length=1) # type: ignore
        renda_mensal: float 
        idade: int 
        celular: constr(min_length=1) # type: ignore
        email: constr(min_length=1) # type: ignore
        categoria: constr(min_length=1) # type: ignore
        saldo: float
    
    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
