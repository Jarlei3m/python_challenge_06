from sqlalchemy import Column, String, Integer, BIGINT, REAL
from src.models.sqlite.settings.base import Base

class NaturalPersonTable(Base):
    __table_name__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL)
    idade = Column(Integer) 
    nome_completo = Column(String) 
    celular = Column(String) 
    email = Column(String) 
    categoria = Column(String) 
    saldo = Column(REAL) 

    def __repr__(self):
        return (
            f"Natural Person ["
            f"renda_mensal={self.renda_mensal}, "
            f"idade={self.idade}, "
            f"nome_completo={self.nome_completo}, "
            f"celular={self.celular}, "
            f"email={self.email}, "
            f"categoria={self.categoria}, "
            f"saldo={self.saldo}"
            f"]"
        )
