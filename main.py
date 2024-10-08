"""Game logic."""

from faker import Faker
from school.component import Class, USStudent

fake = Faker()

if __name__ == "__main__":
    students = [
        USStudent(
            std_id=i,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        for i in range(1, 10)
    ]
    american_class = Class(students=students)
    american_class.roll_call()
