from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column
from .declarative_base.declarative_base import Base
import datetime

# class DuoCrypto(Enum):
#     BTC_USDT = 'BTC/USDT'
#     BTC_ETH = 'BTC/ETH'
#     BTC_XMR = 'BTC/XMR'
#     BTC_SOL = 'BTC/SOL'
#     BTC_RUB = 'BTC/RUB'
#     BTC_DOGS = 'BTC/DOGC'
 

class Binance(Base):
    __tablename__ = 'binance'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    min_price: Mapped[float] = mapped_column(nullable=False)
    max_price: Mapped[float] = mapped_column(nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.now(datetime.timezone.utc), 
                                                    onupdate=datetime.datetime.now(datetime.timezone.utc))
    difference: Mapped[float] = mapped_column(nullable=False)
    total_amount: Mapped[float] = mapped_column(nullable=False)

    repr_cols_num = 3