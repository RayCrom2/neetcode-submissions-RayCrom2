class Solution {
public:
    bool isValid(string s) {
        std::stack<char> a;
        char cur;
        for (int i = 0; i < s.length(); ++i){
            cur = s[i];
            switch(cur){
                case '(':
                case '{':
                case '[':
                    a.push(cur);
                    break;
                case ')': {
                    if (a.size() > 0 && a.top() == '('){
                        a.pop();
                    }
                    else{
                        return false;
                    }
                    break;
                }
                case '}': {
                    if (a.size() > 0 && a.top() == '{'){
                        a.pop();
                    }
                    else{
                        return false;
                    }
                    break;
                }
                case ']': {
                    if (a.size() > 0 && a.top() == '['){
                            a.pop();
                    }                    
                    else{
                        return false;
                    }
                    
                    break;
                }

            }
        }
        return a.size() == 0;
    }
};
