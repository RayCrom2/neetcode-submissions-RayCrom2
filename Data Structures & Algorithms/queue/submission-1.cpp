class Node {
private:
    int value;
    Node* next;
    Node* prev;
public:
    Node(const int& val) : value(val), next(nullptr), prev(nullptr){}
    int getValue (){
        return value;
    }
    bool setNext(Node* node){
        if (this == nullptr)
            return false;
        next = node;
        return true;
    }
    bool setPrev(Node* node){
        if (this == nullptr)
            return false;
        prev = node;
        return true;
    }
    Node* getNext(){
        return next;
    }
    Node* getPrev(){
        return prev;
    }
    
    
};

class Deque {
private:
    Node* head;
    Node* tail;
public:
    Deque() : head(nullptr), tail(nullptr) {}

    bool isEmpty() {
        return head == nullptr;
    }

    void append(int value) {
        Node* newNode = new Node(value);
        if (head == nullptr){
            head = newNode;
            tail = newNode;
        }
        else if(head == tail){
            tail = newNode;
            tail->setPrev(head);
            head->setNext(tail);
        }
        else{
            tail->setNext(newNode);
            newNode->setPrev(tail);
            tail = newNode;
        }
    }

    void appendleft(int value) {
        Node* newNode = new Node(value);
        if (head == nullptr){
            head = newNode;
            tail = newNode;
        }
        else if(head == tail){
            head = newNode;
            tail->setPrev(head);
            head->setNext(tail);
        }
        else{
            head->setPrev(newNode);
            newNode->setNext(head);
            head = newNode;
        }
    }

    int pop() {
        if (tail == nullptr){
            return -1;
        }
        Node* toPop = tail;
        int retValue = toPop->getValue();
        if(head == tail){
            head = nullptr;
            tail = nullptr;
        }
        else{
            tail = tail->getPrev();
            tail->setNext(nullptr);
        }
        
        
        delete toPop;
        return retValue;
    }

    int popleft() {
        if (head == nullptr){
            return -1;
        }
        Node* toPopLeft = head;
        int retValue = toPopLeft->getValue();
        if(head == tail){
            head = nullptr;
            tail = nullptr;
        }
        else{
            head = head->getNext();
            head->setPrev(nullptr);
        }
        
        
        delete toPopLeft;
        return retValue;
    }
};

