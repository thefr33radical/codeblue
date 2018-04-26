#include<iostream>
using namespace std;
int i=0;
void print_even();
void print_odd();
void print_even()
{
    cout<<i++<<endl;
    if(i<101&&i%2!=0)
        print_odd();
}

void print_odd()
{
    cout<<i++<<endl;
    if(i<101&&i%2==0)
        print_even();
}

int main()
{
print_even();
return 0;
}
