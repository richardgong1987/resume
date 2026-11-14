/**
 *  Formula:
 *
 *    B(P):
 *      if |P|=m,  Save P
 *
 *      otherwise, for each x  ∈ S
 *
 *          if x ∉ P:
 *              add x
 *              B(P)
 *              remove x
 *
 */

var S = [1, 2, 3];
var m = 2;
var results = [];

backtracking([]);

function backtracking(P) {
    if (P.length === m) {
        return results.push(P.slice());
    }
    for (let x of S) {
        if (P.includes(x)) continue;

        P.push(x);
        backtracking(P);
        P.pop();
    }
}

console.log(results);

