from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from menu_app.submenu_model import Submenu
    from menu_app.submenu_model import Menu


class DishBase(SQLModel):
    title: str = Field(index=True)
    description: str
    price: float
    submenu_id: Optional[int] = Field(default=None, foreign_key="submenu.id")
    menu_id: Optional[int] = Field(default=None, foreign_key="menu.id")


class Dish(DishBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    menu: Optional["Menu"] = Relationship(back_populates="dishes")
    submenu: Optional["Submenu"] = Relationship(back_populates="dishes")


class DishRead(DishBase):
    id: int


class DishCreate(DishBase):
    pass


class DishUpdate(SQLModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
