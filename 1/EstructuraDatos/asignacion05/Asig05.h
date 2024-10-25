
#ifndef ASIG05_H
#define ASIG05_H

#include <vector>
#include <list>
#include <ctime>
#include <chrono>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

// Node structure
struct Node {
    int data;
    Node* left;
    Node* right;
};

// Binary Search Tree class
class BinarySearchTree {
public:
    BinarySearchTree();
    ~BinarySearchTree();
    void insert(int data);
    Node* search(int data);

private:
    Node* root;
    Node* insert(Node* node, int data);
    Node* search(Node* node, int data);
    void deleteTree(Node* node);
};

// Linear search for vector and list
bool linear_search(const vector<int>& vec, int data);
bool linear_search(const list<int>& lst, int data);

#endif // ASIG05_H