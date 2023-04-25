#include "HuffmanTree.h"

HuffmanTree::TreeNode::TreeNode(char v, int f) : val(v), freq(f), left(nullptr), right(nullptr) {}
HuffmanTree::TreeNode::TreeNode(int f) : val('\0'), freq(f), left(nullptr), right(nullptr) {}
HuffmanTree::TreeNode::~TreeNode() {
    delete left;
    delete right;
}

bool HuffmanTree::NodeComparator::operator()(const TreeNode* lhs, const TreeNode* rhs) const {
    return lhs->freq > rhs->freq;
}

HuffmanTree::HuffmanTree(const std::string& text) : root(nullptr) {
    std::unordered_map<char, int> freqs = get_frequencies(text);
    std::priority_queue<TreeNode*, std::vector<TreeNode*>, NodeComparator> pq;
    for (const auto& pair : freqs) {
        pq.push(new TreeNode(pair.first, pair.second));
    }
    while (pq.size() > 1) {
        TreeNode* left = pq.top();
        pq.pop();
        TreeNode* right = pq.top();
        pq.pop();
        TreeNode* parent = new TreeNode(left->freq + right->freq);
        parent->left = left;
        parent->right = right;
        pq.push(parent);
    }
    if (pq.size() == 1) {
        root = pq.top();
        pq.pop();
    }
}

HuffmanTree::~HuffmanTree() {
    delete root;
}

std::unordered_map<char, std::string> HuffmanTree::get_codes() const {
    std::unordered_map<char, std::string> codes;
    if (root != nullptr) {
        traverse_tree(root, "", codes);
    }
    return codes;
}

std::unordered_map<char, int> HuffmanTree::get_frequencies(const std::string& text) const {
    std::unordered_map<char, int> freqs;
    for (char c : text) {
        freqs[c]++;
    }
    return freqs;
}

void HuffmanTree::traverse_tree(const TreeNode* node, std::string code, std::unordered_map<char, std::string>& codes) const {
    if (node->left == nullptr && node->right == nullptr) {
        codes[node->val] = code;
    }
    else {
        if (node->left != nullptr) {
            traverse_tree(node->left, code + "0", codes);
        }
        if (node->right != nullptr) {
            traverse_tree(node->right, code + "1", codes);
        }
    }
}

