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
// 155. Min Stack
// https://leetcode-cn.com/problems/min-stack/description/

#include <stdio.h>

MinStack* minStackCreate(int maxSize);
void minStackPush(MinStack* obj, int x);
void minStackPop(MinStack* obj);
int minStackTop(MinStack* obj);
int minStackGetMin(MinStack* obj);
void minStackFree(MinStack* obj);

typedef struct {
    int * base;
    int * top;
    int * min_top;
    int * min_base;
    int size;
} MinStack;

int main()
{
    struct MinStack* obj = minStackCreate(maxSize);
    minStackPush(obj, x);
    minStackPop(obj);
    int param_3 = minStackTop(obj);
    minStackFree(obj);
    return 0;

}
/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack * stack = (MinStack *)malloc(sizeof(MinStack));
    if (!stack) return NULL;
    stack->base = (int * )malloc(sizeof(int) * maxSize);
    if (!stack->base)
    {
        free(stack);
        return NULL;
    }
    stack->top = stack->base;
    stack->min_base = (int *)malloc(sizeof(int) * maxSize);
    if (!stack->min_base) {
        free(stack->min_base);
        free(stack);
        return NULL;
    }
    stack->min_top = stack->min_base;
    stack->size = maxSize;

    return stack;
}

void minStackPush(MinStack* obj, int x) {
    
}

void minStackPop(MinStack* obj) {
    
}

int minStackTop(MinStack* obj) {
    
}

int minStackGetMin(MinStack* obj) {
    
}

void minStackFree(MinStack* obj) {
    
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