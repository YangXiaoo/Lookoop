/**
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
*/

// 2018-7-29
//  
// https://leetcode-cn.com/problems/min-stack/description/

#include <stdio.h>

typedef struct {
    int head;
    int stack[2000];
} MinStack;
MinStack* minStackCreate(int maxSize);
void minStackPush(MinStack* obj, int x);
void minStackPop(MinStack* obj);
int minStackTop(MinStack* obj);
int minStackGetMin(MinStack* obj);
void minStackFree(MinStack* obj);

int main()
{
    // not declare
    struct MinStack* obj = minStackCreate(maxSize);
    minStackPush(obj, 2);
    minStackPush(obj, 3);
    minStackPop(obj);
    int t = minStackTop(obj);
    minStackFree(obj);
    printf("%d\n", t);
    return 0;

}
/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack * stack = (MinStack *)malloc(sizeof(MinStack));
    if (!stack) return NULL;
    stack->head = -1;

    return stack;
}

void minStackPush(MinStack* obj, int x) {
    (obj->head)++;
    obj->stack[obj->head] = x;

}

void minStackPop(MinStack* obj) {
    if (obj->head != -1) (obj->head)--;
}

int minStackTop(MinStack* obj) {
    return obj->stack[obj->head];
}

int minStackGetMin(MinStack* obj) {
    long min = 2147473648;
    if (obj_>head == -1)
        return;
    for (int i = 0; i <= obj->head; i++)
    {
        if (obj->stack[i] < min) min = obj->stack[i];
    }
    return min;
}

void minStackFree(MinStack* obj) {
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */