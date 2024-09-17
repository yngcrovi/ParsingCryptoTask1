from repositoy.config.engine import async_session_factory
from sqlalchemy import select, cast, update, delete
from repositoy.models.declarative_base.declarative_base import Base
from pydantic import BaseModel

class PostgreSQLRepository:
    asf = async_session_factory
    table = Base

    async def insert_data(self, insert_data: dict | list):
        async with self.asf() as session:
            if type(insert_data) == dict:
                rows_to_insert = self.table(**insert_data)
                session.add(rows_to_insert)
                await session.flush()
                await session.refresh(rows_to_insert)
                await session.commit()
                return rows_to_insert
            else:
                rows_to_insert = [self.table(**row) for row in insert_data]
                session.add_all(rows_to_insert)
                await session.commit()

    async def select_data(self, filter_data: dict | None):
        async with self.asf() as session:
            if type(filter_data) is dict:
                query = (
                    select(self.table)
                    .filter_by(**filter_data)
                )
            else:
                query = (
                    select(self.table)
                    .order_by(self.table.id)
                )
            result = await session.execute(query)
            return result

    async def update_data(self, upd_title: list | str, upd_data: dict | list) -> None:
        async with self.asf() as session:
            if type(upd_data) == dict:
                upd = (
                    update(self.table)
                    .filter(self.table.title == upd_title)
                    .values(upd_data)
                )
            else:
                for i in range(len(upd_data)):
                    upd = (
                        update(self.table)
                        .filter(self.table.title == upd_title[i])
                        .values(upd_data[i])
                    )
                    await session.execute(upd)
            await session.commit()

    async def delete_data(self, id: int):
        async with self.asf() as session:
            query = (
                delete(self.table)
                .filter(self.table.id == id)
            )
            await session.execute(query)
            await session.commit()

    def get_dto_form(self, dto_form: BaseModel, res: list):
        result_dto = [dto_form.model_validate(row, from_attributes=True) for row in res]
        if len(result_dto) == 1:
            result_dto = result_dto[0]
        return result_dto