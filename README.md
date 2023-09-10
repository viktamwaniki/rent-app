# Rental Payment App

The Rental Payment App is a command-line application that helps you manage rental payments and property information. With this app, you can easily track rent payments, payment dates, and property locations in a database.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Adding a Tenant](#adding-a-tenant)
  - [Adding a Property](#adding-a-property)
  - [Recording Rent Payments](#recording-rent-payments)
  - [Viewing Tenant Information](#viewing-tenant-information)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add and manage tenant information.
- Add and manage property locations.
- Record rent payments with payment dates.
- View tenant information, property details, and payment history.
- Generate payment reports for analysis.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Virtual environment (optional but recommended).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/rental-payment-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rental-payment-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Adding a Tenant

To add a new tenant to the database, use the following command:

```bash
python rental_payment_cli.py add-tenant --name "Tenant Name"
```

Replace `"Tenant Name"` with the actual name of the tenant.

### Adding a Property

To add a new property location to the database, use the following command:

```bash
python rental_payment_cli.py add-property --address "Property Address"
```

Replace `"Property Address"` with the actual address of the property.

### Recording Rent Payments

To record a rent payment for a tenant and property, use the following command:

```bash
python rental_payment_cli.py record-payment --tenant "Tenant Name" --property "Property Address" --amount 1000 --date "2023-09-01"
```

Replace `"Tenant Name"` with the tenant's name, `"Property Address"` with the property's address, `1000` with the payment amount, and `"2023-09-01"` with the payment date.

### Viewing Tenant Information

To view tenant information, use the following command:

```bash
python rental_payment_cli.py view-tenant --name "Tenant Name"
```

Replace `"Tenant Name"` with the name of the tenant whose information you want to view.

### Generating Payment Reports

To generate a payment report, use the following command:

```bash
python rental_payment_cli.py generate-report --start-date "2023-01-01" --end-date "2023-12-31"
```

Replace `"2023-01-01"` and `"2023-12-31"` with the desired date range for the report.

## Database Schema

The app uses an SQLite database with the following schema:

- Tenants
- Properties
- Payments
- Tenant-Property Association

![Database Schema](database_schema.png)

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README.md according to your specific project needs. You can also include screenshots, additional sections, or any other relevant information to make it more comprehensive.