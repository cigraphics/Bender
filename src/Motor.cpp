#include "Motor.h"

Motor::Motor(const unsigned int &pins[])
{
  mPins = pins;
}

void Motor::changeSpeed(const unsigned int &speed)
{
  mSpeed = speed;
}

void Motor::changeDirection(const eDirection &direction)
{
  mDirection = direction;
}

void Motor::run()
{
  for(int pinIndex = 0; pinIndex<4; pinIndex++ )
  {
    mPins[i],
  }
}

