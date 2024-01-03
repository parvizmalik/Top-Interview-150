var addBinary = function(a, b) {
    let carry = 0, result='';
    let ac = a.length-1, ab=b.length-1;
    while (ac>=0||ab>=0||carry){
        if (ac>=0){
            carry += parseInt(a[ac]);
            ac--;
        }
        if (ab>=0){
            carry += parseInt(b[ab]);
            ab--;
        }
        result = (carry % 2 ).toString() + result;
        carry = Math.floor(carry/2);
    }
    return result ;

};