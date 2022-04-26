#ifndef MyLibrary_h
#define MyLibrary_h

#include "Arduino.h"

class MyLibrary {
  public:
    MyLibrary();
    void repeater(String msg);
    int doubler(int x);
};

#endif
