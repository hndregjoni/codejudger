from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class LanguageConstraint(Base):
    id = Column(Integer, primary_key=True)

    cset_id = Column(Integer, ForeignKey("constraintset.id", use_alter=True))
    # cset = relationship("ConstraintSet", back_populates="language_constraints")

    language_id = Column(String, ForeignKey("language.id"))
    language = relationship("Language", backref="constrained_to")