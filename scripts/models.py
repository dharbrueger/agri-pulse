from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'sqlite:///agri_pulse.db'
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weatherdata'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    weather_description = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)

class SoilMoistureData(Base):
    __tablename__ = 'soil_moisture_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    soil_moisture = Column(Float, nullable=False)
    normalized_soil_moisture = Column(Float, nullable=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
