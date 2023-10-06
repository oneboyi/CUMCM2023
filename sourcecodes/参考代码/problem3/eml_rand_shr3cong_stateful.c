

/* Include Files */
#include "eml_rand_shr3cong_stateful.h"
#include "Q3_data.h"

/* Function Definitions */
/*
 * Arguments    : void
 * Return Type  : void
 */
void eml_rand_shr3cong_stateful_init(void)
{
  b_state[0] = 362436069U;
  b_state[1] = 521288629U;
}

/*
 * File trailer for eml_rand_shr3cong_stateful.c
 *
 * [EOF]
 */
