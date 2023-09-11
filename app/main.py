from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker
from models import Tenant, Property, Payment
from datetime import datetime

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


def list_tenants():
    tenants = session.query(Tenant).all()
    if tenants:
        print("\nList of Tenants:")
        for tenant in tenants:
            print(f"ID: {tenant.id}, Name: {tenant.name}")
    else:
        print("\nNo tenants found in the database.")

def add_property():
    property_name = input("Enter the property name: ")
    property_address = input("Enter the property address: ")
    
    new_property = Property(name=property_name, address=property_address)
    
    session.add(new_property)
    session.commit()
    
    print(f'Property "{new_property.name}" at address "{new_property.address}" has been added to the database.')

def remove_property():
    property_id = int(input("Enter the property's ID to remove: "))
    property_to_remove = session.query(Property).filter_by(id=property_id).first()

    if property_to_remove:
        session.delete(property_to_remove)
        session.commit()
        print(f'Property "{property_to_remove.name}" has been removed from the database.')
    else:
        print(f'Property with ID "{property_id}" not found in the database.')

def list_properties():
    properties = session.query(Property).all()
    if properties:
        print("\nList of Properties:")
        for property in properties:
            print(f"ID: {property.id}, Name: {property.name}, Address: {property.address}")
    else:
        print("\nNo properties found in the database.")


def relate_tenant():
   
    tenant_id = int(input("Enter the tenant's ID: "))
    property_id = int(input("Enter the property's ID: "))

   
    tenant = session.query(Tenant).filter_by(id=tenant_id).first()
    property = session.query(Property).filter_by(id=property_id).first()

    if tenant and property:
       
        if property in tenant.properties:
            print(f'Tenant "{tenant.name}" is already related to property "{property.name}".')
        else:
           
            tenant.properties.append(property)
            session.commit()
            print(f'Tenant "{tenant.name}" has been related to property "{property.name}".')
    else:
        print("Invalid tenant or property ID. Make sure both IDs exist in the database.")

def add_payment():
    tenant_id = int(input("Enter the tenant's ID for the payment: "))
    property_id = int(input("Enter the property's ID for the payment: "))
    payment_date_str = input("Enter the payment date (YYYY-MM-DD): ")
    amount = float(input("Enter the payment amount: "))

    try:
        payment_date = datetime.strptime(payment_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    new_payment = Payment(
        tenant_id=tenant_id,
        property_id=property_id,
        amount=amount,
        payment_date=payment_date
    )
    session.add(new_payment)
    session.commit()
    print("Payment has been added to the database.")

def remove_payment():
    payment_id = int(input("Enter the payment's ID to remove: "))
    payment_to_remove = session.query(Payment).filter_by(id=payment_id).first()

    if payment_to_remove:
        session.delete(payment_to_remove)
        session.commit()
        print("Payment has been removed from the database.")
    else:
        print(f"Payment with ID {payment_id} not found in the database.")

# Your existing menu code...

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Add Tenant")
        print("2. Remove Tenant")
        print("3. List Tenants")
        print("4. Add Property")
        print("5. Remove Property")
        print("6. List Properties")
        print("7. Relate Tenant to Property")
        print("8. Add Payment")
        print("9. Remove Payment")
        print("10. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice == "1":
            add_tenant()
        elif choice == "2":
            remove_tenant()
        elif choice == "3":
            list_tenants()
        elif choice == "4":
            add_property()
        elif choice == "5":
            remove_property()
        elif choice == "6":
            list_properties()
        elif choice == "7":
            relate_tenant()
        elif choice == "8":
            add_payment()  # Call the new function for adding payment
        elif choice == "9":
            remove_payment()  # Call the new function for removing payment
        elif choice == "10":
            session.close()
            break
        else:
            print("Invalid choice. Please enter a valid option.")