var simplifyPath = function(path) {
    let stack = [];
    let segments = path.split('/');

    for (let segment of segments) {
        if (segment === "..") {
            if (stack.length > 0) {
                stack.pop();
            }
        } else if (segment !== "" && segment !== ".") {
            stack.push(segment);
        }
    }

    return "/" + stack.join('/');
};
