//fruit.cpp
#include "fruit.h"
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

void fruitType::setAll(string n, double p, double q)
{
    name = n;
    price = p;
    quantity = q;
}

fruitType::fruitType(string n, double p, double q)
{
    setAll(n, p, q);
}

void fruitType::setName(string n)
{
    name = n;
}

void fruitType::setPrice(double p)
{
    price = p;
}

void fruitType::setQuantity(double q)
{
    quantity = q;
}

ostream & operator<<(ostream & os, fruitType & ob)
{
    os << setw(20)<< ob.name << "$" << ob.price <<setw(20) << "/lb"
         << ob.quantity << setw(20)  << " lb"  << "$"  << ob.getCost() << endl;
    return os;

}
