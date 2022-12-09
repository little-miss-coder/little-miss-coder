#ifndef ARRAYLISTTYPE_H
#define ARRAYLISTTYPE_H

#include <iostream>
#include <cassert>

using namespace std;

template <class elemType>
class arrayListType
{
public:
    const arrayListType<elemType>& operator=(const arrayListType<elemType>&);
		//Overloads the assignment operator

    bool isEmpty();
		//Function to determine whether the list is empty

    bool isFull();
		//Function to determine whether the list is full

    int listSize();
		//Function to determine the number of elements in the list
    int maxListSize();
		//Function to determine the size of the list

    void print() const;
		//Function to output the elements of the list

    bool isItemAtEqual(int location, const elemType& item);
		//Function to determine whether the item is the same
 		//as the item in the list at the position specified

   void insertAt(int location, const elemType& insertItem);
		//Function to insert an item in the list at the
		//position specified by location. The item to be inserted
		//is passed as a parameter to the function.

   void insertEnd(const elemType&
                   insertItem);
		//Function to insert an item at the end of the list

    void removeAt(int location);
		//Function to remove the item from the list at the
		//position specified by location

    void retrieveAt(int location, elemType& retItem);
		//Function to retrieve the element from the list at the
		//position specified by location

    void replaceAt(int location, const elemType& repItem);
		//Function to replace the elements in the list at the
		//position specified by location.
    void clearList();
		//Function to remove all the elements from the list

    int seqSearch(const elemType& item);
  		//Function to search the list for a given item.
		//Postcondition: If the item is found, returns the location
		//               in the array where the item is found;
   		//               otherwise, returns -1.
    void insert(const elemType& insertItem);
		//Function to insert the item specified by the parameter
		//insertItem at the end of the list. However, first the
		//list is searched to see whether the item to be inserted
		//is already in the list.

    void remove(const elemType& removeItem);
		//Function to remove an item from the list. The parameter
		//removeItem specifies the item to be removed.


    arrayListType(int size = 100);
		//constructor
		//Creates an array of the size specified by the
		//parameter size. The default array size is 100.


    arrayListType(const arrayListType<elemType>& otherList);
		//copy constructor

    ~arrayListType();
		//destructor
		//Deallocates the memory occupied by the array.

protected:
    elemType *list; 	//array to hold the list elements
    int length;		//to store the length of the list
    int maxSize;		//to store the maximum size of the list
};



template <class elemType>
bool arrayListType<elemType>::isEmpty()
{
	return (length == 0);
}

template <class elemType>
bool arrayListType<elemType>::isFull()
{
	return (length == maxSize);
}

template <class elemType>
int arrayListType<elemType>::listSize()
{
	return length;
}

template <class elemType>
int arrayListType<elemType>::maxListSize()
{
	return maxSize;
}

template <class elemType>
void arrayListType<elemType>::print() const
{
	for(int i = 0; i < length; i++)
		cout<<list[i]<<" ";
	cout<<endl;
}

template <class elemType>
bool arrayListType<elemType>::isItemAtEqual
                   (int location, const elemType& item)
{
	return(list[location] == item);
}

template <class elemType>
void arrayListType<elemType>::insertAt
                   (int location, const elemType& insertItem)
{
	if(location < 0 || location >= maxSize)
		cerr<<"The position of the item to be inserted "
			<<"is out of range."<<endl;
	else
		if(length >= maxSize)  //list is full
			cerr<<"Cannot insert in a full list."<<endl;
		else
		{
			for(int i = length; i > location; i--)
				list[i] = list[i - 1];	//move the elements down

			list[location] = insertItem;	//insert the item at the
 										//specified position

			length++;	//increment the length
		}
} //end insertAt

template <class elemType>
void arrayListType<elemType>::insertEnd(const elemType& insertItem)
{
	if(length >= maxSize)  //the list is full
		cerr<<"Cannot insert in a full list."<<endl;
	else
	{
		list[length] = insertItem;	//insert the item at the end
		length++;	//increment length
	}
} //end insertEnd

template <class elemType>
void arrayListType<elemType>::removeAt(int location)
{
	if(location < 0 || location >= length)
    	cerr<<"The location of the item to be removed "
			<<"is out of range."<<endl;
	else
	{
   		for(int i = location; i < length - 1; i++)
	 		list[i] = list[i+1];

		length--;
	}
} //end removeAt

template <class elemType>
void arrayListType<elemType>::retrieveAt
                     (int location, elemType& retItem)
{
	if(location < 0 || location >= length)
    	cerr<<"The location of the item to be retrieved is "
			<<"out of range."<<endl;
	else
		retItem = list[location];
} // retrieveAt

template <class elemType>
void arrayListType<elemType>::replaceAt
                    (int location, const elemType& repItem)
{
	if(location < 0 || location >= length)
    	cerr<<"The location of the item to be replaced is "
			<<"out of range."<<endl;
	else
		list[location] = repItem;

} //end replaceAt

template <class elemType>
void arrayListType<elemType>::clearList()
{
	length = 0;
} // end clearList

template <class elemType>
int arrayListType<elemType>::seqSearch(const elemType& item)
{
	int loc;
	bool found = false;

	for(loc = 0; loc < length; loc++)
	   if(list[loc] == item)
	   {
		found = true;
		break;
	   }

	if(found)
		return loc;
	else
		return -1;
} //end seqSearch

template <class elemType>
void arrayListType<elemType>::insert(const elemType& insertItem)
{
	int loc;

	if(length == 0)					 //list is empty
		list[length++] = insertItem; //insert the item and
 									 //increment the length
	else
		if(length == maxSize)
			cout<<"Cannot insert in a full list."<<endl;
		else
		{
			loc = seqSearch(insertItem);

			if(loc == -1)   //the item to be inserted
							//does not exist in the list
				list[length++] = insertItem;
			else
				cerr<<"the item to be inserted is already in "
 					<<"the list. No duplicates are allowed."<<endl;
	}
} //end insert

template <class elemType>
void arrayListType<elemType>::remove(const elemType& removeItem)
{
	int loc;

	if(length == 0)
		cerr<<"Cannot delete from an empty list."<<endl;
	else
	{
		loc = seqSearch(removeItem);

		if(loc != -1)
			removeAt(loc);
		else
			cout<<"The item to be deleted is not in the list."
				<<endl;
	}

} //end remove


template <class elemType>
arrayListType<elemType>::arrayListType(int size)
{
	if(size < 0)
	{
		cerr<<"The array size must be positive. Creating "
 			<<"an array of size 100. "<<endl;

 	   maxSize = 100;
 	}
 	else
 	   maxSize = size;

	length = 0;

	list = new elemType[maxSize];
	assert(list != NULL);
}

template <class elemType>
arrayListType<elemType>::~arrayListType()
{
	delete [] list;
}

	//copy constructor
template <class elemType>
arrayListType<elemType>::arrayListType
                   (const arrayListType<elemType>& otherList)
{
   maxSize = otherList.maxSize;
   length = otherList.length;
   list = new elemType[maxSize]; 	//create the array
   assert(list != NULL);	//terminate if unable to allocate
 							//memory space

   for(int j = 0; j < length; j++)  //copy otherList
 	   list [j] = otherList.list[j];
}//end copy constructor


template <class elemType>
const arrayListType<elemType>& arrayListType<elemType>::operator=
			(const arrayListType<elemType>& otherList)
{
	if(this != &otherList)	//avoid self-assignment
	{
	   delete [] list;
	   maxSize = otherList.maxSize;
       length = otherList.length;

       list = new elemType[maxSize];
	   assert(list != NULL);

       for(int i = 0; i < length; i++)
	   	    list[i] = otherList.list[i];
	}

    return *this;
}


#endif
