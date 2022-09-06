/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    int depth = 0;
    void traverse(Node* root,int d){
        if(root==nullptr){
            return;
        }
        depth = max(d,depth);
        for(int i=0;i<root->children.size();i++){
            traverse(root->children[i],d+1);
        }
    }
    int maxDepth(Node* root) {
        traverse(root,1);
        return depth;
    }
};
