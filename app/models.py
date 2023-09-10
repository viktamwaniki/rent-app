from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
   
    tenant_property_associations = relationship("TenantPropertyAssociation", back_populates="tenant")

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
   
    tenant_property_associations = relationship("TenantPropertyAssociation", back_populates="property")

class TenantPropertyAssociation(Base):
    __tablename__ = 'tenant_property_association'
    tenant_id = Column(Integer, ForeignKey('tenants.id'), primary_key=True)
    property_id = Column(Integer, ForeignKey('properties.id'), primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
   
    tenant = relationship("Tenant", back_populates="tenant_property_associations")
    property = relationship("Property", back_populates="tenant_property_associations")


engine = create_engine('sqlite:///app/rental_payment.db')
engine = create_engine('sqlite:///migrations_test.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
