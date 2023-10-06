
/* Include Files */
#include "Q3.h"
#include "Q3_data.h"
#include "Q3_initialize.h"
#include "rand.h"

void Q3(void)
{
  int i;
  if (!isInitialized_Q3) {
    Q3_initialize();
  }
  for (i = 0; i < 18; i++) {
    b_rand();
    b_rand();
  }
  for (i = 0; i < 18; i++) {
    b_rand();
    b_rand();
  }
}

/*
 * File trailer for Q3.c
 *
 * [EOF]
 */
