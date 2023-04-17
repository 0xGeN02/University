#ifndef story_h
#define story_h

#include <vector>
#include <string>
#include "level.h"


class Story{
    private:
        std::vector<Level>levels;
        int currentLevel;

    public:
        Story(std::vector<std::string> problems);
        void displayStory();
        void setLevel(int level);
        int getCurrentLevel();
        bool isGameFinished();
        Level& getCurrentLevelObj();
};

#endif
