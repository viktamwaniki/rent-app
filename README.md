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

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3 installed.
- Virtual environment (optional but recommended).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/viktamwaniki/rent-app
   ```

2. Navigate to the project directory:

   ```bash
   cd app
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

## Usage

### Adding a Tenant

To add a new tenant to the database, use the following command:

```bash
python3 main.py 
```

### Adding a Property

To add a new property location to the database, use the following command:

```bash
python3 main.py 
```
## Database Schema

The app uses an SQLite database with the following schema:

- Tenants
- Properties
- Payments
- Tenant-Property Association

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README.md according to your specific project needs. You can also include screenshots, additional sections, or any other relevant information to make it more comprehensive.