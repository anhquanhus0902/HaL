const swap = require('./swap');

/**
 * 
 * @param {Array} arr
 */
function bubbleSort(arr) {
    for (var i = 0; i < arr.length-1; ++i) {
        for (var j = i+1; j < arr.length; ++j) {
            if (arr[i] > arr[j]) {
                swap(arr, i, j);
            }
        }
    }
}

/**
 * 
 * @param {Array} arr
 */
function reverseBubbleSort(arr) {
    for (var i = 0; i < arr.length-1; ++i) {
        for (var j = i+1; j < arr.length; ++j) {
            if (arr[i] < arr[j]) {
                swap(arr, i, j);
            }
        }
    }
}

module.exports = {
    bubbleSort,
    reverseBubbleSort
};