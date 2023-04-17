#include "story.h"

Story::Story(std::vector<std::string> problems){
    for (auto& problem : problems){
        levels.emplace_back(problem);
    }
    currentLevel = 0;
}

void Story::displayStory(){
    //TODO: Display the story based on the player´s progress
}

void Story::setLevel (int level){
    currentLevel = level;
}

int Story::getCurrentLevel() {
    return currentLevel;
}

bool Story::isGameFinished() {
    return currentLevel == levels.size();
}

Level& Story::getCurrentLevelObj() {
    return levels[currentLevel];
}

