class TreeNode {
private:
    int key;
    int value;
    TreeNode* leftC; 
    TreeNode* rightC;
public:
    TreeNode(const int&k, const int&v) : key(k), value(v), leftC(nullptr), rightC(nullptr){}
    int getKey(){
        return key;
    }
    int getValue(){
        return value;
    }
    void setKey(const int& newKey){
        key = newKey;
    }
    void setValue(const int& newValue){
        value = newValue;
    }
    TreeNode* getLeftC(){
        return leftC;
    }
    TreeNode* getRightC(){
        return rightC;
    }
    void setLeftC(TreeNode* node){
        leftC = node;
    }
    void setRightC(TreeNode* node){
        rightC = node;
    }
};
class TreeMap {
private:
    TreeNode* root;

    TreeNode* inOrdPred(TreeNode* nodeToRemove){
        nodeToRemove = nodeToRemove->getLeftC();
        while(nodeToRemove->getRightC() != nullptr){
            nodeToRemove = nodeToRemove->getRightC();
        }
        return nodeToRemove;
    }
    
    TreeNode* removeHelper(TreeNode* node, int key){
        if (!node) return nullptr;

        if(key > node->getKey()){
            node->setRightC(removeHelper(node->getRightC(), key));
            return node;
        } else if (key < node->getKey()){
            node->setLeftC(removeHelper(node->getLeftC(), key));
            return node;
        }
        else{
            if (!node->getLeftC()){
                TreeNode* rChild = node->getRightC();
                delete node;
                return rChild;
            }
            else if (!node->getRightC()){
                TreeNode* lChild = node->getLeftC();
                delete node;
                return lChild;
            }
            else{
                TreeNode* preDec = inOrdPred(node);
                node->setKey(preDec->getKey());
                node->setValue(preDec->getValue());
                node->setLeftC(removeHelper(node->getLeftC(), preDec->getKey()));
                return node;
            }
        }
    }
    
public:
    TreeMap() {
        root = nullptr;
    }

    

    void insert(int key, int val) {
        if (root == nullptr){
            root = new TreeNode(key,val);
            return;
        }
            
        TreeNode* curr = root;
        while(true){
            if(curr->getKey() > key){
                if(curr->getLeftC() == nullptr){
                    curr->setLeftC(new TreeNode(key,val));
                    return;
                }
                curr = curr->getLeftC();
            }
            else if(curr->getKey() < key){
                if(curr->getRightC() == nullptr){
                    curr->setRightC(new TreeNode(key,val));
                    return;
                }
                curr = curr->getRightC();
            }
            else{
                curr->setValue(val);
                return;
            }
        }

    }
    

    int get(int key) {
        TreeNode* curr = root;
        while(curr != nullptr){
            if (curr->getKey() == key){
                return curr->getValue();
            }
            else if(curr->getKey() > key){
                curr = curr->getLeftC();
            }
            else{
                curr = curr->getRightC();
            }
        }
        return -1;
    }

    int getMin() {
        if (root == nullptr) return -1;
        TreeNode* curr = root;
        while (curr->getLeftC() != nullptr){
            curr = curr->getLeftC();
        }
        return curr->getValue();
    }

    int getMax() {
        if (root == nullptr) return -1;
        TreeNode* curr = root;
        while (curr->getRightC() != nullptr){
            curr = curr->getRightC();
        }
        return curr->getValue();
    }

    void remove(int key) {
        root = removeHelper(root, key);
    }

    std::vector<int> getInorderKeys() {
        std::vector<int> result;
        std::stack<TreeNode*> st;
        TreeNode* curr = root;

        while(curr || !st.empty()){
            while(curr){
                st.push(curr);
                curr = curr->getLeftC();
            }
            
            curr = st.top();
            st.pop();
            result.push_back(curr->getKey());

            curr = curr->getRightC();
        }
        return result;
    }
};