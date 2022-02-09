const swap = require('./swap');

function bubbleSort(arr) {
    for (var i = 0; i < arr.length-1; ++i) {
        for (var j = i+1; j < arr.length; ++j) {
            if (arr[i] > arr[j]) {
                swap(arr, i, j);
            }
        }
    }
    return arr;
}

function reverseBubbleSort(arr) {
    for (var i = 0; i < arr.length-1; ++i) {
        for (var j = i+1; j < arr.length; ++j) {
            if (arr[i] < arr[j]) {
                swap(arr, i, j);
            }
        }
    }
    return arr;
}

module.exports = {
    bubbleSort,
    reverseBubbleSort
};