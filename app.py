from faker import Faker
import pandas as pd

# Initialize the Faker library
fake = Faker()

# Function to generate fake data
def generate_fake_data(num_records=10):
    data = []
    for _ in range(num_records):
        record = {
            'Name': fake.name(),
            'Address': fake.address(),
            'Email': fake.email(),
            'Phone Number': fake.phone_number(),
            'Date of Birth': fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
            'Company': fake.company(),
            'Job Title': fake.job()
        }
        data.append(record)
    return data

# Function to save data to a CSV file
def save_to_csv(data, filename='fake_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, sep='\t', index=True)

# Generate fake data
num_records = 10  # Number of fake records you want to generate
fake_data = generate_fake_data(num_records=num_records)

# Save fake data to CSV
save_to_csv(fake_data, filename='fake_data.txt')

print(f"Fake data with {num_records} records has been saved to 'fake_data.csv'")
