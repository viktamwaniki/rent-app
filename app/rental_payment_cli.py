from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Tenant 


engine = create_engine('sqlite:///app/rental_payment.db')
Session = sessionmaker(bind=engine)
session = Session()

"""def add_tenant():
    tenant_name = input("Enter the tenant's name: ")
    new_tenant = Tenant(name=tenant_name)
    session.add(new_tenant)
    session.commit()
    print(f'Tenant "{tenant_name}" has been added to the database.')
add_tenant()"""

def remove_tenant():
    tenant_name = input("Enter the tenant's name to remove: ")
    tenant_to_remove = session.query(Tenant).filter_by(name=tenant_name).first()

    if tenant_to_remove:
        session.delete(tenant_to_remove)
        session.commit()
        print(f'Tenant "{tenant_name}" has been removed from the database.')
    else:
        print(f'Tenant "{tenant_name}" not found in the database.')
remove_tenant()

session.close()
