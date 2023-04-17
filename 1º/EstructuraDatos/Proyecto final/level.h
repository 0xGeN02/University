#ifndef level_h
#define level_h

#include <string>

class Level{

    private:
        std::string problem;
        bool solved;

    public:
        Level(std::string prob);
        bool isSolved();
        void setSolved(bool isSolved);

        std::string getProblem();
        bool checkSolution(std::string solution);
};

#endif level_h