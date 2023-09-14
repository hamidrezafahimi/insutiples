#include "header.h"

SomeClass::SomeClass(float multiplier_) : multiplier(multiplier_) {};

SomeClass::SomeClass(float multiplier_, float f_) : multiplier(multiplier_), f(f_) {};

float SomeClass::multiply(float input)
{
  return multiplier * input;
}

