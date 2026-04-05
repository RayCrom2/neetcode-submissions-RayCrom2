class Node{
public:
    int value;
    Node* next;

    Node() : 
    value(0), next(nullptr){}

    Node(int val) : 
    value(val), next(nullptr){}


    void setNext(Node* node){
        next = node;
    }

    int getValue(){
        return value;
    }
};

class LinkedList {
private:
    Node* head;
    Node* tail;
public:
    LinkedList() :
    head(nullptr), tail(nullptr)
    {}

    int get(int index) {
        if (index < 0){
            return -1;
        }
        Node* requestedNode = head;
        for (int i = 0; i < index && requestedNode != nullptr; ++i) {
            requestedNode = requestedNode->next;
        }
        if (!requestedNode){
            return -1;
        }
        return requestedNode->getValue();
    }

    void insertHead(int val) {
        Node* newHead = new Node(val);
        newHead->setNext(head);
        head = newHead;
        if (tail == nullptr){
            tail = head;
        }
    }
    
    void insertTail(int val) {
        if (!head){
            insertHead(val);
            return;
        }
        Node* newTail = new Node(val);
        tail->setNext(newTail);
        tail = newTail;
    }

    bool remove(int index) {
        if (head == nullptr){
            return false;
        }
        if (index == 0){
            Node* toDelete = head;
            if (head == tail){
                head = head->next;
                tail = head;
                delete toDelete;
            }
            else{
                head = head->next;
                delete toDelete;
            }
            return true;
        }
        int i = 1;
        Node* curr = head;
        while (i < index && curr != nullptr) {
            i++;
            curr = curr->next;
        }

        // Remove the node ahead of curr
        if (curr != nullptr && curr->next != nullptr) {
            if (curr->next == tail) {
                Node* toDelete = tail;
                tail = curr;
                curr->setNext(nullptr);
                delete toDelete;
            }
            else{
                Node* toDelete = curr->next;
                curr->setNext(toDelete->next);
                delete toDelete;
            }
            return true;
        }
        return false;
    }

    vector<int> getValues() {
        vector<int> values;
        Node* current = head;
        while (current != nullptr){
            values.push_back(current->getValue());
            current = current->next;
        }
        return values;
    }
};

