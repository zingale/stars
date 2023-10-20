#include <iostream>

#include <array.H>
#include <gauss.H>

///
/// given the state Y, return the RHS of our ODE system
///
std::vector<Real> rhs(const std::vector<Real>& Y) {

    std::vector<Real> dYdt(3, 0.0);

    dYdt[0] = -0.04 * Y[0] + 1.e4 * Y[1] * Y[2];
    dYdt[1] =  0.04 * Y[0] - 1.e4 * Y[1] * Y[2] - 3.e7 * Y[1] * Y[1];
    dYdt[2] =                                     3.e7 * Y[1] * Y[1];

    return dYdt;
}

///
/// given the state Y, return the Jacobian of the ODE system
///
Array jacobian(const std::vector<Real>& Y) {

    Array jac(3, 3);

    jac(0, 0) = -0.04;
    jac(0, 1) = 1.e4 * Y[2];
    jac(0, 2) = 1.e4 * Y[1];

    jac(1, 0) = 0.04;
    jac(1, 1) = -1.e4 * Y[2] - 6.e7 * Y[1];
    jac(1, 2) = -1.e4 * Y[1];

    jac(2, 0) = 0.0;
    jac(2, 1) = 6.e7 * Y[1];
    jac(2, 2) = 0.0;

    return jac;
}

int main() {



}