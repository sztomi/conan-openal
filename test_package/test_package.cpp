// #include <cpprest/json.h>
#include <stdio.h>
#include "AL/alc.h"

int main() {
  ALCdevice *device = alcOpenDevice(NULL);
  if (device) {
    printf("Opened device, now closing...\n");
    alcCloseDevice(device);
    printf("Closed device.\n");
  }
  else {
    printf("Device was not opened.\n");
  }
  printf("Test OK\n");
  return 0;
}
