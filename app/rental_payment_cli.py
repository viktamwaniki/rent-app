from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Tenant 


engine = create_engine('sqlite:///app/rental_payment.db')


Session = sessionmaker(bind=engine)
session = Session()

new_tenant = Tenant(name="John Doe")
session.add(new_tenant)
session.commit()

retrieved_tenant = session.query(Tenant).filter_by(name="John Doe").first()

print("Tenant ID:", retrieved_tenant.id)
print("Tenant Name:", retrieved_tenant.name)

session.close()
