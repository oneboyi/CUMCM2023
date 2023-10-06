
#include "rand.h"
#include "Q3_data.h"
#include <string.h>

/* Function Definitions */
/*
 * Arguments    : void
 * Return Type  : double
 */
double b_rand(void)
{
  static unsigned int c_state[625];
  double r;
  int hi;
  int kk;
  if (method == 4U) {
    unsigned int b_r;
    unsigned int y;
    hi = (int)(state / 127773U);
    b_r = 16807U * (state - hi * 127773U);
    y = 2836U * hi;
    if (b_r < y) {
      state = ~(y - b_r) & 2147483647U;
    } else {
      state = b_r - y;
    }
    r = (double)state * 4.6566128752457969E-10;
  } else if (method == 5U) {
    unsigned int b_r;
    unsigned int y;
    b_r = 69069U * b_state[0] + 1234567U;
    y = b_state[1] ^ b_state[1] << 13;
    y ^= y >> 17;
    y ^= y << 5;
    b_state[0] = b_r;
    b_state[1] = y;
    r = (double)(b_r + y) * 2.328306436538696E-10;
  } else {
    unsigned int b_r;
    if (!state_not_empty) {
      memset(&c_state[0], 0, 625U * sizeof(unsigned int));
      b_r = 5489U;
      c_state[0] = 5489U;
      for (hi = 0; hi < 623; hi++) {
        b_r = ((b_r ^ b_r >> 30U) * 1812433253U + hi) + 1U;
        c_state[hi + 1] = b_r;
      }
      c_state[624] = 624U;
      state_not_empty = true;
    }
    /* ========================= COPYRIGHT NOTICE ============================
     */
    /*  This is a uniform (0,1) pseudorandom number generator based on: */
    /*                                                                         */
    /*  A C-program for MT19937, with initialization improved 2002/1/26. */
    /*  Coded by Takuji Nishimura and Makoto Matsumoto. */
    /*                                                                         */
    /*  Copyright (C) 1997 - 2002, Makoto Matsumoto and Takuji Nishimura, */
    /*  All rights reserved. */
    /*                                                                         */
    /*  Redistribution and use in source and binary forms, with or without */
    /*  modification, are permitted provided that the following conditions */
    /*  are met: */
    /*                                                                         */
    /*    1. Redistributions of source code must retain the above copyright */
    /*       notice, this list of conditions and the following disclaimer. */
    /*                                                                         */
    /*    2. Redistributions in binary form must reproduce the above copyright
     */
    /*       notice, this list of conditions and the following disclaimer */
    /*       in the documentation and/or other materials provided with the */
    /*       distribution. */
    /*                                                                         */
    /*    3. The names of its contributors may not be used to endorse or */
    /*       promote products derived from this software without specific */
    /*       prior written permission. */
    /*                                                                         */
    /*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS */
    /*  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT */
    /*  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR */
    /*  A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT */
    /*  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, */
    /*  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT */
    /*  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, */
    /*  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY */
    /*  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT */
    /*  (INCLUDING  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
     */
    /*  OF THIS  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. */
    /*                                                                         */
    /* =============================   END   =================================
     */
    unsigned int u[2];
    do {
      for (hi = 0; hi < 2; hi++) {
        unsigned int y;
        b_r = c_state[624] + 1U;
        if (c_state[624] + 1U >= 625U) {
          for (kk = 0; kk < 227; kk++) {
            y = (c_state[kk] & 2147483648U) | (c_state[kk + 1] & 2147483647U);
            if ((y & 1U) == 0U) {
              y >>= 1U;
            } else {
              y = y >> 1U ^ 2567483615U;
            }
            c_state[kk] = c_state[kk + 397] ^ y;
          }
          for (kk = 0; kk < 396; kk++) {
            y = (c_state[kk + 227] & 2147483648U) |
                (c_state[kk + 228] & 2147483647U);
            if ((y & 1U) == 0U) {
              y >>= 1U;
            } else {
              y = y >> 1U ^ 2567483615U;
            }
            c_state[kk + 227] = c_state[kk] ^ y;
          }
          y = (c_state[623] & 2147483648U) | (c_state[0] & 2147483647U);
          if ((y & 1U) == 0U) {
            y >>= 1U;
          } else {
            y = y >> 1U ^ 2567483615U;
          }
          c_state[623] = c_state[396] ^ y;
          b_r = 1U;
        }
        y = c_state[(int)b_r - 1];
        c_state[624] = b_r;
        y ^= y >> 11U;
        y ^= y << 7U & 2636928640U;
        y ^= y << 15U & 4022730752U;
        u[hi] = y ^ y >> 18U;
      }
      u[0] >>= 5U;
      u[1] >>= 6U;
      r = 1.1102230246251565E-16 * ((double)u[0] * 6.7108864E+7 + (double)u[1]);
    } while (r == 0.0);
  }
  return r;
}

/*
 * File trailer for rand.c
 *
 * [EOF]
 */
