from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Tenant

engine = create_engine('sqlite:///rental_payment.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_tenant():
    tenant_name = input("Enter the tenant's name: ")
    new_tenant = Tenant(name=tenant_name)
    session.add(new_tenant)
    session.commit()
    print(f'Tenant "{new_tenant.name}" has been added to the database.')


def remove_tenant():
    tenant_id = int(input("Enter the tenant's ID to remove: "))
    tenant_to_remove = session.query(Tenant).filter_by(id=tenant_id).first()

    if tenant_to_remove:
        session.delete(tenant_to_remove)
        session.commit()
        print(f'Tenant "{tenant_to_remove.name}" has been removed from the database.')
    else:
        print(f'Tenant with ID "{tenant_id}" not found in the database.')


# Function to add start and end dates to a tenant's record
"""def add_start_and_end_dates():
    tenant_id = int(input("Enter the tenant's ID: "))
    property_id = int(input("Enter the property's ID: "))
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    tenant = session.query(Tenant).filter_by(id=tenant_id).first()
    property = session.query(Property).filter_by(id=property_id).first()

    if tenant and property:
        tenant_property = TenantPropertyAssociation(
            tenant=tenant,
            property=property,
            start_date=start_date,
            end_date=end_date
        )
        session.add(tenant_property)
        session.commit()
        print(f'Start and end dates added for Tenant ID {tenant_id} and Property ID {property_id}.')
    else:
        print(f'Tenant with ID "{tenant_id}" or Property with ID "{property_id}" not found in the database.')

# Function to view tenant information
def see_tenant_info():
    tenant_id = int(input("Enter the tenant's ID: "))
    tenant = session.query(Tenant).filter_by(id=tenant_id).first()

    if tenant:
        print(f'Tenant ID: {tenant.id}')
        print(f'Tenant Name: {tenant.name}')
        print(f'Start Date: {tenant.start_date}')
        print(f'End Date: {tenant.end_date}')
    else:
        print(f'Tenant with ID "{tenant_id}" not found in the database.')"""

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Add Tenant")
        print("2. Remove Tenant")
       #print("3. Add Start and End Dates")
       #print("4. See Tenant Info")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_tenant()
        elif choice == "2":
            remove_tenant()
        elif choice == "5":
            session.close()
            break
        else:
            print("Invalid choice. Please enter a valid option.")
