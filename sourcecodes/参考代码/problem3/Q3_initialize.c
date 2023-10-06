

/* Include Files */
#include "Q3_initialize.h"
#include "Q3_data.h"
#include "eml_rand.h"
#include "eml_rand_mcg16807_stateful.h"
#include "eml_rand_mt19937ar_stateful.h"
#include "eml_rand_shr3cong_stateful.h"

/* Function Definitions */
/*
 * Arguments    : void
 * Return Type  : void
 */
void Q3_initialize(void)
{
  state_not_empty_init();
  eml_rand_init();
  eml_rand_mcg16807_stateful_init();
  eml_rand_shr3cong_stateful_init();
  isInitialized_Q3 = true;
}

/*
 * File trailer for Q3_initialize.c
 *
 * [EOF]
 */
