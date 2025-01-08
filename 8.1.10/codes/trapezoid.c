#include <stdio.h>
// Function to compute y = x + 2 - x^2
double func(double x){
    return 0.25*(x + 2 - x*x);
}
// Trapezoidal Rule Function
double Area(double a, double b, int n){
    double h = (b - a) / n; // Step size
    double sum = 0.0;

    // Compute the values at the interval boundaries
    for(int i = 0; i <= n; i++){
        double x = a + i*h;
        double y = func(x);
        
        if(i == 0 || i == n){
            sum += (h/2.0) * y; // First and last terms
        } else {
            sum += h * y; // Intermediate terms
        }
    }
    return sum;
}

int main() {
    double a = -1;  // lower limit
    double b = 2.0; // Upper limit
    int n = 1000;    // Subdivisions

    double result = Area(a, b, n);
    printf("Approximated Area: %f\n", result);

    return 0;
}

