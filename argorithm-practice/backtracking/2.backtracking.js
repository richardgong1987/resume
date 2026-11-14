/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
    const Output = [];
    const letters = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    const group = [];
    for (const ch of digits) {
        group.push(letters[ch]);
    }

    B(0, '', group);


    function B(i, p, group) {
        if (group.length === 0) {
            return Output.push(p);
        }

        for (let j = 0; j < group[0].length; j++) {
            const c = group[0][j];
            B(i + 1, p + c, group.slice(1));
        }
    }

    return Output;

};

console.log(letterCombinations('234'))