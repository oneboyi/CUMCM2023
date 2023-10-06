#include "Q2.h"
#include <math.h>

void Q2(double saomiaodaikuan[64])
{
  static const double dv[8] = {0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1};
  int i;
  int j;
  for (i = 0; i < 8; i++) {
    double DSW;
    double beta;
    beta = 45.0 * (double)i / 180.0 * 3.1415926535897931;
    DSW = tan(beta);
    DSW =
        atan(0.026185921569186928 * DSW / sqrt(DSW * DSW + 1.001371875164758));
    for (j = 0; j < 8; j++) {
      double Deepth;
      Deepth = dv[j] * 1852.0 * 0.026185921569186928 * cos(beta) + 120.0;
      saomiaodaikuan[i + (j << 3)] =
          0.8660254037844386 / sin(0.52359877559829893 - DSW) * Deepth +
          0.8660254037844386 / sin(DSW + 0.52359877559829893) * Deepth;
    }
  }
}
