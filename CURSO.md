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
  - [8. Setup Database (7.1) ](#8-setup-database-71-)
      - [1. Intro](#1-intro-1)
      - [2. DB Connection with ORM SQLAlchemy](#2-db-connection-with-orm-sqlalchemy)
      - [3. DB Tables (Models)](#3-db-tables-models)
      - [4. main: DB Conn. for API \& init](#4-main-db-conn-for-api--init)
      - [5. SQLite3 Installation](#5-sqlite3-installation)
      - [6. SQL Queries Crash-Course](#6-sql-queries-crash-course)
      - [7. SQLite3 Setup: TODOs](#7-sqlite3-setup-todos)
  - [9. API Request Methods](#9-api-request-methods)
  - [10. Authentication \& Authorization (JWT)](#10-authentication--authorization-jwt)
  - [11. Authenticate Requests](#11-authenticate-requests)
  - [12. Large Production Database Setup](#12-large-production-database-setup)
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

python3 -m pip --version  # && pip install pip-autoremove -y
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

## 8. Setup Database (7.1) <!--(*Dockerized* PostgreSQL)-->

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

## 9. API Request Methods
## 10. Authentication & Authorization (JWT)
## 11. Authenticate Requests
## 12. Large Production Database Setup
## 13. Project 3.5 - Alembic Data Migration
## 14. Project 4 - Unit & Integration Testing
## 15. Project 5 - Full Stack Application
## 16. Git - Version Control
## 17. Deploying FastAPI Applications