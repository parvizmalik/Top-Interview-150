* @param {string[]} tokens
* @return {number}
*/
// var evalRPN = function(tokens) {
//     let stack = [];
//     for (let token of tokens){
//         if (!['+','-','*','/'].includes(token)){
//             stack.push(parseInt(token));
//         }
//         else{
//             let right = stack.pop() , left = stack.pop()
//             if (token==='+'){
//                 stack.push(right+left);
//             }
//             else if (token==='-'){
//                 stack.push(left-right);
//             }
//             else if (token==='*'){
//                 stack.push(left*right);
//             }
//             else if (token==='/'){
//                 stack.push(parseInt(left/right));
//             }
//         }
//     }
//     return stack.pop();
// };
var evalRPN = function(tokens) {
    let stack = [];
    for (let token of tokens){
        switch(token) {
            case '+':
                stack.push(stack.pop() + stack.pop());
                break;
            case '-':
                stack.push(-stack.pop() + stack.pop());
                break;
            case '*':
                stack.push(stack.pop() * stack.pop());
                break;
            case '/':
                let right = stack.pop(), left = stack.pop();
                stack.push((left / right) | 0); // bitwise OR for truncating towards zero
                break;
            default:
                stack.push(Number(token)); // Direct conversion to Number
        }
    }
    return stack.pop();
};
