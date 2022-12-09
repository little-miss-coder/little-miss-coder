//fruitArrayType.cpp

#ifndef FRUITARRAYTYPE_H
#define FRUITARRAYTYPE_H

#include <iostream>
//#include <iomanip>
//#include <string>

using namespace std;

class fruitArrayType: public arrayListType<fruitType>
{
public:
    void print() const; //whole receipt
    void printByItem(int) const; //specific number ex:3rd item in list
    void printByName(string) const; //print all of given fruit "Apple"
    void updateQ(int, double);
    void updateP(string, double);
    double getTotal();

};

#endif
