// bard.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <unordered_set>

int main()
{
    int n = 0;
    std::cin >> n;

    std::unordered_set<std::string> unique_words;

    std::string current_word;
    std::cin >> current_word;

    unique_words.insert(current_word);

    int i = 1;
    for (; i < n; i++) {
        std::string next_word;
        std::cin >> next_word;

        if (next_word.front() != current_word.back()) {
            std::cout << "Player " << ((i % 2 == 0) ? "1" : "2") << " lost" << std::endl;
            return 0;
        }

        if (!unique_words.insert(next_word).second) {
            std::cout << "Player " << ((i % 2 == 0) ? "1" : "2") << " lost" << std::endl;
            return 0;
        }

        current_word = std::move(next_word);
    }

    std::cout << "Fair Game" << std::endl;
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
