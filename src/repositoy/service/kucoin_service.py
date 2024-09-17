from repositoy.db_repo.postgres import PostgreSQLRepository
from repositoy.models.kucoin import Kucoin
from repositoy.models.declarative_base.declarative_base import Base
from repositoy.service.dto.kucoin_dto import KucoinGetDTO


class KucoinService(PostgreSQLRepository):

    def __init__(self, table: Base):
        self.table = table

    async def select_crypto(self, filter_data: dict = None, dto = KucoinGetDTO) -> KucoinGetDTO:
        result = await self.select_data(filter_data)
        res = result.scalars().all()
        result_dto = self.get_dto_form(dto, res)
        return result_dto
    

    async def insert_crypto(self, data: dict | list) -> Kucoin:
        value = await self.insert_data(data)
        return value
    
    async def update_crypto(self, upd_title: str | list, upd_data: dict | list):
        await self.update_data(upd_title, upd_data)



kucoin_service = KucoinService(Kucoin)