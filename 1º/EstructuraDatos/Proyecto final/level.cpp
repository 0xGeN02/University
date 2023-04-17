#include "level.h"

Level::Level(std::string prob): problem(prob), solved(false){}

bool Level::isSolved(){
    return solved;
}

void Level::setSolved(bool solved){
    this->solved = solved;
}

std::string Level::getProblem(){
    return problem;
}

bool Level::checkSolution(std::string solution){
    //If level is correct, marks level as solved
    solved = true;
    return true;
}
