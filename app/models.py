from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Float , Date
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

TenantPropertyAssociation = Table(
    'tenant_property_association',  # Table name
    Base.metadata,  # Reference to your Base metadata object
    Column('tenant_id', Integer, ForeignKey('tenants.id'), primary_key=True),
    Column('property_id', Integer, ForeignKey('properties.id'), primary_key=True),
)

class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define the many-to-many relationship with the Property model
    properties = relationship("Property", secondary=TenantPropertyAssociation, back_populates="tenants")
    payments = relationship("Payment", back_populates="tenant")

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    # Define the many-to-many relationship with the Tenant model
    tenants = relationship("Tenant", secondary=TenantPropertyAssociation, back_populates="properties")
    payments = relationship("Payment", back_populates="property")

    
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    amount = Column(Float)
    payment_date = Column(Date)

    # Define the relationship with Tenant
    tenant = relationship("Tenant", back_populates="payments")

    # Define the relationship with Property
    property = relationship("Property", back_populates="payments")
engine = create_engine('sqlite:///rental_payment.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
