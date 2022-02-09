const swap = require('./swap');

function selectionSort(arr) {
    for (var i = 0; i < arr.length-1; ++i) {
        var indexOfElementHasMinValue = i;
        for (var j = i+1; j < arr.length; ++j) {
            if (arr[indexOfElementHasMinValue] > arr[j]) {
                indexOfElementHasMinValue = j;
            }
        }
        swap(arr, i, indexOfElementHasMinValue);
    }
    return arr;
}

function reverseSelectionSort(arr) {
    for (var i = 0; i < arr.length-1; ++i) {
        var indexOfElementHasMaxValue = i;
        for (var j = i+1; j < arr.length; ++j) {
            if (arr[indexOfElementHasMaxValue] < arr[j]) {
                indexOfElementHasMaxValue = j;
            }
        }
        swap(arr, i, indexOfElementHasMaxValue);
    }
    return arr;
}

module.exports = {
    selectionSort,
    reverseSelectionSort
}