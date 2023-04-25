#ifndef HUFFMANTREE_H
#define HUFFMANTREE_H

#include <queue>
#include <unordered_map>

class HuffmanTree {
    private:
        struct TreeNode {
            char val;
            int freq;
            TreeNode* left;
            TreeNode* right;
            TreeNode(char v, int f);
            TreeNode(int f);
            ~TreeNode();
        };

        struct NodeComparator {
            bool operator()(const TreeNode* lhs, const TreeNode* rhs) const;
        };

        void traverse_tree(const TreeNode* node, std::string code, std::unordered_map<char, std::string>& codes) const;
        std::unordered_map<char, int> get_frequencies(const std::string& text) const;

        TreeNode* root;

    public:
        HuffmanTree(const std::string& text);
        ~HuffmanTree();

        std::unordered_map<char, std::string> get_codes() const;
};

#endif