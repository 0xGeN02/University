#include <iostream>
#include <vector>
#include "story.h"

int main() {
    std::vector<std::string> problems = {"Problem 1", "Problem 2", "Problem 3"};
    Story story(problems);
    while (!story.isGameFinished()) {
        story.displayStory();
        Level& currentLevel = story.getCurrentLevelObj();
        std::cout << "Problem: " << currentLevel.getProblem() << std::endl;
        std::string solution;
        std::cin >> solution;
        if (currentLevel.checkSolution(solution)) {
            std::cout << "Correct solution!" << std::endl;
            story.setLevel(story.getCurrentLevel() + 1);
        } else {
            std::cout << "Wrong solution, try again!" << std::endl;
        }
    }
    // Player finished the game, now display the final story and ask for the solution
    story.displayStory();
    std::string solution;
    std::cin >> solution;
    // Check if the solution is correct and finish the game
    // ...
    return 0;
}