#include <cmath>
#include <iostream>
#include <limits>

#include <array.H>
#include <gauss.H>

///
/// given the state Y, return the RHS of our ODE system
///
std::vector<double> rhs(const std::vector<double>& Y) {

    std::vector<double> dYdt(3, 0.0);

    dYdt[0] = -0.04 * Y[0] + 1.e4 * Y[1] * Y[2];
    dYdt[1] =  0.04 * Y[0] - 1.e4 * Y[1] * Y[2] - 3.e7 * Y[1] * Y[1];
    dYdt[2] =                                     3.e7 * Y[1] * Y[1];

    return dYdt;
}

///
/// given the state Y, return the Jacobian of the ODE system
///
Array jacobian(const std::vector<double>& Y) {

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


std::vector<double>
backward_euler(const double t_start, const double t_end, const double dt_init,
               const std::vector<double> y_init) {

    const double tol{1.e-6};
    const int max_iter{100};

    int neq = static_cast<int>(y_init.size());

    double time{t_start};
    double dt{dt_init};

    // starting point of the integration for each step
    std::vector<double> y_n{y_init};
    std::vector<double> y_new{0.0};

    while (time < t_end) {

        for (int n = 0; n < static_cast<int>(y_new.size()); ++n) {
            y_new[n] = y_n[n];
        }

        bool converged{false};

        int niter{0};
        while (!converged && niter < max_iter) {

            // construct the matrix A = I - dt J
            Array A = jacobian(y_n);

            for (int irow = 0; irow < neq; ++irow) {
                for (int jcol = 0; jcol < neq; ++jcol) {
                    A(irow, jcol) *= -dt;
                    if (irow == jcol) {
                        A(irow, jcol) += 1.0;
                    }
                }
            }

            // construct the HS
            std::vector<double> b = rhs(y_new);
            for (int irow = 0; irow < neq; ++irow) {
                b[irow] = y_n[irow] - y_new[irow] + dt * b[irow];
            }

            // solve the linear system A dy = b
            std::vector<double> dy = gauss_elim(A, b);

            // correct our guess
            for (int irow = 0; irow < neq; ++irow) {
                y_new[irow] += dy[irow];
            }

            // check for convergence by computing the norms
            double dy_norm{0.0};
            double y_new_norm(0.0);
            for (int irow = 0; irow < neq; ++irow) {
                dy_norm += dy[irow] * dy[irow];
                y_new_norm += y_new[irow] * y_new[irow];
            }
            double error = std::sqrt(dy_norm / y_new_norm);
            if (error < tol) {
                converged = true;
            }

            niter++;
        }

        if (!converged) {
            std::cout << "convergence failure" << std::endl;
            std::exit(EXIT_FAILURE);
        }

        if (time + dt > t_end) {
                dt = t_end - time;
        }

        // reset the solution for the next step
        for (int irow = 0; irow < neq; ++irow) {
            y_n[irow] = y_new[irow];
        }

        time += dt;
    }

    return y_n;
}

int main() {

    // setup the initial conditions
    std::vector<double> y_init{1.0, 0.0, 0.0};

    // we are going to do a bunch of short integrations to different
    // end points -- this holds the end times for each interval
    std::vector<double> t_ends{-6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0,
                               1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0};

    double time{0.0};
    std::vector<double> y_old{y_init};

    for (auto log_t_max: t_ends) {

        double tmax = std::pow(10.0, log_t_max);

        auto y_new = backward_euler(time, tmax, tmax/10.0, y_old);
        time = tmax;

        std::cout << tmax << " " << y_new[0] << " " << y_new[1] << " " << y_new[2] << std::endl;

        for (int irow = 0; irow < 3; ++irow) {
            y_old[irow] = y_new[irow];
        }
    }

}
