# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 16:42:00 2022

@author: bpcos
"""

class Person(object):
  def __init__(self, name: str, age: int, gender: str = 'ND') -> None:
    assert gender in ['M', 'F', 'ND', 'B'], "Gender Type Not Valid"
    self.name: str   = name
    self.age: int    = age
    self.gender: str = gender

  def __str__(self) -> str:
      return f"Person: Name:{self.name} Age:{self.age} Gender:{self.gender}"

class BankAccount(object):
  def __init__(self, holder: Person) -> None:
    self.holder = holder
    self.account = 0.0

  def deposit(self) -> None:
    self.account += float(input("Digitare quantità: "))
    self.show_balance()

  def withdraw(self):
    amount = float(input("Preleva: "))

    if self.account < amount:
      raise ValueError("The given amount is over your balance amount")

    self.account -= amount
    self.show_balance()
  
  def show_balance(self) -> None:
    print(self.account)
  
  def get_holder_name(self) -> str:
    return self.holder.name
  
  def get_holder_age(self) -> str:
    return self.holder.age

  def get_holder_gender(self) -> str:
    return self.holder.gender

class Bank(object):
  def __init__(self) -> None:
    self.accounts = set()

  def add_account(self, account: BankAccount) -> None:
    self.accounts.add(account)

# Persone
bruno = Person("Bruno", 16, 'M')
michele = Person("Michele", 20, 'B')
giorgia = Person("Giorgia", 17, 'F')

# Banche
banca = Bank()


# Conti
b1 = BankAccount(bruno)
m1 = BankAccount(michele)
g1 = BankAccount(giorgia)


banca.add_account(b1)
banca.add_account(m1)
banca.add_account(g1)

print(b1.get_holder_name())