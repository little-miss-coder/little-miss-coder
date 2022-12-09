//fruit.h

#ifndef FRUIT_H
#define FRUIT_H

#include <iostream>
#include <iomanip>
#include <string>
using namespace std;


class fruitType
{
private:
    string name;
    double price;
    double quantity;
public:
    void setAll(string n, double p, double q);
    void setName(string n);
    void setPrice(double p);
    void setQuantity(double q);
    double getCost() {return price * quantity;}
    string getName() {return name;}
    double getPrice() {return price;}
    double getQuantity() {return quantity;}
    fruitType (string name = " ", double price = 0, double quantity = 0);

    friend ostream& operator<<(ostream& os, fruitType& ob);
};



#endif // FRUIT_H
