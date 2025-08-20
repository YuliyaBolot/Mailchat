import string
import os
from random import choice, randint
from faker import Faker

fake = Faker()


class Email:
    Correct_email = [f'{''.join(choice(string.ascii_lowercase) for _ in range(10))}{randint(1, 10)}@test.com',
                     f'{''.join(choice(string.ascii_lowercase) for _ in range(10))}@test.com',
                     f'{randint(1, 10)}@test.com']

    Incorrect_email = [f'{''.join(choice(string.ascii_lowercase) for _ in range(10))}{randint(1, 10)}.com',
                       f'{''.join(choice(string.ascii_lowercase) for _ in range(10))}{randint(1, 10)}@.com',
                       f'{''.join(choice(string.ascii_lowercase) for _ in range(10))}{randint(1, 10)}@.test',
                       '&^^%$$##@test.com', ' @test.com', '@test.com']

    New_email = [f'{fake.first_name()}@test.com', f'{fake.first_name()}@test.com', f'{fake.last_name()}@test.com',
                 f'{fake.first_name()}@test.com']


class Code:
    Correct_code = [6, 6, 6, 5, 5, 5]

    Incorrect_code = [i for i in range(0, 9)]

    Short_code = [i for i in range(0, 9)]

    Error_code_message = "Код введен неправильно"


class Workspace:
    Message_about_short_workspace_name = "Имя домена не может быть короче 3-х символов"

    Message_about_incorrect_workspace_name = "Разрешены латинские буквы и символы aA-zZ, 0-9, -, _"

    Message_about_domain_is_taken = "Этот домен занят"

    Correct_workspace_name = f'{''.join(choice(string.ascii_lowercase) for _ in range(3, 24))}{randint(1, 9)}'

    Short_workspace_name = f'{''.join(choice(string.ascii_lowercase) for _ in range(1, 3))}'

    Incorrect_workspace_name = "абвгдеёжзийклмнопрстуфхц"

    Exist_domain = "test"

    New_workspace_name = [f'{fake.last_name()}{randint(1000, 2000)}', f'{fake.last_name()}{randint(1000, 2000)}',
                          f'{fake.last_name()}{randint(1000, 2000)}', f'{fake.last_name()}{randint(1000, 2000)}']


class Profile:
    Name = fake.first_name()
    Last_name = fake.last_name()
    Photo = os.path.abspath(r"photo.jpg")
