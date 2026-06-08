#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class RouletteGame {
private:
    string playerName;
    double totalAmount;

public:
    RouletteGame() : totalAmount(1000.0) {  ]
        cout << "Enter your name: ";
        cin >> playerName;
    }

    void playRound() {
        int guessedNumber, randomNumber;
        double betAmount;

        cout << "\nWelcome, " << playerName << "!\n";
        cout << "Your current balance: $" << totalAmount << endl;

        cout << "Enter your bet amount: $";
        cin >> betAmount;
        
        if(betAmount > totalAmount) {
            cout << "Insufficient funds! Try again with a lesser amount.\n";
            return;
        }

        cout << "Guess a number between 0 and 36: ";
        cin >> guessedNumber;

        srand(time(0));  
        randomNumber = rand() % 37;  

        
        cout << "The roulette wheel spun and the number is: " << randomNumber << endl;

        
        if (guessedNumber == randomNumber) {
            cout << "You won! You guessed the number correctly.\n";
            totalAmount += betAmount * 35;  
        } else {
            cout << "You lost. Better luck next time.\n";
            totalAmount -= betAmount;  
        }

        cout << "Your updated balance: $" << totalAmount << endl;

        if (totalAmount <= 0) {
            cout << "You have run out of money. Game over!" << endl;
            exit(0);  
        }
    }

    void startGame() {
        char playAgain;

        do {
            playRound();
            cout << "\nWould you like to play again? (y/n): ";
            cin >> playAgain;
        } while (playAgain == 'y' || playAgain == 'Y');
        
        cout << "Thanks for playing, " << playerName << "!\n";
    }
};

int main() {
    RouletteGame game;
    game.startGame();
    return 0;
}
