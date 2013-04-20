#ifndef MOTOR_H
#define MOTOR_H

class Motor
{

  public:
    typedef enum {
      FORWARD = 0,
      BACKWARD
    } eDirection;

    Motor(const unsigned int &pins[]);

    void changeSpeed(const unsigned int &speed);
    void changeDirection(const eDirection &direction);
    void run();

  private:
    unsigned int mSpeed;
    eDirection mDirection;
    unsigned int mPins[];

};

#endif // MOTOR_H
