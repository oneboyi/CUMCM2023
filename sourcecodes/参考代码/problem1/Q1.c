
#include "Q1.h"


void Q1(double eta_list[9])
{
  double DsCNS[9];
  int i;
  for (i = 0; i < 9; i++) {
    double d;
    eta_list[i] = 0.0;
    d = 70.0 - 0.026185921569186928 * (200.0 * (double)i + -800.0);
    DsCNS[i] = d;
    if (i + 1 != 1) {
      double eta_list_tmp;
      eta_list_tmp = DsCNS[i - 1];
      eta_list[i] = (-0.30470617011518009 * (eta_list_tmp / -0.960065624146096 +
                                             d / -0.94410760040152886) -
                     (eta_list_tmp - d) / 0.026185921569186928) /
                    (d * -0.30481062110221668 * -2.0831909295563458 *
                     0.99965732497555726);
    }
  }
}

