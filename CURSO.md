# Curso FastAPI

- [Curso FastAPI](#curso-fastapi)
  - [1. Introduction](#1-introduction)
  - [2. Python Installation \& Refresher](#2-python-installation--refresher)
      - [1. Intro: Python Installation (Linux) + IDE](#1-intro-python-installation-linux--ide)
    - [(Fundamentos de programación)](#fundamentos-de-programación)
      - [2. Comments and Variables](#2-comments-and-variables)
      - [3. String formatting](#3-string-formatting)
      - [4. Getting User Input](#4-getting-user-input)
      - [5. Lists](#5-lists)
      - [6. Sets and Tuples](#6-sets-and-tuples)
      - [7. Booleans and Operators](#7-booleans-and-operators)
      - [8. If Elif Else Statements](#8-if-elif-else-statements)
      - [9. Loops](#9-loops)
      - [10. Dictionaries](#10-dictionaries)
      - [11. Functions](#11-functions)
    - [12. Imports \& Standard Library](#12-imports--standard-library)
    - [(OOP Game!)](#oop-game)
      - [13. OOP Overview](#13-oop-overview)
      - [14. Game Overview](#14-game-overview)
      - [15. Abstraction](#15-abstraction)
      - [16. Constructors (`Bar` in `foo = Bar()`)](#16-constructors-bar-in-foo--bar)
      - [17. Encapsulation](#17-encapsulation)
      - [18. Inheritance 1/2](#18-inheritance-12)
      - [19. Self vs Super](#19-self-vs-super)
      - [20. Inheritance 2/2](#20-inheritance-22)
      - [21. Polymorphism](#21-polymorphism)
      - [21. Composition](#21-composition)
  - [3. FastAPI Overview](#3-fastapi-overview)
  - [4. FastAPI Setup \& Installation (`pip` \& `venv`)](#4-fastapi-setup--installation-pip--venv)
  - [5. Project 1 - FastAPI Request Method Logic](#5-project-1---fastapi-request-method-logic)
    - [1. Intro](#1-intro)
    - [2. GET Request 1/2](#2-get-request-12)
    - [3. GET Request 2/2](#3-get-request-22)
    - [4. Path Parameters](#4-path-parameters)
    - [5. Query Parameters](#5-query-parameters)
    - [6. POST Request](#6-post-request)
    - [7. PUT Request](#7-put-request)
    - [8. DELETE Request](#8-delete-request)
    - [9. *Assignment*](#9-assignment)
  - [6. Project 2 - Move Fast with FastAPI](#6-project-2---move-fast-with-fastapi)
    - [(Swagger, Pydantic, Path \& Query Validation)](#swagger-pydantic-path--query-validation)
      - [1. Intro \& Project Setup (`Book` Python Object)](#1-intro--project-setup-book-python-object)
      - [2. POST Request before Validation](#2-post-request-before-validation)
      - [3. Book Request Data Validation (**pydantic**)](#3-book-request-data-validation-pydantic)
      - [4. Fields - Data Validation](#4-fields---data-validation)
      - [5. Pydantic Configurations (Swagger defaults)](#5-pydantic-configurations-swagger-defaults)
      - [6. Fetch Book](#6-fetch-book)
      - [7. Fetch Books by Rating](#7-fetch-books-by-rating)
      - [8. Update Book with PUT Request](#8-update-book-with-put-request)
      - [9. Delete Book with DELETE Request](#9-delete-book-with-delete-request)
      - [10. Assignment](#10-assignment)
      - [11. Data Validation: Path Parameters](#11-data-validation-path-parameters)
      - [12. Data Validation: Query Parameters](#12-data-validation-query-parameters)
    - [(HTTP Status Codes)](#http-status-codes)
      - [13. Status Codes Overview](#13-status-codes-overview)
      - [14. HTTP Exceptions](#14-http-exceptions)
      - [15. Explicit Status Code Responses](#15-explicit-status-code-responses)
  - [7. Project 3 - Complete RESTful APIs](#7-project-3---complete-restful-apis)
  - [8. (7.1) Setup Database ](#8-71-setup-database-)
      - [1. Intro](#1-intro-1)
      - [2. DB Connection with ORM SQLAlchemy](#2-db-connection-with-orm-sqlalchemy)
      - [3. DB Tables (Models)](#3-db-tables-models)
      - [4. main: DB Conn. for API \& init](#4-main-db-conn-for-api--init)
      - [5. SQLite3 Installation](#5-sqlite3-installation)
      - [6. SQL Queries Crash-Course](#6-sql-queries-crash-course)
      - [7. SQLite3 Setup: TODOs](#7-sqlite3-setup-todos)
  - [9. (7.2) API Request CRUD Methods](#9-72-api-request-crud-methods)
      - [1. GET All Todos from DB](#1-get-all-todos-from-db)
      - [2. GET Todo by ID](#2-get-todo-by-id)
      - [3. POST Request](#3-post-request)
      - [4. PUT Request](#4-put-request)
      - [5. DELETE Request](#5-delete-request)
  - [10. (7.3) Authentication \& Authorization (JWT)](#10-73-authentication--authorization-jwt)
      - [1. Routers: todos.py \& auth.py](#1-routers-todospy--authpy)
      - [2. One-To-Many Relationship (mind FKs)](#2-one-to-many-relationship-mind-fks)
      - [3. Rename SQLite DB, create Users table, add FK to Todos table](#3-rename-sqlite-db-create-users-table-add-fk-to-todos-table)
      - [4. create\_users endpoint, hashed passwords (*passlib* + *bcrypt*)](#4-create_users-endpoint-hashed-passwords-passlib--bcrypt)
      - [5. Save User to DB](#5-save-user-to-db)
      - [6. Authenticate User (`python-multipart` + `OAuth2PasswordRequestForm`)](#6-authenticate-user-python-multipart--oauth2passwordrequestform)
      - [7. JSON Web Token (JWT) Overview](#7-json-web-token-jwt-overview)
      - [8. Encode a JWT](#8-encode-a-jwt)
      - [9. Decode a JWT](#9-decode-a-jwt)
      - [10. Authentication Enhancements](#10-authentication-enhancements)
  - [11. (7.4) Authenticate Requests](#11-74-authenticate-requests)
      - [0. CUSTOM: tweak `auth.py` for authentication with `curl`](#0-custom-tweak-authpy-for-authentication-with-curl)
      - [1. POST Todo (user\_id)](#1-post-todo-user_id)
      - [2. GET all Todos (user\_id)](#2-get-all-todos-user_id)
      - [3. GET Todo (id + user\_id)](#3-get-todo-id--user_id)
      - [4. PUT Todo (user\_id)](#4-put-todo-user_id)
      - [5. DELETE Todo (user\_id)](#5-delete-todo-user_id)
      - [6. Admin Router](#6-admin-router)
      - [7. Assignment](#7-assignment)
  - [12. (7.5) Dockerized FastAPI with ~~MySQL~~ PostgreSQL (~~Large Production Database Setup~~)](#12-75-dockerized-fastapi-with-mysql-postgresql-large-production-database-setup)
    - [I. Dockerizar FastAPI](#i-dockerizar-fastapi)
    - [II. Implantar stack y verificar FastAPI requests](#ii-implantar-stack-y-verificar-fastapi-requests)
    - [III. pgAdmin (opcional)](#iii-pgadmin-opcional)
    - [IV. MySQL (UNDONE)](#iv-mysql-undone)
  - [13. Project 3.5 - Alembic Data Migration](#13-project-35---alembic-data-migration)
  - [14. Project 4 - Unit \& Integration Testing](#14-project-4---unit--integration-testing)
  - [15. Project 5 - Full Stack Application](#15-project-5---full-stack-application)
  - [16. Git - Version Control](#16-git---version-control)
  - [17. Deploying FastAPI Applications](#17-deploying-fastapi-applications)


## 1. Introduction

...


## 2. Python Installation & Refresher

<!-- <details> -->

#### 1. Intro: Python Installation (Linux) + IDE

<!-- <details> -->

> [!IMPORTANT]
> Custom setup for my Pop!_OS 22.04 workstation with the ~~*pycharm*~~ **vscodium** IDE

```bash
sudo apt get install -y --no-install-recommends \
  python3-pip python3-venv

python3 --version && python3 -c 'print("Hello World!")'
  # Python 3.10.12
  # Hello World!

python3 -m pip --version  # && pip install isort pip-autoremove -y
  # pip 22.0.2 from /home/pabloqpacin/repos/FastAPI-The-Complete-Course/.venv/lib/python3.10/site-packages/pip (python 3.10)

# ---
codium --version
  # 1.94.2
  # 62f778783c52510c94e687de293bc2ad230f9a67
  # x64
```

> [!TIP]
> Uso de virtual environments (`venv`) en este repo para **instalar FastAPI**

```bash
# cd ~/repos/FastAPI-The-Complete-Course
python3 -m venv .venv

# ---
source .venv/bin/activate

# pip install "fastapi[standard]"
# ...
# pip freeze > requirements.txt

deactivate
```

<!-- </details> -->

### (Fundamentos de programación)

<details>
<summary>Fundamentos de programación</summary>

#### 2. Comments and Variables

Comments

```py
# This is a comment
print('sup')
"""
This is a
multiline
comment
"""
'''
This is also a
multiline comment
'''
print('dawg')
  # sup
  # dawg
```
<!-- ```bash
python3 <<-EOF
# This is a comment
print('sup')
"""
This is a
multiline
comment
"""
'''
This is also a
multiline comment
'''
print('dawg')
EOF
  # sup
  # dawg
``` -->

Variables

```py
print(10)
  # 10

x=10
print(x)
  # 10

# ---
print (x + (x * 0.25))
  # 12.5

cost=10
tax_percent=0.25
tax=cost*tax_percent
price=cost+tax
print(price)
  # 12.5

# ---
username="pabloqpacin"
first_name="Pablo"
print(username + " " + first_name)
  # pabloqpacin Pablo

# ---
first_num=10
second_num=2
print(first_num)
print(second_num)
first_num=1
second_num=2
print(first_num)
print(second_num)
  # 10 2 1 2
```

Assignment

```py
'''
Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.
'''
money=50
cost=15
tax_percent=0.03
remaining_money=money-cost-cost*tax_percent
print(remaining_money)
  # 34.55
```

#### 3. String formatting

```py
first_name="Pablo"
print ("Hi " + first_name)
print (f"Hi {first_name}")
  # Hi Pablo
  # Hi Pablo

sentence="Hi {} {}"
last_name="Quevedo"
print(sentence.format(first_name,last_name))
print (f"Hi {first_name} {last_name}")
  # Hi Pablo Quevedo
  # Hi Pablo Quevedo
```

#### 4. Getting User Input

Uso de `var=input("foo")`

```py
first_name=input("Enter your first name: ")
days=input("How many days before your birthday: ")
print(f"Hi {first_name}, only {days} days "
      f"before your birthday!")
  # Pablo
  # 69
  # Hi Pablo, only 69 days before your birthday!
```

Strings Assignment

```py
'''
- Ask the user how many days until their birthday
- Using the print()function. Print an approx. number of weeks until their birthday
- 1 week is = to 7 days.
- Decimals within the return is allowed
'''
days=int(input("How many days until your birthday: "))
# print(type(days))
weeks=round(days/7, 2)
print(f"Only about {weeks} weeks until your birthday!")
```

#### 5. Lists

Lists (*indexed collections of data*)

```py
my_list=[80,96,72,100,8]
print(my_list)
  # [80, 96, 72, 100, 8]

people_list=["Pablo","Foo","Bar"]
print(people_list)
  # ['Pablo', 'Foo', 'Bar']

# ---
print(people_list[0])
  # Pablo
print(my_list[2])
  # 72

print(people_list[-1])
  # Bar

# ---
people_list[0]="supdawg"
print(people_list)
  # ['supdawg', 'Foo', 'Bar']

print(len(people_list))
  # 3

# ---
# SLICES
print(people_list[0:2])
  # ['supdawg', 'Foo']

print(my_list[2:4])
  # [72, 100]

# ---
my_list.append(1000)
print(my_list)
  # [80, 96, 72, 100, 8, 1000]

my_list.insert(2,2000)
print(my_list)
  # [80, 96, 2000, 72, 100, 8, 1000]

my_list.remove(8)
print(my_list)
  # [80, 96, 2000, 72, 100, 1000]

my_list.sort()
print(my_list)
  # [72, 80, 96, 100, 1000, 2000]
```

Lists Assignment

```py
'''
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
'''

zoo=["Pinguin","Chameleon","Koala","Octopus","Gorilla"]
zoo.pop(3)
zoo.append("Wombat")
zoo.pop(0)
print(zoo)
print(zoo[0:3])
```

#### 6. Sets and Tuples

Sets (*unordered <!--in memory--> lists, cannot contain duplications, use curly brackets*)

```py
my_set={1,4,3,2,5,1,2}
print(my_set)
print(len(my_set))
  # {1, 2, 3, 4, 5}
  # 5

for x in my_set:
  print(x)
  # 1
  # 2
  # 3
  # 4
  # 5

# ---
my_set.discard(3)
print(my_set)
  # {1, 2, 4, 5}

my_set.clear()
print(my_set)
  # set()

my_set.add(6)
print(my_set)
  # {6}

my_set.update([7,8])
print(my_set)
  # {8, 6, 7}
```

Tuples (*ordered unchangable*)

```py
my_tuple=(1,4,2,3,5)
print(my_tuple)
print(my_tuple[1])
print(len(my_tuple))
  # (1, 4, 2, 3, 5)
  # 4
  # 5
```

#### 7. Booleans and Operators

Booleans and Operators (*comparison and logical operators*)

```py
# Booleans (True or False)
like_coffee=True
like_tea=False
print(like_coffee)
print(type(like_coffee))
  # True
  # <class 'bool'>

# Comparison Operators
print(1 == 2)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
  # False
  # True
  # False
  # True
  # False
  # True

# Logical Operators
print(1 > 3 and 5 < 7)
print(1 > 3 or 5 < 7)
  # False
  # True

print(1 == 1)
print(not(1 == 1))
  # True
  # False
```

#### 8. If Elif Else Statements

Flow control

```py
hour=13

if hour<15:
  print("Good morning!")
elif hour<20:
  print("Good afternoon!")
else:
  print("Good night!")

print("Outside of if statement")

  # Good morning!
  # Outside of if statement
```

If Else Assignment

```py
'''
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:
if grade = 87 then print('B')
'''

grade=69

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")

# elif 80 <= grade < 90:
# elif grade >= 80 and grade < 90:
```

#### 9. Loops

For Loops

```py
for i in range(3,6):
  print(i)
  # 3
  # 4
  # 5

# ---
my_list=[1,4,3,2,5]
sum_of_list=0

# print(my_list[0])
# print(my_list[1])

# for i in sorted(my_list):
for i in my_list:
  sum_of_list+=i
  print(i)

print(sum_of_list)
  # 15

# ---
my_list=["Monday","Tuesday","Wednesday","Thursday"]

for i in my_list:
  print(f"Happy {i}!")
  # Happy Monday!
  # Happy Tuesday!
  # Happy Wednesday!
  # Happy Thursday!
```

While Loops

```py
i=0

while i<5:
  i+=1
  if i==3:
    continue
  print(i)
  if i==4:
    break
else:
  print("i is now larger or equal to 5")

  # 1
  # 2
  # 4
```

Loops Assignment

```py
'''
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements, use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
'''

my_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
i=0

while i<3:
  i+=1
  for j in my_list:
    if j=="Monday":
      continue
    print(j)
  print("===")

  # Tuesday
  # Wednesday
  # Thursday
  # Friday
  # ===
  # Tuesday
  # Wednesday
  # Thursday
  # Friday
  # ===
  # Tuesday
  # Wednesday
  # Thursday
  # Friday
  # ===
```

#### 10. Dictionaries

Dictionaries (*key-value pairs*)

```py
user_dictionary={
  'username':'pabloqpacin',
  'name':'Pablo',
  'age':69
}

user_dictionary["sex"]=False

print(user_dictionary)
print(len(user_dictionary))
  # {'username': 'pabloqpacin', 'name': 'Pablo', 'age': 69, 'sex': False}
  # 4

# ---
print(user_dictionary.get("username"))
  # pabloqpacin

user_dictionary.pop("age")
print(user_dictionary)
  # 69
  # {'username': 'pabloqpacin', 'name': 'Pablo', 'sex': False}

user_dictionary.clear()
print(user_dictionary)
  # {}

del user_dictionary
print(user_dictionary)
  # NameError: name 'user_dictionary' is not defined

# ---
for x in user_dictionary:
  print(x)
  # username
  # name
  # age
  # sex

for x,y in user_dictionary.items():
  print(x,y)
  # username pabloqpacin
  # name Pablo
  # age 69
  # sex False

# ---
# sin el copy(), ambos Dics. referencian al mismo, por lo que el pop afectaría a ambos
user_dictionary2=user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary2)
print(user_dictionary)
  # {'username': 'pabloqpacin', 'name': 'Pablo', 'sex': False}
  # {'username': 'pabloqpacin', 'name': 'Pablo', 'age': 69, 'sex': False}
```

Dictionaries Assignment

```py
'''
Based on the dictionary:
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2
'''

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for x,y in my_vehicle.items():
  print(x,y)

vehicle2=my_vehicle.copy()
vehicle2["number_of_tires"]=4
vehicle2.pop("mileage")

for x in vehicle2:
  print(x)

# model Ford
# make Explorer
# year 2018
# mileage 40000
# model
# make
# year
# number_of_tires
```

#### 11. Functions

Functions (*scope for global/local vars*)

> [!TIP]
> En el IDE, click derecho sobre `print` y *Go to definition*

```py
# print("Welcome to functions!")

def print_my_name(name,last_name):
  print(f"Hello {name} {last_name}!")

print_my_name("Pablo","Quevedo")
  # Hello Pablo Quevedo!

# ---
def print_color_red():
  color="Red"
  print(color)

color="Blue"
print(color)
print_color_red()
  # Blue
  # Red

# ---
def print_numbers(high,low):
  print(high)
  print(low)

print_numbers(low=3,high=10)
  # 10
  # 3

# ---
def multiply_numbers(a,b):
  return a*b

solution=multiply_numbers(10,6)
print(solution)
  # 60

# ---
def print_list(list_of_numbers):
  for x in list_of_numbers:
    print(x)

number_list=[1,2,3,4,5]
print_list(number_list)
  # 1
  # 2
  # 3
  # 4
  # 5

# ---
def buy_item(cost_of_item):
  return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
  current_tax_rate=.03
  return cost_of_item * current_tax_rate

final_cost=buy_item(50)
print(final_cost)
  # 51.5
```

Functions Assignment

```py
'''
- Create a function that takes in 3 parameters(firstname, lastname, age) and returns a dictionary based on those values
'''

def user_dictionary(firstname,lastname,age):
  created_user_dictionary={
    "firstname":firstname,
    "lastname":lastname,
    "age":age
  }
  return created_user_dictionary

solution_dictionary=user_dictionary(firstname='sup',lastname='dawg',age=69)
  # {'firstname': 'sup', 'lastname': 'dawg', 'age': 69}
```

</details>

### 12. Imports & Standard Library

<details>
<summary>Uso básico de `import`</summary>

> [!NOTE]
> Ojo: uso de varios archivos ~~sin Imports/~~

```tree
 tests
├──  a.py
└──  b.py
```

```py
# ./a.py

def calculate_homework(homework_assignments):
  sum_of_grades=0
  for homework in homework_assignments.values():
    sum_of_grades+=homework
  final_grade=round(sum_of_grades /
                  len(homework_assignments),2)
  print(final_grade)
```

```py
# ./b.py

# import Imports.a as foo
from a import *

homework_assignment_grades = {
  'homework_1':85,
  'homework_2':100,
  'homework_3':81,
}

calculate_homework(homework_assignment_grades)
# Imports.a.calculate_homework(homework_assignment_grades)
```
```bash
python3 tests/b.py
  # 88.67
```

Standard Library

```py
# == Random ==
import random

types_of_drinks=['Soda','Coffee','Water','Tea']
print(random.choice(types_of_drinks))

print(random.randint(1,10))


# == Math ==
import math
square_root=math.sqrt(64)
print(square_root)
  # 8.0


# == ...= =
# ...
```

</details>

### (OOP Game!)

<details>
<summary>Paso-a-paso del `00-oop_game/`</summary>

#### 13. OOP Overview

> [!NOTE]
> Ver diapositivas (249-...) en [./docs/FastAPI_slides.pdf](/docs/FastAPI_slides.pdf) <br>
> y el juego en [./00-oop_game/](/00-oop_game/)

- Paradigm for Scalability, Efficiency and Reusability
- Object definition by Behavior ~~(what it do)~~ VS State ~~(what it be)~~
- Primitive data type example below: **just variables, not a dawg object**!

```py
# main.py
legs:int=4
ears:int=2
type:str='Goldendoodle'
age:int=5
color:str='Yellow'
```

- Crear objetos en Python

```py
# dawg.py
class Dog:
  legs:int=4
  ears:int=2
  type:str='Goldendoodle'
  age:int=5
  color:str='Yellow'
```
```py
# main.py
from Dog import *

dog = Dog()

# en este caso, asignación estática pero ta bien
dog.legs    # 4
dog.ears    # 2
dog.type    # 'Goldendoodle'
dog.age     # 5
dog.color   # 'Yellow'
```

- 4 pillars of OOP: Encapsulation, Abstraction, Inheritance, Polymorphism


#### 14. Game Overview

Acceptance Criteria

```md
- Enemies that can fight one another
- Different types of enemies: Zombie, Ogre...
- Each enemy has different powers, health points and attack damage
```

Focus on: 4 pillars of OOP

What do we need

```md
Enemy Object:
- Name / Type of enemy
- Health points
- Attack damage
```

CODE

```tree
 00-oop_game
├──  __pycache__
│  └──  enemy.cpython-310.pyc
├──  enemy.py
└──  main.py
```
```py
# enemy.py
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1
```
```py
# main.py
from enemy import *

enemy = Enemy()

# enemy2 = Enemy()
# enemy2.health_points = 100
# print(enemy2.health_points)

enemy.type_of_enemy='Zombie'

print(f'{enemy.type_of_enemy} has '
        f'{enemy.health_points} health points '
        f'and can do attack of {enemy.attack_damage}')
```
```bash
python3 00-oop_game/main.py
  # Zombie has 10 health points and can do attack of 1
```

#### 15. Abstraction

> [!TIP]
> Usar `self` para referirse al objeto dentro del class file

- Hide implementation from the users it just works! ~~(via **methods** aka functions calls aye)~~
- Create simple and reusable code, following DRY principle
- Enables Python objects to become more scalable


```py
# enemy.py

    # ...
    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight.')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage.')
```
```py
# main.py

# ...
enemy.talk()
enemy.walk_forward()
enemy.attack()
```
```bash
python3 00-oop_game/main.py
  # Zombie has 10 health points and can do attack of 1
  # I am a Zombie. Be prepared to fight.
  # Zombie moves closer to you.
  # Zombie attacks for 1 damage.
```

#### 16. Constructors (`Bar` in `foo = Bar()`)

- Are used to create and initialize an object of a class with or without using values
- 3 different types:
  - Default/Empty Constructors
  - No Argument Constructors
  - Parameter Constructors

> `enemy.py`

```py
# Default/Empty Constructors
# Optional since it's created by default if no Arguments
# Empty constructor, what should happen when we instantiate this object
  # ...
  def __init__(self):
    pass
```
```py
# No Argument Constructors
  # ...
  def __init__(self):
    print('New enemy created with no starting values')
```
```py
# Parameter Constructors
class Enemy:
  def __init__(self,type_of_enemy,health_points=10,attack_damage=1):
    self.type_of_enemy=type_of_enemy
    self.health_points=health_points
    self.attack_damage=attack_damage
  def talk(self):
    print('I am an enemy')

# ---
# main.py

enemy0 = Enemy('Zombie')
enemy1 = Enemy('Zombie',15,3)
```

#### 17. Encapsulation

- Bundling of data
- Usecase: we don't want `zombie.type_of_enemy='Orc'` to happen (overwrite type etc.)
- Implementation:
  - Change public attributes to private with double underscore (`self.__type_of_enemy`)
  - Usage of Getters and Setters (`def get_foo`, `def set_foo`)
- Keeps related fields and methods together; makes code cleaner, flexible and reusable

```py
# enemy.py
class Enemy:
  def __init__(self,type_of_enemy,health_points=10,attack_damage=1):
    self.__type_of_enemy=type_of_enemy  # private: can't be changed when instanciated
    self.health_points=health_points    # public: can be changed when instanciated
    self.attack_damage=attack_damage    # public: can be changed when instanciated

  def get_type_of_enemy(self):
    return self.__type_of_enemy
```
```py
# main.py
zombie = Enemy('Zombie',15,3)
zombie.talk()
print(zombie.health_points)
print(zombie.get_type_of_enemy())
```

#### 18. Inheritance 1/2

- Process of acquiring properties from one class to others, creating a hierarchy between them (Parent and Child clases)
- Method overriding: child class inherits a method from the parent, but can be overwritten

```py
# classes.py
class Animal:
  weight: int
  color: str
  age: int
  animal_type: str

  def eat(self):
    print('Animal eating')
  def sleep(self):
    print('Animal sleeping')

class Dog(Animal):
  # All Animal Attributes
  can_shed: bool
  domestic_name: str

  # All Animal Methods
  def talk(self):
    print('Bark!')
  def eat(self):
    print('Chews on bone!')

# ---
# main.py

dog = Dog()
dog.eat()
```

#### 19. Self vs Super

> [!TIP]
> `self` VS `super` explained

- **self**:
  - refers to the current object that is created or being instantiated
  - <u>differenciates between the instance variables & parameters with the same name</u>
- **super**:
  - refers to the parent class
  - calls the parent class methods and constructors

```py
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Student(Person):
  def __init__(self,name,age,degree):
    super().__init__(name=name,age=age)
    self.degree=degree
```

#### 20. Inheritance 2/2

> [!NOTE]
> Archivos en [./00-oop_game/](/00-oop_game/)

- Parent class `Enemy()` with two children classes `Zombie()` and `Ogre()`
- Children classes instantiated with `super().__init__(args)` <!--`__init__`==constructor-->

```py
# enemy.py

class Enemy:
    def __init__(self,type_of_enemy,health_points=10,attack_damage=1):
        self.__type_of_enemy=type_of_enemy  # private: can't be changed when instanciated (encapsulation)
        self.health_points=health_points    # public: can be changed when instanciated
        self.attack_damage=attack_damage    # "
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    # def set_type_of_enemy(self,type_of_enemy):
    #     self.__type_of_enemy=type_of_enemy

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight.')
    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')
    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage.')
```
```py
# zombie.py
class Zombie(Enemy):
    def __init__(self,health_points,attack_damage):
        super().__init__(type_of_enemy='Zombie',health_points=health_points,attack_damage=attack_damage)
            # Inheritance

        def talk(self):
            print('*Grumbling...')
            # Method Overriding
        def spread_disease(self):
            print('The zombie is trying to spread infection')
```
```py
# ogre.py
class Ogre(Enemy):
    def __init__(self,health_points,attack_damage):
        super().__init__(type_of_enemy='Ogre',health_points=health_points,attack_damage=attack_damage)
            # Inheritance

        def talk(self):
            print('Ogre is slamming hands all around.')
            # Method Overriding
```
```py
# main.py
from zombie import *
from ogre import *

zombie = Zombie(10,1)
ogre = Ogre(20,3)

print(f'{zombie.get_type_of_enemy()} has '
      f'{zombie.health_points} health points '
      f'and can do attack of {zombie.attack_damage}')

print(f'{ogre.get_type_of_enemy()} has '
      f'{ogre.health_points} health points '
      f'and can do attack of {ogre.attack_damage}')

zombie.talk()
ogre.talk()
```

#### 21. Polymorphism

- many forms aye... the children classes chan still act as the parent (`def battle(e: Enemy): foo`)
- changing an object (`animal`...) at a specific runtime

```py
# classes.py

class Animal:
  # ...
  def talk(self):
    print('Does not make a sound')
class Dog(Animal):
  # ...
  def talk(self):
    print('Bark!')
class Bird(Animal):
  # ...
  def talk(self):
    print('Chirp!')

# ---
# main.py

zoo: Animal=[]

dog = Animal()
dog2 = Dog()
bird = Bird()

# This will work
zoo.apend(dog)
zoo.apend(dog2)
zoo.apend(bird)

for animal in zoo:
  animal.talk()
  # ...
  # Bark!
  # Chirp
```

- create new battle function in `main.py`

```py
from enemy import *
from zombie import *
from ogre import *

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(10,1)
ogre = Ogre(20,3)

print(f'({zombie.get_type_of_enemy()} has '
      f'{zombie.health_points} health points '
      f'and can do attack of {zombie.attack_damage})')

print(f'({ogre.get_type_of_enemy()} has '
      f'{ogre.health_points} health points '
      f'and can do attack of {ogre.attack_damage})')

battle(zombie)
battle(ogre)
```

- create a special attack: default at the parent class, specifics at the children classes (ver [./00-oop_game/](/00-oop_game/))


#### 21. Composition

- Create objects made up of other objects, providing layered functionality
- A class contains one or more objects of another class as instance variables
- Known as a HAS-A relationship (not an IS-A)
- In the example, a vehicle must have an engine, but an engine does not need to have a vehicle

```py
class Engine:
  def __init__(self,engineType):
    self.engineType=engineType
  def startEngine(self):
    print("Engine is running")
  def stopEngine(self):
    print("Engine is off")

class Vehicle:
  def __init__(self,type,forSale,engine):
    self.type=type
    self.forSale=forSale
    self.engine=engine

engine = Engine("V6")
vehicle = Vehicle("Car",True,engine)
vehicle.engine.startEngine()
  # Engine is running
```

- Implementación en [./00-oop_game/](/00-oop_game/)
  - crear clases Hero y Weapon, con una relación HAS-A!!



</details>

<!-- </details> -->

---


## 3. FastAPI Overview

> [!NOTE]
> Ver diapositivas (21-...) en [./docs/FastAPI_slides.pdf](/docs/FastAPI_slides.pdf)

- **[FastAPI](https://fastapi.tiangolo.com/)**: web-framework for building modern RESTful APIs
- **Características**: fast performance and fast development: few bugs, quick & easy, robust, standards ([OpenAPI](https://www.openapis.org/) ([Swagger](https://swagger.io/specification/)) & [JsonSchema](https://json-schema.org/))
- **Roles**: 
  - **FastAPI** handles all business logic for the application. Nowadays any webpage communicates with a server application through RESTful APIs, requesting data from the backend server (business logic). So **FastAPI** ensures the webpage is getting correct and secure data for the users to interact with.
  - **FastAPI** can also leverage additional tools to create full stack applications, where FastAPI also renders the front web page


> [!IMPORTANT]
> En el curso crearemos tanto FastAPI RESTful applications como full stack applications.


## 4. FastAPI Setup & Installation (`pip` & `venv`)

> [!NOTE]
> Ver diapositivas (11-...) en [./docs/FastAPI_slides.pdf](/docs/FastAPI_slides.pdf) <br>
> Ver comandos para instalación en Linux más arriba en '*# 2.1 Intro: ...*'

<!-- - Isolate dependencies (eg. `uvicorn` etc.) thru dedicated environments to maintain lean systems -->

<!-- 
```bash
# Listar pip packages en la workstation (ho lee fuk)
pip list | wc -l
  # 182

# Crear FastAPI project
mkdir project-foo && cd $_
python3 -m venv .fastapivenv

source .venv/bin/activate
pip list | wc -l
  # 2
pip install "fastapi[standard]"
  # ...
pip list | wc -l
  # 38
```
 -->

<!-- 
```bash
pip install "fastapi[standard]"
  # Collecting fastapi[standard]
  #   Using cached fastapi-0.115.2-py3-none-any.whl (94 kB)
  # Collecting typing-extensions>=4.8.0
  #   Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
  # Collecting starlette<0.41.0,>=0.37.2
  #   Using cached starlette-0.40.0-py3-none-any.whl (73 kB)
  # Collecting pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4
  #   Using cached pydantic-2.9.2-py3-none-any.whl (434 kB)
  # Collecting email-validator>=2.0.0
  #   Downloading email_validator-2.2.0-py3-none-any.whl (33 kB)
  # Collecting httpx>=0.23.0
  #   Downloading httpx-0.27.2-py3-none-any.whl (76 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 76.4/76.4 KB 4.0 MB/s eta 0:00:00
  # Collecting uvicorn[standard]>=0.12.0
  #   Downloading uvicorn-0.32.0-py3-none-any.whl (63 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.7/63.7 KB 17.1 MB/s eta 0:00:00
  # Collecting python-multipart>=0.0.7
  #   Downloading python_multipart-0.0.12-py3-none-any.whl (23 kB)
  # Collecting jinja2>=2.11.2
  #   Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 KB 22.2 MB/s eta 0:00:00
  # Collecting fastapi-cli[standard]>=0.0.5
  #   Downloading fastapi_cli-0.0.5-py3-none-any.whl (9.5 kB)
  # Collecting dnspython>=2.0.0
  #   Downloading dnspython-2.7.0-py3-none-any.whl (313 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 313.6/313.6 KB 18.5 MB/s eta 0:00:00
  # Collecting idna>=2.0.0
  #   Using cached idna-3.10-py3-none-any.whl (70 kB)
  # Collecting typer>=0.12.3
  #   Downloading typer-0.12.5-py3-none-any.whl (47 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.3/47.3 KB 26.8 MB/s eta 0:00:00
  # Collecting certifi
  #   Downloading certifi-2024.8.30-py3-none-any.whl (167 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 167.3/167.3 KB 8.7 MB/s eta 0:00:00
  # Collecting sniffio
  #   Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
  # Collecting httpcore==1.*
  #   Downloading httpcore-1.0.6-py3-none-any.whl (78 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.0/78.0 KB 43.0 MB/s eta 0:00:00
  # Collecting anyio
  #   Using cached anyio-4.6.2.post1-py3-none-any.whl (90 kB)
  # Collecting h11<0.15,>=0.13
  #   Downloading h11-0.14.0-py3-none-any.whl (58 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 KB 27.9 MB/s eta 0:00:00
  # Collecting MarkupSafe>=2.0
  #   Downloading MarkupSafe-3.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (20 kB)
  # Collecting pydantic-core==2.23.4
  #   Using cached pydantic_core-2.23.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
  # Collecting annotated-types>=0.6.0
  #   Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
  # Collecting click>=7.0
  #   Using cached click-8.1.7-py3-none-any.whl (97 kB)
  # Collecting watchfiles>=0.13
  #   Downloading watchfiles-0.24.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (425 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 425.7/425.7 KB 82.6 MB/s eta 0:00:00
  # Collecting pyyaml>=5.1
  #   Downloading PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (751 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 751.2/751.2 KB 74.0 MB/s eta 0:00:00
  # Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0
  #   Downloading uvloop-0.21.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.8 MB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 64.3 MB/s eta 0:00:00
  # Collecting httptools>=0.5.0
  #   Downloading httptools-0.6.4-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (442 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 442.1/442.1 KB 32.2 MB/s eta 0:00:00
  # Collecting python-dotenv>=0.13
  #   Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
  # Collecting websockets>=10.4
  #   Downloading websockets-13.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (164 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 164.1/164.1 KB 93.1 MB/s eta 0:00:00
  # Collecting exceptiongroup>=1.0.2
  #   Using cached exceptiongroup-1.2.2-py3-none-any.whl (16 kB)
  # Collecting shellingham>=1.3.0
  #   Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
  # Collecting rich>=10.11.0
  #   Downloading rich-13.9.2-py3-none-any.whl (242 kB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.1/242.1 KB 59.7 MB/s eta 0:00:00
  # Collecting markdown-it-py>=2.2.0
  #   Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
  # Collecting pygments<3.0.0,>=2.13.0
  #   Downloading pygments-2.18.0-py3-none-any.whl (1.2 MB)
  #     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 68.8 MB/s eta 0:00:00
  # Collecting mdurl~=0.1
  #   Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
  # Installing collected packages: websockets, uvloop, typing-extensions, sniffio, shellingham, pyyaml, python-multipart, python-dotenv, pygments, mdurl, MarkupSafe, idna, httptools, h11, exceptiongroup, dnspython, click, certifi, annotated-types, uvicorn, pydantic-core, markdown-it-py, jinja2, httpcore, email-validator, anyio, watchfiles, starlette, rich, pydantic, httpx, typer, fastapi, fastapi-cli
  # Successfully installed MarkupSafe-3.0.2 annotated-types-0.7.0 anyio-4.6.2.post1 certifi-2024.8.30 click-8.1.7 dnspython-2.7.0 email-validator-2.2.0 exceptiongroup-1.2.2 fastapi-0.115.2 fastapi-cli-0.0.5 h11-0.14.0 httpcore-1.0.6 httptools-0.6.4 httpx-0.27.2 idna-3.10 jinja2-3.1.4 markdown-it-py-3.0.0 mdurl-0.1.2 pydantic-2.9.2 pydantic-core-2.23.4 pygments-2.18.0 python-dotenv-1.0.1 python-multipart-0.0.12 pyyaml-6.0.2 rich-13.9.2 shellingham-1.5.4 sniffio-1.3.1 starlette-0.40.0 typer-0.12.5 typing-extensions-4.12.2 uvicorn-0.32.0 uvloop-0.21.0 watchfiles-0.24.0 websockets-13.1

pip list
  # Package           Version
  # ----------------- -----------
  # annotated-types   0.7.0
  # anyio             4.6.2.post1
  # certifi           2024.8.30
  # click             8.1.7
  # dnspython         2.7.0
  # email_validator   2.2.0
  # exceptiongroup    1.2.2
  # fastapi           0.115.2
  # fastapi-cli       0.0.5
  # h11               0.14.0
  # httpcore          1.0.6
  # httptools         0.6.4
  # httpx             0.27.2
  # idna              3.10
  # Jinja2            3.1.4
  # markdown-it-py    3.0.0
  # MarkupSafe        3.0.2
  # mdurl             0.1.2
  # pip               22.0.2
  # pydantic          2.9.2
  # pydantic_core     2.23.4
  # Pygments          2.18.0
  # python-dotenv     1.0.1
  # python-multipart  0.0.12
  # PyYAML            6.0.2
  # rich              13.9.2
  # setuptools        59.6.0
  # shellingham       1.5.4
  # sniffio           1.3.1
  # starlette         0.40.0
  # typer             0.12.5
  # typing_extensions 4.12.2
  # uvicorn           0.32.0
  # uvloop            0.21.0
  # watchfiles        0.24.0
  # websockets        13.1
```
 -->

---

## 5. Project 1 - FastAPI Request Method Logic

> [!TIP]
> Usar Swagger (en `docs/`) para probar las Requests y los Endpoints. También se puede usar `curl`+`jq` en la terminal, o la aplicación de escritorio [Postman](https://learning.postman.com/docs/getting-started/first-steps/get-postman/) <!--Para consultar los endpoints tal cual con el navegador, usar Firefox o para Chrome-based browsers instalar alguna extensión para visualizar JSON...-->


<!-- 
> [!TIP]
> Para consultar los endpoints en el navegador web (al margen de Swagger en `docs/`), usar Firefox o alguna extensión para chrome-based browsers. <br>
> Otras opciones son usar `curl` + `jq` en la terminal ~~(ver [.utils/workstation.sh](#))~~ o la aplicación de escritorio `postman` ~~(instalación de postman!!)~~
 -->

<details>

### 1. Intro

> Diapositivas (26-...)

- Basic HTTP request methods and how to use FastAPI (`uvicorn` being the web server)
- We'll create and enhance a list of books, and them books will have simple key-value pairs
- We'll use **CRUD Operations**: Create, Read, Update and Delete

```py
BOOKS = [
  {'title':'Title One','author':'Author One','category':'science'},
  {'title':'Title Two','author':'Author Two','category':'science'},
  {'title':'Title Three','author':'Author Three','category':'history'},
  {'title':'Title Four','author':'Author Four','category':'math'},
  {'title':'Title Five','author':'Author Five','category':'math'},
]
```

- **Request and Response**: (CRUD) HTTP methods entre la web page y el FastAPI server
- **[Swagger UI](https://swagger.io/)**: built-in URL `/docs`: listar todos los Request Methods disponibles

| CRUD    | HTTP Requests
| ---     | ---
| Create  | POST
| Read    | GET
| Update  | PUT
| Delete  | DELETE

### 2. GET Request 1/2

> OJO:
> - `@app`: *decorator* que ~~en este caso~~ define el endpoint `/api-endpoint` en la URL http://127.0.0.1:8000/api-endpoint tras el comando `uvicorn foo`
> - `async`: optional, explicit for every function-endpoint

```py
# books.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint")
# GET Request
async def first_api():
    return {'message':'Sup Dawg!'}
```

Run FastAPI application (en `.venv`)

```bash
# source .venv/bin/activate

uvicorn --version
  # Running uvicorn 0.32.0 with CPython 3.10.12 on Linux

cd ./01-books-requests

# uvicorn books:app --reload || \
fastapi dev books.py || \
fastapi run books.py

curl localhost:8000/ &&
curl localhost:8000/api-endpoint
  # {"detail":"Not Found"}%
  # {"message":"Sup Dawg!"}%

xdg-open http://localhost:8000/api-endpoint

# deactivate
```

- fastapi `run` vs `dev`:
  - `run`: no live reloading by default
  - `dev`: live reloading, includes `uvicorn` dev features, enhanced error messages, logging, etc.

### 3. GET Request 2/2

```py
# books.py
from fastapi import FastAPI

app = FastAPI()

BOOKS = [
  {'title':'Title One','author':'Author One','category':'science'},
  {'title':'Title Two','author':'Author Two','category':'science'},
  {'title':'Title Three','author':'Author Three','category':'history'},
  {'title':'Title Four','author':'Author Four','category':'math'},
  {'title':'Title Five','author':'Author Five','category':'math'},
  {'title':'Title Six','author':'Author Two','category':'math'},
]

@app.get("/books")
async def read_all_books():
    return BOOKS
```

```bash
# curl -X 'GET' \
#   'http://localhost:8000/books' \
#   -H 'accept: application/json'

curl localhost:8000/books || \
curl -s localhost:8000/books | jq

# Swagger's */docs
xdg-open http://localhost:8000/docs#/default/read_all_books_books_get
  # Try it out > Execute: lo mismo que con curl + jq, pero además headers y curl explícito, ta bien
```

### 4. Path Parameters

> - NOTE: `%20` == space!!
> - Example: `@app.get("/user/{user_id}")`

- Request parameters attached to the URL, a way to find info based on location
- Rutas estáticas o dinámicas mediante parámetros...
- El orden importa, ya que si la función dinámica estuviese primero se aplicaría siempre siempre

```bash
# books.py

@app.get("/books/mybook")
async def read_all_books():
    return {'book_title':'My Favorite Book!'}

# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param:str):
#     return {'dynamic_param':dynamic_param}

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book
```
```bash
curl localhost:8000/books/mybook && \
curl localhost:8000/books/title%20one
  # {"book_title":"My Favorite Book!"}
  # {"title":"Title One","author":"Author One","category":"science"}%                             [10ms][devel][~/repos/FastAPI-The-Complete-Course]$

# curl localhost:8000/books/science
#   # {"dynamic_param":"science"}%
```

### 5. Query Parameters

- Request parameters (key-value pairs) attached after a `?`
- Example: `localhost:8000/books/?category=science`

```py
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold()==book_author.casefold() and \
                book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return
```
```bash
curl "localhost:8000/books/?category=science"
  # [{"title":"Title One","author":"Author One","category":"science"},{"title":"Title Two","author":"Author Two","category":"science"}]%

curl "localhost:8000/books/author%20two/?category=science"
  # [{"title":"Title Two","author":"Author Two","category":"science"}]%
```

### 6. POST Request

> [!TIP]
> In the Request Body, only **double quotes** are valid, not single quotes

- Creates data; includes additional information: a Body ~~that GET can't have~~
- Example: pass `{'title':'Title Seven','author':'Author Two','category':'math'}`

```py
from fastapi import Body, FastAPI

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
```
```bash
curl -X 'POST' 'http://localhost:8000/books/create_book' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"title":"Title Seven","author":"Author Two","category":"math"}'
  # null%

curl localhost:8000/books/title%20seven
  # {"title":"Title Seven","author":"Author Two","category":"math"}%
```

### 7. PUT Request

- Updates data; also has additional info
- For example, change the category of a book

```py
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==updated_book.get('title').casefold():
            BOOKS[i]=updated_book
```
```bash
curl localhost:8000/books/title%20six
  # {"title":"Title Six","author":"Author Two","category":"math"}%

curl -X 'PUT' \
  'http://localhost:8000/books/update_book' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"title":"Title Six","author":"Author Two","category":"history"}'
  # null%

curl localhost:8000/books/title%20six
  # {"title":"Title Six","author":"Author Two","category":"history"}%                                                        [11ms][devel][~/repos/FastAPI-The-Complete-Course]$
```

### 8. DELETE Request

```py
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(i)
            break
```
```bash
curl -s localhost:8000/books | jq '. | length'
  # 6

curl -X 'DELETE' \
  'http://localhost:8000/books/delete_book/title%20four' \
  -H 'accept: application/json'
  # null%

curl -s localhost:8000/books | jq '. | length'
  # 5
```

### 9. *Assignment*

> [!TIP]
> Keep smaller endpoints (fewer params) above, to prevent it from being consumed by a longer endpoint

```py
'''
Create a new API Endpoint that can fetch all books from a specific author
using either Path Parameters or Query Parameters.
'''

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold()==author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_query(author:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold()==author.casefold():
            books_to_return.append(book)
    return books_to_return
```
```bash
curl localhost:8000/books/byauthor/author%20two
  # [{"title":"Title One","author":"Author One","category":"science"}]%                                                      [12ms][devel][~/repos/FastAPI-The-Complete-Course]$

curl localhost:8000/books/byauthor/\?author=author%20one
  # [{"title":"Title One","author":"Author One","category":"science"}]%                                                      [13ms][devel][~/repos/FastAPI-The-Complete-Course]$
```


</details>

---

## 6. Project 2 - Move Fast with FastAPI

> [!IMPORTANT]
> Content: Data Validation, Exception Handling, Status Codes, Swagger Configuration, and Python Requests Objects

<!-- <details> -->

<!--
```md
FastAPI is now compatible with both Pydantic v1 and Pydantic v2.
Based on how new the version of FastAPI you are using, there could be small method name changes.
The three biggest are:
- `.dict()` function is now renamed to `.model_dump()`
- `schema_extra` function within a Config class is now renamed to `json_schema_extra`
- Optional variables need a `=None`; example: `id: Optional[int] = None`
```
-->

### (Swagger, Pydantic, Path & Query Validation)

<details>

#### 1. Intro & Project Setup (`Book` Python Object)

```py
from fastapi import FastAPI

app = FastAPI()

# ---

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

BOOKS=[
    Book(1,'Computer Science Pro','Setenova','A very nice book!',5),
    Book(2,'Be Fast with FastAPI','Setenova','A great book!',5),
    Book(3,'Master Endpoints','Setenova','An awesome book!',5),
    Book(4,'HP1','Author 1','Book Description',2),
    Book(5,'HP2','Author 2','Book Description',3),
    Book(6,'HP3','Author 3','Book Description',1)
]

# ---

@app.get("/books")
async def read_all_books():
    return BOOKS
```
```bash
curl -X 'GET' \
  'http://localhost:8000/books' \
  -H 'accept: application/json'
  # [{"id":1,"title":"Computer Science Pro","author":"Setenova","description":"A very nice book!","rating":5},{"id":2,"title":"Be Fast with FastAPI","author":"Setenova","description":"A great book!","rating":5},{"id":3,"title":"Master Endpoints","author":"Setenova","description":"An awesome book!","rating":5},{"id":4,"title":"HP1","author":"Author 1","description":"Book Description","rating":2},{"id":5,"title":"HP2","author":"Author 2","description":"Book Description","rating":3},{"id":6,"title":"HP3","author":"Author 3","description":"Book Description","rating":1}]%
```

#### 2. POST Request before Validation

Problema: se puede añadir de todo en el POST (eg. un índice o rating de 200 etc.)

```py
from fastapi import Body, FastAPI

# ---

@app.post("/books/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
```
```bash
curl -X 'POST' \
  'http://localhost:8000/books/create-book' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '  {
    "id": 7,
    "title": "HP4",
    "author": "Author 3",
    "description": "Book Description",
    "rating": 1
  }'
```


#### 3. Book Request Data Validation (**pydantic**)

> [!TIP]
> En Swagger, ahora habrá una plantilla (con data types etc.) en el POST!!

- **[pydantics](https://docs.pydantic.dev/latest/)**: data library for data modelling, data parsing and has efficient error handling
- Procedimiento:
  - create different request model for data validation
  - field data validation on each variable/element
  - we'll convert the Pydantics Request into a Book object

> NOTE: `**` operator: will pass the key/value from BookRequest() into the Book() constructor

```py
from fastapi import FastAPI # ,Body
from pydantic import BaseModel

class BookRequest(BaseModel):
    id:int
    title:str       #=Field(min_length=3)
    author:str      #=Field(min_length=1)
    description:str #=Field(min_length=3,max_length=100)
    rating:int      #=Field(gt=0,lt=5)

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
```

#### 4. Fields - Data Validation

- **Objetivo 1**: asegurarnos de que los datos de POST son válidos
- Poner a prueba la POST incumpliendo las reglas de `Field()`: `422 Error: Unprocessable Entity`
- **Objetivo 2**: automatizar índices incrementales

```py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

class BookRequest(BaseModel):
    id:Optional[int] =None
    title:str =Field(min_length=3)
    author:str =Field(min_length=1)
    description:str =Field(min_length=3,max_length=100)
    rating:int =Field(gt=0,lt=6)

# @app.post("/create-book")
def find_book_id(book:Book):
    # if len(BOOKS)>0:
    #     book.id=BOOKS[-1].id+1
    # else:
    #     book.id=1
    book.id=1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return book
```
```bash
curl -X 'GET' 'http://localhost:8000/books'
# [{"id":1,"title":"Computer Science Pro","author":"Setenova","description":"A very nice book!","rating":5},[...],{"id":6,"title":"HP3","author":"Author 3","description":"Book Description","rating":1}%

curl -X 'POST' \
  'http://localhost:8000/create-book' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"title":"string","author":"string","description":"string","rating": 1}'

curl -X 'GET' 'http://localhost:8000/books'
# [{"id":1,"title":"Computer Science Pro","author":"Setenova","description":"A very nice book!","rating":5},[...],{"id":7,"title":"string","author":"string","description":"string","rating":1}]%
```

![/docs/img/02-post-schema.png](/docs/img/02-post-schema.png)

#### 5. Pydantic Configurations (Swagger defaults)

- Swagger > POST > Example Value

```py
class BookRequest(BaseModel):
    id:Optional[int] =Field(description='ID is not needed on POST',default=None)
    title:str =Field(min_length=3)
    author:str =Field(min_length=1)
    description:str =Field(min_length=3,max_length=100)
    rating:int =Field(gt=0,lt=6)

    model_config={
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"pabloqpacin",
                "description":"A new description of a book",
                "rating":5
            }
        }
    }
```

#### 6. Fetch Book

- new endpoint: find books based on their ID

```py
@app.get("/books/{book_id}")
async def read_book_by_id(book_id:int):
    for book in BOOKS:
        if book.id==book_id:
            return book
```
```bash
curl -X 'GET' \
  'http://localhost:8000/books/5' \
  -H 'accept: application/json'
  # {"id":5,"title":"HP2","author":"Author 2","description":"Book Description","rating":3}%
```

#### 7. Fetch Books by Rating

- new endpoint: find books querying ratings (filter by rating)
- tener en cuenta el orden (posibles conflictos entre endpoints)

```py
@app.get("/books/")
async def read_book_by_rating(book_rating:int):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return
```
```bash
curl -X 'GET' \
  'http://localhost:8000/books/?book_rating=5' \
  -H 'accept: application/json'
  # [{"id":1,"title":"Computer Science Pro","author":"Setenova","description":"A very nice book!","rating":5},{"id":2,"title":"Be Fast with FastAPI","author":"Setenova","description":"A great book!","rating":5},{"id":3,"title":"Master Endpoints","author":"Setenova","description":"An awesome book!","rating":5}]%
```

#### 8. Update Book with PUT Request

- ojo: aquí el ID sería necesario
- ojo: luego haremos Error Handling para que no se pueda actualizar un id 100 inexistente etc.

```py
@app.put("/update-book")
async def update_book_by_id(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
```
```bash
curl 'http://localhost:8000/books/3'
  # {"id":3,"title":"Master Endpoints","author":"Setenova","description":"An awesome book!","rating":5}%

curl -X 'PUT' \
  'http://localhost:8000/update-book' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"id":3,"title":"Endpoints Master","author":"Setenova","description":"An awesome book!","rating":5}'

curl 'http://localhost:8000/books/3'
  # {"id":3,"title":"Endpoints Master","author":"Setenova","description":"An awesome book!","rating":5}%
```

#### 9. Delete Book with DELETE Request

```py
@app.delete("/books/{book_id}")
async def delete_book_by_id(book_id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            break
```
```bash
curl 'http://localhost:8000/books/2'
  # {"id":2,"title":"Be Fast with FastAPI","author":"Setenova","description":"A great book!","rating":5}%

curl -X 'DELETE' \
  'http://localhost:8000/books/2' \
  -H 'accept: application/json'

curl 'http://localhost:8000/books/2'
  # null%
```

#### 10. Assignment

```py
'''
- Add a new field to Book and BookRequest called published_date: int (for example, published_date: int = 2012). So, this book as published on the year of 2012.
- Enhance each Book to now have a published_date
- Then create a new GET Request method to filter by published_date
'''

# ...

@app.get("/books/publish/")
async def read_book_by_publish_date(published_date:int):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date==published_date:
            books_to_return.append(book)
    return books_to_return
```
```bash
curl -X 'GET' \
  'http://localhost:8000/books/publish/?published_date=1984' \
  -H 'accept: application/json'
  # [{"id":6,"title":"HP3","author":"Author 3","description":"Book Description","published_date":1984,"rating":1}]%
```

#### 11. Data Validation: Path Parameters

- atm we only have validation on the BookRequest class, but not on the endpoints (eg. a book doesn't exist, validation to the book IDs)
- verify: search book with id 0 or delete book with id -1: `422	Error: Unprocessable Entity`

```py
from fastapi import FastAPI, Path

async def read_book_by_id(book_id:int =Path(gt=0)):
  # ...

# ...
async def delete_book_by_id(book_id:int =Path(gt=0)):
  # ...
```

#### 12. Data Validation: Query Parameters

- verificar: buscar con rating 7, o con fecha 12345

```py
from fastapi import FastAPI, Path, Query

# ...
async def read_book_by_rating(book_rating:int =Query(gt=0,lt=6)):
  # ...

# ...
async def read_book_by_publish_date(published_date:int =Query(lt=9999)):
  # ...
```

</details>


### (HTTP Status Codes)

<details>

#### 13. Status Codes Overview

>[!IMPORTANT]
> HTTP Status Codes 101

<!-- >[!NOTE]
> Diapositivas 61-... -->

- international standards on how a client/server should handle the result of a request

| Code  | Meaning
| ---   | ---
| 1xx   | Information Response: request processing
| 2xx   | Success: request sucessfully complete
| 3xx   | Redirection: further action must be complete
| 4xx   | Client Errors: an error was caused by the client
| 5xx   | Server Errors: an error occurred on the server

| Code  | Meaning               | Description
| ---   | ---                   | ---
|       |
| 200   | OK                    | Successful GET with data returned
| 201   | Created               | Sucessful POST
| 204   | No Content            | Sucessful PUT with no data returned or created
|       |
| 400   | Bad Request           | Invalid request methods, can't be processed bc client error
| 401   | Unauthorized          | Client lacks valid authentication for target resource
| 404   | Not Found             | Client's requested resource not found
| 422   | Unprocessable Entity  | Semantic errors in client request
|       |
| 500   | Internal Server Error | Generic message for unexpected issues on the server


#### 14. HTTP Exceptions

- "An HTTP exception is something that we have to raise within our method, which will cancel the functionality of our method and return a message in a status code back to our user"

```py
from fastapi import FastAPI, Path, Query, HTTPException

# ...
    raise HTTPException(status_code=404, detail='Item not found')


# ...
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

```
```bash
curl -X 'GET' \
  'http://localhost:8000/books/999' \
  -H 'accept: application/json'
  # {"detail":"Item not found"}%
```

#### 15. Explicit Status Code Responses

```py
from starlette import status

@app.get("/books",status_code=status.HTTP_200_OK)
@app.get("/books/{book_id}",status_code=status.HTTP_200_OK)
@app.get("/books/",status_code=status.HTTP_200_OK)
@app.get("/books/publish/",status_code=status.HTTP_200_OK)

@app.post("/create-book",status_code=status.HTTP_201_CREATED)
@app.put("/update-book",status_code=status.HTTP_204_NO_CONTENT)
@app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
```
```bash
curl -v -X 'DELETE' \
  'http://localhost:8000/books/1' \
  -H 'accept: */*'
  # ...
  # < HTTP/1.1 204 No Content

curl -v -X 'DELETE' \
  'http://localhost:8000/books/1' \
  -H 'accept: */*'
  # ...
  # < HTTP/1.1 404 Not Found

# ... -X 'POST' ...
# ... -X 'PUT' ...
```


</details>

---

## 7. Project 3 - Complete RESTful APIs

- Content 1/2:
  - full SQL Database: SQLite, PostreSQL & MySQL (WIP: Dockerized!!!!)
  - Authentication: create usernames+passwords (JWT)
  - Authorization: roles/permissions for endpoints
  - Hashing Passwords
- Content 2/2:
  - TODOS instead of BOOKS
  - create new TODO Table Model for the application
  - using TODOs to save records throughout the project

```mermaid
flowchart LR;

Webpage -. auth .-> FastAPI
FastAPI -. fetch users & save TODOs .-> Database
```

---

## 8. (7.1) Setup Database <!--(*Dockerized* PostgreSQL)-->

<details>

<!-- > db mysql - https://github.com/pabloqpacin/proyecto_lemp_compose/blob/main/compose.yaml -->


#### 1. Intro

- **Database**: easily accessible, modifiable, controlled and organized; atm we use SQL
- **Data**: info related to objects (eg. user: name,age,email,password)
- **Database Management Systems (DBMS)**: SQLite, MySQL, PostreSQL
- **SQL**: relational DBs with tables etc.
- ~~**Usecase**: store, retrieve and modify data~~


#### 2. DB Connection with ORM SQLAlchemy

- Instalar [SQLAlchemy](https://www.sqlalchemy.org/) en el `.venv`

```bash
# source .venv/bin/activate

pip install sqlalchemy
  # ...
  # Successfully installed greenlet-3.1.1 sqlalchemy-2.0.36
```

- Crear [./database.py](/03-todos-database/database.py)
<!-- # Create a session local ~~(will be object)~~, and each instance will have its own session -->

```py
# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL='sqlite:///./todos.db'

# SQLite only allows one thread per request by default to prevent accidents sharing a connection with multiple requests, but it's common to have many threads interacting with the DB... therefore we have SQLite not check the same thread because there could be many
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
```

#### 3. DB Tables (Models)

- TODO Tables Example (**modelado de datos**)

| ID (PK) | title               | description | priority  | complete
| ---     | ---                 | ---         | ---       | ---
| 1       | Go to store         | foo         | 4         | 0
| 2       | Haircut             | foo         | 3         | 0
| 3       | Feed dog            | foo         | 5         | 0
| 4       | Water plant         | foo         | 4         | 0
| 5       | Learn something new | foo         | 5         | 0


- Create [.models.py](/03-todos-database/models.py)

```py
# models.py

from database import Base
from sqlalchemy import Column,Integer,String,Boolean

# Table
class Todos(Base):
    __tablename__='todos'
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)
```

#### 4. main: DB Conn. for API & init

```py
# main.py

from fastapi import FastAPI
from database import engine
import models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
```
```bash
# cd 03-todos-database

fastapi dev main.py || \
uvicorn main:app --reload

file ./todos.db
  # todos.db: SQLite 3.x database, last written using SQLite version 3037002, file counter 2, database pages 3, cookie 0x2, schema 4, UTF-8, version-valid-for 2
```

#### 5. SQLite3 Installation
 
```bash
# docker compose up ... || \
# docker run ... || \

sudo apt install sqlite -y
  # 3 pkgs
```

#### 6. SQL Queries Crash-Course

Ejemplos de SQL...

```sql
-- Insert data
insert into todos (title,description,priority,complete) values (
  'Go to store','foo',4,False
);

-- Select data
select * from todos where priority=5;

select title,description,priority from todos
  where complete=False
;

-- Update data
update todos set complete=True where id=5;

-- Delete data
delete from todos where complete=False;
delete from todos where id=5;
```

#### 7. SQLite3 Setup: TODOs

```bash
sqlite3 todos.db ".schema"
  # CREATE TABLE todos (
  #         id INTEGER NOT NULL,
  #         title VARCHAR,
  #         description VARCHAR,
  #         priority INTEGER,
  #         complete BOOLEAN,
  #         PRIMARY KEY (id)
  # );
  # CREATE INDEX ix_todos_id ON todos (id);

sqlite3 todos.db "insert into todos (title,description,priority,complete) values
  ('Go to store','foo',4,False),
  ('Haircut','foo',3,False),
  ('Feed dog','foo',5,False),
  ('Water plant','foo',4,False),
  ('Learn something new','foo',5,False)
;"

sqlite3 todos.db "select * from todos;"
  # 1|Go to store|foo|4|0
  # 2|Haircut|foo|3|0
  # 3|Feed dog|foo|5|0
  # 4|Water plant|foo|4|0
  # 5|Learn something new|foo|5|0

sqlite3 todos.db { -column || -markdown || -box || -table } "select * from todos;"
  # ...
```



</details>

## 9. (7.2) API Request CRUD Methods

<details>

#### 1. GET All Todos from DB

- Connection via dependency injection

```py
# main.py

from fastapi import FastAPI, Depends
from database import engine, SessionLocal
import models
from models import Todos
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# ---

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@app.get("/")
async def read_all(db:db_dependency):
    return db.query(Todos).all()
```
```bash
curl http://localhost:8000/
  # [{"description":"foo","complete":false,"id":1,"priority":4,"title":"Go to store"},{"description":"foo","complete":false,"id":2,"priority":3,"title":"Haircut"},{"description":"foo","complete":false,"id":3,"priority":5,"title":"Feed dog"},{"description":"foo","complete":false,"id":4,"priority":4,"title":"Water plant"},{"description":"foo","complete":false,"id":5,"priority":5,"title":"Learn something new"}]%
```

#### 2. GET Todo by ID

```py
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status

@app.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency,todo_id:int =Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found.')
```
```bash
curl http://localhost:8000/todo/2
  # {"title":"Haircut","priority":3,"description":"foo","id":2,"complete":false}%

curl http://localhost:8000/todo/22
  # {"detail":"Todo not found."}%

curl http://localhost:8000/todo/-2
  # {"detail":[{"type":"greater_than","loc":["path","todo_id"],"msg":"Input should be greater than 0","input":"-2","ctx":{"gt":0}}]}%
```

#### 3. POST Request

- We don't pass ID in the Request

```py
from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    title:str =Field(min_length=3)
    description:str =Field(min_length=3,max_length=100)
    priority:int =Field(gt=0,lt=6)
    complete:bool

@app.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model = Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
```
```bash
curl localhost:8000
  # [{"description":"foo","id":1,"complete":false,"priority":4,"title":"Go to store"},{"description":"foo","id":2,"complete":false,"priority":3,"title":"Haircut"},{"description":"foo","id":3,"complete":false,"priority":5,"title":"Feed dog"},{"description":"foo","id":4,"complete":false,"priority":4,"title":"Water plant"},{"description":"foo","id":5,"complete":false,"priority":5,"title":"Learn something new"}]%

curl -X 'POST' \
  'http://localhost:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Learn FastAPI",
  "description": "bar",
  "priority": 4,
  "complete": false
}'
  # null%

curl localhost:8000
  # [{"description":"foo","id":1,"complete":false,"priority":4,"title":"Go to store"},{"description":"foo","id":2,"complete":false,"priority":3,"title":"Haircut"},{"description":"foo","id":3,"complete":false,"priority":5,"title":"Feed dog"},{"description":"foo","id":4,"complete":false,"priority":4,"title":"Water plant"},{"description":"foo","id":5,"complete":false,"priority":5,"title":"Learn something new"},{"description":"bar","id":6,"complete":false,"priority":4,"title":"Learn FastAPI"}]%
```

#### 4. PUT Request

```py
@app.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,
                      todo_request:TodoRequest,
                      todo_id:int =Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    
    todo_model.title=todo_request.title
    todo_model.description=todo_request.description
    todo_model.priority=todo_request.priority
    todo_model.complete=todo_request.complete

    db.add(todo_model)
    db.commit()
```
```bash
curl localhost:8000/todo/3
  # {"description":"foo","complete":false,"id":3,"priority":5,"title":"Feed dog"}%

curl -X 'PUT' \
  'http://localhost:8000/todo/3' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{"description":"foo","complete":false,"priority":5,"title":"Feed cat"}'

curl localhost:8000/todo/3
  # {"description":"foo","complete":false,"id":3,"priority":5,"title":"Feed cat"}%
```

#### 5. DELETE Request

```py
@app.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int =Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
```
```bash
curl localhost:8000/todo/2
  # {"description":"foo","complete":false,"id":2,"priority":3,"title":"Haircut"}%

curl -X 'DELETE' \
  'http://localhost:8000/todo/2' \
  -H 'accept: */*'

curl localhost:8000/todo/2
  # {"detail":"Todo not found."}%
```


</details>



## 10. (7.3) Authentication & Authorization (JWT)

<!-- AUTOPOPULATE SQLITE!?!?! -->

> - For each API request, a user will have their ID attached via JWT
> - Thus we can validate the JWT to use the ID and return any todos relevant to the FK!!

<details>


#### 1. Routers: todos.py & auth.py

- **routers**: a way to have our main file (root of our app) interact with other API files/endpoints...
- create [./routers/todos.py](/03-todos-database/routers/todos.py) for [./main.py](/03-todos-database/main.py)'s Todos logic (*refactor*), and create [./routers/auth.py](/03-todos-database/routers/auth.py) (verificar endpoints en Swagger)


```py
# main.py

from fastapi import FastAPI
from database import engine
import models
from routers import auth, todos


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
```
```py
# routers/todos.py

# ...
```
```py
# routers/auth.py

from fastapi import APIRouter

router = APIRouter()

# ---

@router.get("/auth/")
async def get_user():
    return {'user':'authenticated'}
```

#### 2. One-To-Many Relationship (mind FKs)

- example Users table

| ID (PK) | email           | username  | first_name  | last_name | hashed_password | is_active
| ---     | ---             | ---       | ---         | ---       | ---             | ---
| 1       | foo@example.com | foo       | foo         | example   | 123abc          | 1
| 2       | bar@example.com | bar       | bar         | example   | 123xyz          | 1

- relationship users ~ todos
  - 1 user > n todos
  - 1 todo > 1 user

```mermaid
erDiagram

user ||--o{ todo : has
user{
  int id PK
  str email
  str username
  str first_name
  str last_name
  str hashed_password
  bool is_active
  str role
}
todo {
  int id PK
  str title
  str description
  int priority
  bool complete
  int owner FK
}
```

- **FK**: column in a table that references a PK on a second table to establish a link
  - we'll get associate each request with a user id via JWT, and retrieve relevant todos based on their FK


#### 3. Rename SQLite DB, create Users table, add FK to Todos table

> [!IMPORTANT]
> Later on, we'll use Alembic to 'enhance/populate' tables (SQLAlchemy can only create'em)

- rename our SQLite DB from `todos.db` to `todosapp.db` at [./database.py](/03-todos-database/database.py)
- at [./models.py](/03-todos-database/models.py), create new `users` table and add FK to `todos` table

```py
# database.py

SQLALCHEMY_DATABASE_URL='sqlite:///./todosapp.db'
```
```py
# models.py

from database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

# Table
class Users(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True)
    username=Column(String,unique=True)
    first_name=Column(String)
    last_name=Column(String)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)
    role=Column(String)

# Table
class Todos(Base):
    __tablename__='todos'
    # ...
    owner_id=Column(Integer,ForeignKey("users.id"))
```

#### 4. create_users endpoint, hashed passwords (*passlib* + *bcrypt*)

> [!CAUTION]
> Passlib requires a deprecated version of Bcrypt, hence we should not use passlib ([src](https://github.com/pyca/bcrypt/issues/684#issuecomment-1902590553))

- Install passlib and bcrypt ~~([src](https://passlib.readthedocs.io/en/stable/install.html))~~

```bash
# source .venv/bin/activate

# pip install "passlib[bcrypt]" || \
pip install passlib
pip install bcrypt==4.0.1

# pip list | wc -l
#   # 42
```
<!--
(trapped) error reading bcrypt version
Traceback (most recent call last):
  File "/home/pabloqpacin/repos/FastAPI-The-Complete-Course/.venv/lib/python3.10/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_backend_mixin
    version = _bcrypt.__about__.__version__
AttributeError: module 'bcrypt' has no attribute '__about__'

https://github.com/pyca/bcrypt/issues/684#issuecomment-1902590553
...
-->

- Update [./routers/auth.py](/03-todos-database/routers/auth.py) for a `create_user` endpoint!

```py
from fastapi import APIRouter
from pydantic import BaseModel
from models import Users
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class CreateUserRequest(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    password:str
    role:str

# ---

@router.post("/auth")
async def create_user(create_user_request:CreateUserRequest,):
    # create_user_model = Users(**create_user_request.model_dump()) # won't work bc password, not hashed_password
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True
    )
    return create_user_model
```

```bash
curl -X 'POST' \
  'http://localhost:8000/auth' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "foo",
  "email": "foo@example.com",
  "first_name": "foo",
  "last_name": "example",
  "password": "123abc",
  "role": "admin"
}'
  # {"username":"foo","email":"foo@example.com","first_name":"foo","last_name":"example","hashed_password":"$2b$12$2sgedDcNpk6wfBxvEFmQ7ONU41ISa/TJWu55er8RPGO1ID1hqEXEW","role":"admin","is_active":true}%
```

#### 5. Save User to DB

- modificar [./auth.py](/03-todos-database/routers/auth.py)

```py
from fastapi import APIRouter, Depends
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]
```
```bash
curl -X 'POST' \
  'http://localhost:8000/auth' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "foo",
  "email": "foo@example.com",
  "first_name": "foo",
  "last_name": "example",
  "password": "123abc",
  "role": "admin"
}'
  # null%

sqlite3 todosapp.db "select * from users;"
  # 1|foo@example.com|foo|foo|example|$2b$12$7FEvQoIB77yV7vAFlAYYIOia5MI7nFjMzorsIJSC5NoT.r526w2SC|1|admin
```

#### 6. Authenticate User (`python-multipart` + `OAuth2PasswordRequestForm`)

- Instalar [python-multipart](https://multipart.fastapiexpert.com/) (en el `.venv`) si no está instalado (debería)

```bash
# source .venv/bin/activate

if ! pip list | grep 'python-multipart'; then
  pip install python-multipart
fi
```

- Edit `auth.py` to fill **a user-pass form in Swagger** (or just use proper `curl`)

```py
# routers/auth.py

from fastapi.security import OAuth2PasswordRequestForm

def authenticate_user(username:str,password:str,db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

@router.post("/token")
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        return 'Failed Authentication'
    return 'Succesful Authentication'

    return form_data.username
```
```bash
curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=a&password=a&scope=&client_id=&client_secret='
  # "Failed Authentication"%

curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=foo&password=123abc&scope=&client_id=&client_secret='
  # "Succesful Authentication"%
```

#### 7. JSON Web Token (JWT) Overview

> [Introduction to JSON Web Tokens](https://jwt.io/introduction)

- **JWT**: self-contained way to securely transmit data and information between two parties using a JSON Object; digitally signed therefore trusted by the server; used for Authorization, not Authentication
- **Process**: user logs in > server returns encoded str JWT; client sends request > authentication > sends JWT for validation (each time)
- **Structure**: `header.payload.signature`
  - `header`: two parts `alg` for signing algorithm, `typ` for token type (eg. `{"alg":"HS256","typ":"JWT"}`) encoded using *Base64*
  - `payload`: actual data aka claims (3 types of claims), also encoded with Base64
    - *[Registered](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1)*: predefined, recommended but not mandatory (eg. `iss`, `exp` about 1h, `sub` as if ID)
    - *Public*
    - *Private*
  - `signature`: is created using the `alg` in the header to hash out the encoder header, encoded payload and a secret (...)
- Example:


```json
// JWT Header
{
  "alg": "HS256",
  "typ": "JWT"
}
```

```json
// JWT Payload
{
  "sub": "1234567890",
  "username": "foo",
  "email": "foo@example.com"
}
```
```ts
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```
```ts
// JSON Web Token
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

- **Outcome**: unique JSON Web Token string based on the authentication, sent by the requester in the authorization header using the [bearer schema](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/) (different than the basic authentication...)
- **Ojo**: never send anything back to the client; JWT is safe as long as client doesn't know the secret key
- **Usecase**: two apps (same provider) share the same secret, so two servers can handle decoding and authorization

> CLEARLY RELEVANT FOR **MICROSERVICES**

#### 8. Encode a JWT

<!-- 
> [!TIP]
> Está [jwt.io](https://jwt.io/) pero vamos a usar [jwt-cli](https://github.com/mike-engel/jwt-cli) para automatizar y tal
> ```
> cargo install jwt-cli
 -->

- **objective**: return JWT if `login_for_access_token` is successful
- install [python-jose](https://pypi.org/project/python-jose/)

```bash
pip install "python-jose[cryptography]"
  # Successfully installed cffi-1.17.1 cryptography-43.0.3 ecdsa-0.19.0 pyasn1-0.6.1 pycparser-2.22 python-jose-3.3.0 rsa-4.9 six-1.16.0
```

- tweak `auth.py`

```py
from datetime import timedelta
from jose import jwt

    # openssl rand -hex 32
SECRET_KEY='a3f34163c39774c189289aacc2629768423f54a0fe55c8058714b3c976ca984a'
ALGORITHM='HS256'

class Token(BaseModel):
    access_token:str
    token_type:str

def create_access_token(username:str,user_id:int,expires_delta:timedelta):
    encode={'sub':username,'id':user_id}
    expires=datetime.now(timezone.utc)+expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

# ---

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
    # ...
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {'access_token':token,'token_type':'bearer'}
```
```bash
curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=a&password=a&scope=&client_id=&client_secret='
  # "Failed Authentication"%

curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=foo&password=123abc&scope=&client_id=&client_secret='
  # {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJpZCI6MSwiZXhwIjoxNzI5NTQ5MzMyfQ.sPDGxrfsrhkquQ2rMxMys9yg2MU_5Eoon8asLXZ1oFY","token_type":"bearer"}%
```

- verify with jwt-cli

```bash
cargo install jwt-cli

BEARER_TOKEN=$(curl -s -X 'POST' \
  'http://localhost:8000/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=foo&password=123abc&scope=&client_id=&client_secret=' \
| jq -r '.access_token')

jwt decode $bearer_token
  #
  # Token header
  # ------------
  # {
  #   "typ": "JWT",
  #   "alg": "HS256"
  # }
  #
  # Token claims
  # ------------
  # {
  #   "exp": 1729549524,
  #   "id": 1,
  #   "sub": "foo"
  # }
```



#### 9. Decode a JWT

- **Recap**: user logs in with user-pass returning a JWT > verify JWT to authenticate to API endpoints

```py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError

# Verify the token as a dependency in our API requests
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        return {'username':username,'id':user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')
```



#### 10. Authentication Enhancements

- separate endpoints on the Swagger Web UI

```py
# routers/auth.py

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

@router.post("/",status_code=status.HTTP_201_CREATED)
```

</details>

## 11. (7.4) Authenticate Requests

<details>

> - básicamente modificar [routers/todos.py](/03-todos-database/routers/todos.py) para establecer autenticación


#### 0. CUSTOM: tweak `auth.py` for authentication with `curl`

- probarlo en el siguiente apartado de Todos...

```py
# auth.py

async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        if username is None or user_id is None:
            raise credentials_exception
        return {"username":username,"id":user_id}
    except JWTError:
        raise credentials_exception

@router.post("/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"},
        )
    access_token_expires=timedelta(minutes=20)
    access_token=create_access_token(user.username,user.id,access_token_expires)
    return {"access_token":access_token,"token_type":"bearer"}
```

#### 1. POST Todo (user_id)

> [!TIP]
> En Swagger, pinchar el icono del candado en POST `/todo` para autenticarse!!

```py
from .auth import get_current_user

user_dependency=Annotated[dict,Depends(get_current_user)]

@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(user:user_dependency,
                      db:db_dependency,todo_request:TodoRequest):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model = Todos(**todo_request.model_dump(),owner_id=user.get('id'))
    db.add(todo_model)
    db.commit()
```
```bash
curl -X 'POST' \
  'http://localhost:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "sup",
  "description": "dawg",
  "priority": 1,
  "complete": true
}'
  # {"detail":"Not authenticated"}%

  # Authenticate via Swagger UI
curl -X 'POST' \
  'http://localhost:8000/todo' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJpZCI6MSwiZXhwIjoxNzI5NjIyODU3fQ.fwC5rrX2l2cqfmkrwXOOSziU45R5UYnYWwXPjv6wLCI' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "sup",
  "description": "dawg",
  "priority": 1,
  "complete": true
}'
  # null%
```
```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
)

curl -X 'POST' \
  'http://localhost:8000/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "sup",
  "description": "dawg",
  "priority": 1,
  "complete": true
}'
  # null%   # 201 Created
```

#### 2. GET all Todos (user_id)

```py
@router.get("/")
async def read_all(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return db.query(Todos).filter(Todos.owner_id==user.get('id')).all()
```
```bash
curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json'
  # {"detail":"Not authenticated"}%

TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"priority":1,"title":"sup","description":"dawg","owner_id":1,"id":1,"complete":true},{"priority":1,"title":"sup","description":"dawg","owner_id":1,"id":2,"complete":true},{"priority":1,"title":"sup","description":"dawg","owner_id":1,"id":3,"complete":true}]%
```

#### 3. GET Todo (id + user_id)

```py
@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(user:user_dependency,db:db_dependency,todo_id:int =Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id==user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found.')
```
```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/todo/2' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # {"description":"dawg","title":"sup","priority":1,"owner_id":1,"id":2,"complete":true}%
```

#### 4. PUT Todo (user_id)

```py
@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependency,db:db_dependency,
                      todo_request:TodoRequest,
                      todo_id:int =Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id==user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    # ...
```
```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'PUT' \
  'http://localhost:8000/todo/2' \
  -H 'accept: */*' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "sup",
  "description": "dawg",
  "priority": 5,
  "complete": true
}'
  # # 204 No Content

curl -X 'GET' \
  'http://localhost:8000/todo/2' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # {"description":"dawg","title":"sup","priority":5,"owner_id":1,"id":2,"complete":true}%
```

#### 5. DELETE Todo (user_id)

```py
@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency,todo_id:int =Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model = db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id==user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    db.query(Todos).filter(Todos.id == todo_id)\
        .filter(Todos.owner_id==user.get('id')).delete()
    db.commit()
```
```bash
curl -X 'DELETE' \
  'http://localhost:8000/todo/2' \
  -H 'accept: */*' \
  -H "Authorization: Bearer $TOKEN"
  # # 204 No Content

curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"priority":1,"title":"sup","description":"dawg","owner_id":1,"id":1,"complete":true},{"priority":1,"title":"sup","description":"dawg","owner_id":1,"id":3,"complete":true}]%
```

#### 6. Admin Router

- Crear rol admin para que ciertos usuarios puedan ver todos los Todos etc.

```py
# routers/auth.py

def create_access_token(username:str,user_id:int,role:str,expires_delta:timedelta):
    encode={'sub':username,'id':user_id,'role':role}

# async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
        user_role:str=payload.get('role')
        return {"username":username,"id":user_id,'user_role':user_role}

# @router.post("/token",response_model=Token)
    access_token=create_access_token(user.username,user.id,user.role,access_token_expires)
```
```py
# routers/admin.py

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from .auth import get_current_user
from database import SessionLocal
from models import Todos

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

# ---

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]

# ---

@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user:user_dependency,db:db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return db.query(Todos).all()
```
```py
# main.py
from routers import auth, todos, admin
app.include_router(admin.router)
```

- Pruebas: tenemos usuario `foo` que es `admin`, creamos usuario `bar` sin rol, creamos un Todo de este nuevo usuario, y luego como ambos usuarios probamos a leer todos los todos (en `/` correspondientes al usuario) y todos los todos del nuevo endpoint `/admin/todo`

```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/admin/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"description":"dawg","title":"sup","priority":1,"owner_id":1,"id":1,"complete":true}]%
```
```bash
curl -X 'POST' \
  'http://localhost:8000/auth/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "bar",
  "email": "bar@example.com",
  "first_name": "bar",
  "last_name": "example",
  "password": "123xyz",
  "role": ""
}'
  # null%

TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=bar&password=123xyz' \
  | jq -r .access_token
) && \
curl -X 'POST' \
  'http://localhost:8000/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "bar",
  "description": "bar",
  "priority": 1,
  "complete": false
}'
  # null%

curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"description":"bar","title":"bar","priority":1,"owner_id":2,"id":2,"complete":false}]%

curl -X 'GET' \
  'http://localhost:8000/admin/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # {"detail":"Authentication Failed"}%

# ---

TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"description":"dawg","title":"sup","priority":1,"owner_id":1,"id":1,"complete":true}]%

curl -X 'GET' \
  'http://localhost:8000/admin/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"description":"dawg","title":"sup","priority":1,"owner_id":1,"id":1,"complete":true},{"description":"bar","title":"bar","priority":1,"owner_id":2,"id":2,"complete":false}]%
```

- Crear y probar otro endpoint para DELETE

```py
# routers/admin.py

@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency,todo_id:int =Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401,detail='Authentication Failed')
    todo_model = db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='Todo not found.')
    db.query(Todos).filter(Todos.id==todo_id).delete()
    db.commit()
```
```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/admin/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"title":"sup","priority":1,"description":"dawg","owner_id":1,"complete":true,"id":1},{"title":"bar","priority":1,"description":"bar","owner_id":2,"complete":false,"id":2}]%

curl -X 'DELETE' \
  'http://localhost:8000/admin/todo/2' \
  -H 'accept: */*' \
  -H "Authorization: Bearer $TOKEN"

curl -X 'GET' \
  'http://localhost:8000/admin/todo' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # [{"title":"sup","priority":1,"description":"dawg","owner_id":1,"complete":true,"id":1}]%
```



#### 7. Assignment

- User provides old_password and new_password, we first need to verify the old_password and then do the update > crear clase *pydantic* `UserVerification(BaseModel)`

```md
1. Create a new route called Users.
2. Then create 2 new API Endpoints:
  - get_user: this endpoint should return all information about the user that is currently logged in.
  - change_password: this endpoint should allow a user to change their current password.
```

```py
# routers/users.py
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status

from .auth import get_current_user
from database import SessionLocal
from models import Users, Todos

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# ---

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class UserVerification(BaseModel):
    password:str
    new_password:str =Field(min_length=6)

# ---

@router.get("/",status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()

# ===== PUT =====

@router.put("/password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user:user_dependency,db:db_dependency,
                          user_verification:UserVerification):
    if user is None:
        raise HTTPException(status_code=401,detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id==user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password,user_model.hashed_password):
        raise HTTPException(status_code=401,detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()
```
```py
# main.py
from routers import auth, admin, users, todos
app.include_router(users.router)
```

```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # {"username":"foo","last_name":"example","id":1,"is_active":true,"first_name":"foo","email":"foo@example.com","hashed_password":"$2b$12$7FEvQoIB77yV7vAFlAYYIOia5MI7nFjMzorsIJSC5NoT.r526w2SC","role":"admin"}%

curl -X 'PUT' \
  'http://localhost:8000/user/password' \
  -H 'accept: */*' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
  "password": "123abc",
  "new_password": "123123"
}'

TOKEN=$(curl -s -X 'POST' 'http://localhost:8000/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123123' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:8000/user/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # {"username":"foo","last_name":"example","id":1,"is_active":true,"first_name":"foo","email":"foo@example.com","hashed_password":"$2b$12$udHlG896h8puSb.Gsz64BulGrW74iZAgP.ZaybO6/C1KTl73NeUG2","role":"admin"}%
```

</details>

---


## 12. (7.5) Dockerized FastAPI with ~~MySQL~~ PostgreSQL (~~Large Production Database Setup~~)

<!-- NO MySQL... -->

<!-- https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-with-a-single-file-fastapi -->

<details>

> [!IMPORTANT]
> Podríamos implantar [pgAdmin](https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html) tanto en tanto en el server (ver [docker-compose.yaml](/03-todos-database/docker-compose.yaml)) como en nuestra Workstation con otro setup...

- **Objetivos**: implantar una BD relacional (PostgreSQL y MySQL) e implementar CRUD Operations
- **Objetivos CUSTOM**: Dockerizarlo todo
- **Diferencias DBMS vs SQLite**: diapositivas 133-... en [../docs/FastAPI_slides.pdf](/docs/FastAPI_slides.pdf)...


### I. Dockerizar FastAPI

>  Tareas: `requirements.txt`, `app/`, `Dockerfile`, `.env.example`, `docker-compose.yaml`, `db/fastapi_todos.sql`, `SQLALCHEMY_DATABASE_URL`... 

1. Generamos nuestro [requirements.txt](/03-todos-database/requirements.txt) desde el `.venv` tras instalar una última dependencia ([psycopg2-binary](https://pypi.org/project/psycopg2-binary/))


```bash
# source .venv/bin/activate

pip install psycopg2-binary

pip freeze > 03-todos-database/requirements.txt
```

2. Nos aseguramos de que el nuevo directorio raíz de nuestra app FastAPI está en un subdirectorio `app/` (luego habrá que modificar el [app/database.py](/03-todos-database/app/database.py))

```bash
cd 03-todos-database

mkdir app
git mv routers *.py app/
```

3. Preparamos el [Dockerfile](/03-todos-database/Dockerfile) para la `app/`; entiendo que en prod. deberíamos:
   - montar los archivos en la imagen,
   - cambiar el comando `dev` por `run` y
   - verificar que funciona bien detrás de HAProxy (tema cabeceras y tal)

```Dockerfile
FROM python:3.12-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Descomentar y montar la app aquí en la imagen, no en el contenedor( docker-compose.yaml)
# COPY ./app .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 80

CMD ["fastapi", "dev", "/app/main.py", "--host", "0.0.0.0", "--port", "80"]
# CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "80"]
```

4. Preparamos el [docker-compose.yaml](/03-todos-database/docker-compose.yaml) con los servicios:
   - **fastapi**: el puerto para Swagger (`/docs`) pasa de ser el `8000` al `5012`
   - **postgresql**: usaremos [db/fastapi_todos.sql](/03-todos-database/db/fastapi_todos.sql) para crear las tablas y '*popularlas*'
   - **pgadmin**: no está implementado pero sí preparado y comentado en el `docker-compose.yaml`, por si luego viniera bien usarlo

```yaml
services:

  fastapi:
    build:
      context: .
    container_name: fastapi
    ports:
      - "5012:80"
    env_file:
      - ./.env.development
    # Para prod., comentar el volumen y montar la app/ en la imagen (Dockerfile)
    volumes:
      - ./app:/app
    restart: unless-stopped
    depends_on:
      postgresql:
        condition: service_healthy

  postgresql:
    image: postgres:16.1-alpine
    container_name: postgresql
    # Uncomment the port if we won't connect from outside (fastapi uses 5432 anyways)
    ports:
      - "5010:5432"
    env_file:
      - ./.env.development
    volumes:
      - postgresql_data:/var/lib/postgresql/data
      - ./db/fastapi_todos.sql:/docker-entrypoint-initdb.d/fastapi_todos.sql:ro
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U fastapi"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgresql_data:
```


5. Preparamos el [.env.example](/03-todos-database/.env.example) con las variables necesarias, que luego copiaremos como `.env.development` para darle valor a las variables, archivo que no deberíamos committear por seguridad/privacidad

```bash
# .env.example
POSTGRES_DB=''
POSTGRES_USER=''
POSTGRES_PASSWORD=''
```

6. Para la base de datos, preparamos el script [db/fastapi_todos.sql](/03-todos-database/db/fastapi_todos.sql) para crear las tablas necesarias y de paso *populate them*


```sql
DROP SCHEMA IF EXISTS public CASCADE;
CREATE SCHEMA public;

-- ===== CREATE TABLES =====

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL,
  email varchar(200) DEFAULT NULL,
  username varchar(45) DEFAULT NULL,
  first_name varchar(45) DEFAULT NULL,
  last_name varchar(45) DEFAULT NULL,
  hashed_password varchar(200) DEFAULT NULL,
  is_active boolean DEFAULT NULL,
  role varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS todos;
CREATE TABLE todos (
  id SERIAL,
  title varchar(200) DEFAULT NULL,
  description varchar(200) DEFAULT NULL,
  priority integer DEFAULT NULL,
  complete boolean DEFAULT NULL,
  owner_id integer DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (owner_id) REFERENCES users(id)
);

-- ===== POPULATE TABLES =====

/* Credenciales: foo==123abc; bar==123xyz */
INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active, role) VALUES
-- ( 'foo@example.com', 'foo', 'foo', 'example', crypt('123abc', gen_salt('bf')), TRUE, 'admin'),
  ( 'foo@example.com', 'foo', 'foo', 'example', '$2b$12$hevQQk73MbsOt5AG7Ofe7OZ6FWsp9Xwz8gh048fkK06ZuwS1lJ1DW', TRUE, 'admin'),
  ( 'bar@example.com', 'bar', 'bar', 'example', '$2b$12$TFlZ99l/WK/hIhJHJPajk.GuloOgrntRwQ2SDmnu2shD4bPy7qXVq', TRUE, '')
;

INSERT INTO todos (title, description, priority, complete, owner_id) VALUES
  ('Go to store','supdawg',4,false,1),
  ('Haircut','supdawg',3,true,2),
  ('Feed dog','supdawg',5,false,1),
  ('Water plant','supdawg',4,false,2),
  ('Learn something new','supdawg',5,true,1)
;
```


7. Para poder guardar las contraseñas hasheadas, preparamos el script [**/scripts/encrypt_password.py](/scripts/encrypt_password.py) (~~usa los mismos mecanismos de encriptación que la `app/`, importante~~)

```py
# scripts/encrypt_password.py
# ---

# source .venv/bin/activate && \
# pip install passlib
# (we should drop it tho, in app/ it requires us to use an outdated version of bcrypt as a dep.)

import argparse
from passlib.context import CryptContext

# Set up the bcrypt context
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_password(password: str) -> str:
    return bcrypt_context.hash(password)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hash a password for SQL INSERT.")
    parser.add_argument("password", help="Password to hash")
    
    args = parser.parse_args()
    hashed_password = hash_password(args.password)
    print(f"{args.password}: {hashed_password}")
```

```bash
# source .venv/bin/activate

python3 scripts/encrypt_password.py -h 123abc
  # usage: encrypt_password.py [-h] password
  # 
  # Hash a password for SQL INSERT.
  # 
  # positional arguments:
  #   password    Password to hash
  # 
  # options:
  #   -h, --help  show this help message and exit

python3 scripts/encrypt_password.py 123abc && \
python3 scripts/encrypt_password.py 123xyz
  # 123abc: $2b$12$hevQQk73MbsOt5AG7Ofe7OZ6FWsp9Xwz8gh048fkK06ZuwS1lJ1DW
  # 123xyz: $2b$12$TFlZ99l/WK/hIhJHJPajk.GuloOgrntRwQ2SDmnu2shD4bPy7qXVq
```

8.  Finalmente, definimos la conexión FastAPI > PostgreSQL en el [app/database.py](/03-todos-database/app/database.py)

> - [ ] **DEUDA TÉCNICA**: sacar los valores de un `.env` con python `dotenv` para conexión o así o ke

```py
# SQLALCHEMY_DATABASE_URL='sqlite:///./todosapp.db'
SQLALCHEMY_DATABASE_URL='postgresql://fastapi:s_clpa59Bs?D]BP<AgI@postgresql:5432/fastapi'

# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)
```


### II. Implantar stack y verificar FastAPI requests

DEMO

```bash
cp .env.example .env.development

sed -i -e "/POSTGRES_DB/s/''/'fastapi'/" \
       -e "/POSTGRES_USER/s/''/'fastapi'/" \
       -e "/POSTGRES_PASSWORD/s/''/'s_clpa59Bs?D]BP<AgI'/" \
  .env.development

cat .env.development
  # POSTGRES_DB='fastapi'
  # POSTGRES_USER='fastapi'
  # POSTGRES_PASSWORD='s_clpa59Bs?D]BP<AgI'
```

```bash
docker compose up -d
{
  docker compose logs -f
}

docker exec -it postgresql psql -U fastapi -d fastapi -c "select * from users;"
  #  id |      email      | username | first_name | last_name |                       hashed_password                        | is_active | role
  # ----+-----------------+----------+------------+-----------+--------------------------------------------------------------+-----------+-------
  #   1 | foo@example.com | foo      | foo        | example   | $2b$12$hevQQk73MbsOt5AG7Ofe7OZ6FWsp9Xwz8gh048fkK06ZuwS1lJ1DW | t         | admin
  #   2 | bar@example.com | bar      | bar        | example   | $2b$12$TFlZ99l/WK/hIhJHJPajk.GuloOgrntRwQ2SDmnu2shD4bPy7qXVq | t         |
  # (2 rows)

TOKEN=$(curl -s -X 'POST' 'http://localhost:5012/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'GET' \
  'http://localhost:5012/user/' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN"
  # {"first_name":"foo","id":1,"last_name":"example","is_active":true,"username":"foo","email":"foo@example.com","hashed_password":"$2b$12$hevQQk73MbsOt5AG7Ofe7OZ6FWsp9Xwz8gh048fkK06ZuwS1lJ1DW","role":"admin"}%
```

- Crear todo

```bash
TOKEN=$(curl -s -X 'POST' 'http://localhost:5012/auth/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=foo&password=123abc' \
  | jq -r .access_token
) && \
curl -X 'POST' \
  'http://localhost:5012/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
  "title": "sup",
  "description": "dawg",
  "priority": 3,
  "complete": true
}'
  # null%

curl -X 'GET' \
  'http://localhost:5012/todo/6' \
  -H 'accept: application/json' \
  -H "Authorization: Bearer $TOKEN" \
  # {"title":"sup","priority":3,"owner_id":1,"complete":true,"description":"dawg","id":6}%
```


---


### III. pgAdmin (opcional)

Con los 3 servicios funcionando (fastapi, postgresql y pgAdmin), visitamos la Web UI de pgAdmin para vincular la DB y operar

```yaml
pgAdmin:
  Login:
    email: poc@setenova.es
    password: USd3Fiv2,tJ,b[H\2r{
  Add New Server:
    General:
      Name: FastAPI
    Connection:
      Hostname: postgresql
      Port: 5432
      Username: fastapi
      Password: s_clpa59Bs?D]BP<AgI
      Save password: true
```

- pgAdmin: conectar con la BD (ya lo hemos hecho)
- pgAdmin: Servers > FastAPI > Login/Group Roles > **fastapi** > Properties > Privileges > All (**superuser**)
  - necesitaríamos otros usuarios para los desarrolladores/usuarios?
- pgAdmin: crear DB... no me gusta el click-click-click...


### IV. MySQL (UNDONE)

...




</details>

---



## 13. Project 3.5 - [Alembic](https://alembic.sqlalchemy.org/en/latest/) Data Migration
## 14. Project 4 - Unit & Integration Testing
## 15. Project 5 - Full Stack Application
## 16. Git - Version Control
## 17. Deploying FastAPI Applications