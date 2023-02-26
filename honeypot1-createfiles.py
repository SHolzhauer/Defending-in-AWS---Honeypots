import random
import csv
from faker import Faker
# Needed to generate pdf files
from fpdf import FPDF

class Person:

    def __init__(self):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.address = "{} {} {}".format(fake.street_address(), fake.postcode(), fake.city())
        self.bsn = fake.ssn()
        self.iban = fake.iban()


fake = Faker('nl_NL')

# First we create a csv file which will look like an employee dump

# Define the header row
header = ['first name', 'last name', 'email', 'address', 'bsn', 'bank']

people = []

# Generate fake data and write to CSV file
with open('employee_details_feb_2023.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(header)
    
    # Write 20 rows of fake data
    for i in range(531):
        p = Person()
        people.append(p)
        # Write the row to the CSV file
        writer.writerow([p.first_name, p.last_name, p.email, p.address, p.bsn, p.iban])


# Create the department directories
import os
os.mkdir("decoydata/")
departments = ["IT", "HR", "Sales", "Marketing", "Engineering"]
for i in departments:
    # Create the directory
    os.mkdir(f"decoydata/{i}")

for person in people:
    # create a pdf file for the person in one of the departments
    
    dept = random.choice(departments)

    try:
        # Create a new PDF object
        pdf = FPDF()

        # Add new A4-sized pages to the PDF
        pdf.add_page()
        pdf.add_page()
        pdf.add_page()

        # Set the font and font size
        pdf.set_font('Arial', 'B', 16)

        # Write some Lorem Ipsum text to each page
        pdf.cell(0, 10, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
        pdf.ln()
        pdf.cell(1, 10, 'Proin sit amet odio eu quam fermentum bibendum.')
        pdf.ln()
        pdf.cell(2, 10, 'Mauris a ipsum vel mauris laoreet ultrices.')
        pdf.ln()

        # Save the PDF file
        pdf.output(f"decoydata/{dept}/{person.last_name}-{person.first_name}.pdf", 'F')

    except Exception:
        pass