from sqlalchemy import Column, String, Integer, BIGINT, REAL
from src.models.sqlite.settings.base import Base

class LegalEntityTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(String)
    idade = Column(Integer)
    nome_fantasia = Column(String)
    celular = Column(String)
    email_corporativo = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)

    def __repr__(self):
        return (
            f"Legal Entity ["
            f"faturamento={self.faturamento}, "
            f"idade={self.idade}, "
            f"nome_fantasia={self.nome_fantasia}, "
            f"celular={self.celular}, "
            f"email_corporativo={self.email_corporativo}, "
            f"categoria={self.categoria}, "
            f"saldo={self.saldo}"
            f"]"
        )
    