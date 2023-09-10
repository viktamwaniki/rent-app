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



if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Add Tenant")
        print("2. Remove Tenant")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_tenant()
        elif choice == "2":
            remove_tenant()
        elif choice == "3":
            session.close()
            break
        else:
            print("Invalid choice. Please enter a valid option.")
