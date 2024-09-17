from repositoy.models.declarative_base.declarative_base import Base
from repositoy.config.engine import engine
from repositoy.models.binance import Binance
from repositoy.models.kucoin import Kucoin

Base.metadata.create_all(engine)