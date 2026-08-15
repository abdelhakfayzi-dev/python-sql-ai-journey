#include <stdlib.h>
int main(){


float balance = 500000;
float rate = 0.05/12;
float payment = 2684.11;
float total = 0;

for (int i = 0; i < 360; i++) {
    float interest = balance * rate;
    float principal = payment - interest;
    balance = balance - principal;
    total = total + payment;
}
printf("%.2f\n", total);
return 0;
}