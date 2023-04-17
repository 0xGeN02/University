#include <iostream>
#include <vector>

int main(){
    //Initialiting vector
    std::vector<int> nums;
    for (int i = 0; i < 20; i++) {
        nums.push_back(i);
    }

    //Use range-based for loop
    for(auto num : nums){
        std::cout <<num<<" ";
    }
    std::cout << std::endl;
    //Initializer
    auto my_pair = std::pair{42, "lorem ipusm vitae"}

    auto[my_int, my_string] = my_pair;

    std::cout << my_int << " " << my_string << std::endl;
    return 0;
}