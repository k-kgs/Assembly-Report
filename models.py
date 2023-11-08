from database import Base
from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

class StoreReportDetail(Base):
    __tablename__ = "store_report_details"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    start_time = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))

class StorePollData(Base):
    __tablename__ = "store_poll_data"
    store_id = Column(Integer)
    timestamp_utc = Column(DateTime(timezone=True))
    status = Column(String(15))

class StoreBuisnessHours(Base):
    __tablename__ = "store_buisness_hrs"
    store_id = Column(Integer)
    day = Column(Integer)
    start_time_local = Column(DateTime(timezone=True))
    end_time_local = Column(DateTime(timezone=True))

class StoreTimezone(Base):
    __tablename__ = "store_timezone"
    store_id = Column(Integer)
    timezone_str = Column(String)
