#include <iostream>

int main() {
    int myArray[] = {1, 3, 4, 2, 5};
    int size = sizeof(myArray) / sizeof(myArray[0]);

    for (int i = 0; i < size; ++i) {
        std::cout << "Value: " << myArray[i] << ", Memory Address: " << &myArray[i] << std::endl;
    }

    return 0;
}
