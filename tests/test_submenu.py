import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from menu_app.main import Menu, Submenu


@pytest.mark.asyncio
async def test_create_submenu(async_client: AsyncClient):
    response = await async_client.post(
                "menus/1/submenus",
                json={"title": "Submenu 1",
                      "description": "Submenu description 1"},
    )
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "Submenu 1"
    assert data["description"] == "Submenu description 1"
    assert data["menu_id"] == 1


@pytest.mark.asyncio
async def test_create_submenu_incomplete(async_client: AsyncClient):
    # No description
    response = await async_client.post("menus/1/submenus",
                           json={"title": "Menu 1"})

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_create_submenu_invalid(async_client: AsyncClient):
    # title has an invalid type
    response = await async_client.post(
        "menus/1/submenus",
        json={
            "title": {"message": "Submenu 1"},
            "description": "Submenu description 1",
        },
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_read_submenus(async_session: AsyncSession, async_client: AsyncClient):
    submenu_1 = Submenu(
            title="Submenu 1",
            description="Submenu description 1",
            menu_id=1
    )
    submenu_2 = Submenu(
            title="Submenu 2",
            description="Submenu description 1",
            menu_id=1
    )
    async_session.add(submenu_1)
    async_session.add(submenu_2)
    await async_session.commit()

    response = await async_client.get(f"menus/{submenu_1.menu_id}/submenus")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["title"] == submenu_1.title
    assert data[0]["description"] == submenu_1.description
    assert data[0]["id"] == str(submenu_1.id)
    assert data[0]["menu_id"] == submenu_1.menu_id
    assert data[1]["title"] == submenu_2.title
    assert data[1]["description"] == submenu_2.description
    assert data[1]["id"] == str(submenu_2.id)
    assert data[1]["menu_id"] == submenu_2.menu_id


@pytest.mark.asyncio
async def test_read_submenus_is_empty(async_session: AsyncSession, async_client: AsyncClient):
    menu = Menu(title="Menu 1", description="Menu description 1")
    async_session.add(menu)
    await async_session.commit()

    response = await async_client.get(f"menus/{menu.id}/submenus")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 0


@pytest.mark.asyncio
async def test_read_submenu(async_session: AsyncSession, async_client: AsyncClient):
    submenu = Submenu(
            title="Submenu 1",
            description="Submenu description 1",
            menu_id=1
    )
    async_session.add(submenu)
    await async_session.commit()

    response = await async_client.get(
            f"menus/{submenu.menu_id}/submenus/{submenu.id}"
    )
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == submenu.title
    assert data["description"] == submenu.description
    assert data["id"] == str(submenu.id)
    assert data["menu_id"] == submenu.menu_id


@pytest.mark.asyncio
async def test_update_submenu(async_session: AsyncSession, async_client: AsyncClient):
    submenu = Submenu(
            title="Submenu 1",
            description="Submenu description 1",
            menu_id=1
    )
    async_session.add(submenu)
    await async_session.commit()

    response = await async_client.patch(
            f"menus/{submenu.menu_id}/submenus/{submenu.id}",
            json={"title": "Update submenu 1"},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Update submenu 1"
    assert data["description"] == "Submenu description 1"
    assert data["id"] == submenu.id


@pytest.mark.asyncio
async def test_delete_menu(async_session: AsyncSession, async_client: AsyncClient):
    submenu = Submenu(
            title="Submenu 1",
            description="Submenu description 1",
            menu_id=1
    )
    async_session.add(submenu)
    await async_session.commit()

    response = await async_client.delete(
            f"menus/{submenu.menu_id}/submenus/{submenu.id}"
    )
    submenu_in_db = await async_session.get(Submenu, submenu.id)

    assert response.status_code == 200
    assert submenu_in_db is None
