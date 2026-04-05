class DynamicArray {
private:
int* arr;
size_t size;
size_t capacity;
public:

    DynamicArray(int capacity) :
    size(0), capacity(capacity)
    {
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity){
            resize();
        }
        arr[size++] = n;
    }

    int popback() {
        return arr[size-- - 1];
    }

    void resize() {
        capacity *= 2;
        int* newArray = new int[capacity];
        for (int i = 0; i < size; ++i){
            newArray[i] = arr[i];
        }
        delete arr;
        arr = newArray;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
