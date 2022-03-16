# -*- coding: utf-8 -*-
"""
@author: Bruno Pio Cosentini
"""

from math import sqrt
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

  def module(self):
    return sqrt(self.x**2 + self.y**2, self.z**2)

  def normalize(self):
    norm = self.module()
    self.x /= norm
    self.y /= norm
    self.z /= norm

  def v_sum(self, vector2) -> type[Self]:
    x = self.x + vector2.x
    y = self.y + vector2.y
    z = self.z + vector2.z

    return Vector_3D(x,y,z)