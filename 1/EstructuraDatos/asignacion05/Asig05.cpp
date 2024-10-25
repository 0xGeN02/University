#include "Asig05.h"


// Constructor
BinarySearchTree::BinarySearchTree() : root(nullptr) {}

// Destructor
BinarySearchTree::~BinarySearchTree() { deleteTree(root); }

// Insertar un nodo
Node* BinarySearchTree::insert(Node* node, int data) {
    if (node == nullptr) {
        node = new Node;
        node->data = data;
        node->left = node->right = nullptr;
    }
    else if (data < node->data) {
        node->left = insert(node->left, data);
    }
    else {
        node->right = insert(node->right, data);
    }
    return node;
}

void BinarySearchTree::insert(int data) {
    root = insert(root, data);
}

// Buscar un nodo
Node* BinarySearchTree::search(Node* node, int data) {
    if (node == nullptr || node->data == data)
        return node;
    if (data < node->data)
        return search(node->left, data);
    else
        return search(node->right, data);
}

Node* BinarySearchTree::search(int data) {
    return search(root, data);
}

// Eliminar el árbol
void BinarySearchTree::deleteTree(Node* node) {
    if (node == nullptr) return;
    deleteTree(node->left);
    deleteTree(node->right);
    delete node;
}

// Linear search for vector and list
bool linear_search(const vector<int>& vec, int data) {
    return find(vec.begin(), vec.end(), data) != vec.end();
}

bool linear_search(const list<int>& lst, int data) {
    return find(lst.begin(), lst.end(), data) != lst.end();
}

