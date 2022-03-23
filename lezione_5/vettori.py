# -*- coding: utf-8 -*-
"""
@author: Bruno Pio Cosentini
"""

from math import sqrt, acos
from typing_extensions import Self

class Immutable:
  __slots__ = []
  _immutable = False

  def __init__(self) -> None:
    for attr in dir(self):
      self.__slots__.append(attr)
    self._immutable = True
  
  def __delattr__(self, *args, **kwargs) -> None:
    if self._immutable:
      raise AttributeError('Immutable Object')
    object.__delattr__(self, *args, **kwargs)
  
  def __setattr__(self, *args, **kwargs) -> None:
    if self._immutable:
      raise AttributeError('Immutable Object')
    object.__setattr__(self, *args, **kwargs)

class Vector_3D:
  def __init__(self, x: float, y: float, z: float) -> None:
    self.x = x
    self.y = y
    self.z = z

  @property
  def module(self):
    return (self.x**2 + self.y**2, self.z**2) ** (1/2)

  def normalize(self):
    norm = self.module
    self.x /= norm
    self.y /= norm
    self.z /= norm

  def v_sum(self, vector2) -> type[Self]:
    x = self.x + vector2.x
    y = self.y + vector2.y
    z = self.z + vector2.z

    return Vector_3D(x,y,z)

  def scaling(self, scale_factor) -> None:
    self.x *= scale_factor
    self.y *= scale_factor
    self.z *= scale_factor

  def scalar_prod(self, v2: Vector_3D):
    return self.x * v2.x + self.y * v2.y + self.z * v2.z

  def vectorial_prod(self, v2: Vector_3D):
    x = self.y * v2.z - self.z * v2.y
    y = self.z * v2.x - self.x * v2.z
    z = self.x * v2.y - self.y * v2.x
    return Vector_3D(x,y,z)

  def angle(self, v2):
    ps = self.scalar_prod(v2)
    cos_a = ps / (self.module * v2.module)
    return acos(cos_a)

  def __add__(self, v2):
    x = self.x + v2.x
    y = self.y + v2.y
    z = self.z + v2.z
    return Vector_3D(x,y,z)

  def __mul__(self, v2):
    return self.x * v2.x + self.y * v2.y + self.z * v2.z