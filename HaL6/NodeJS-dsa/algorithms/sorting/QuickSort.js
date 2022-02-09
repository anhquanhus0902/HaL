const swap = require('./swap');

/**
 * 
 * @param {Array} arr
 * @param {Number} l
 * @param {Number} r
 */
function quickSort(arr, l, r) {
    if (l === undefined || r === undefined) {
        l = 0;
        r = arr.length-1;
    }
    if (l < r) {
        var pi = partition(arr, l, r);
        quickSort(arr, l, pi-1);
        quickSort(arr, pi+1, r);
    }
}

/**
 * 
 * @param {Array} arr 
 * @param {Number} l 
 * @param {Number} r
 * @returns {Number}
 */
function partition(arr, l, r) {
    var pivot = arr[r];
    var pivotIndex = l;
    for (var i = l; i < r; ++i) {
        if (arr[i] < pivot) {
            swap(arr, i, pivotIndex);
            ++pivotIndex;
        }
    }
    swap(arr, pivotIndex, r);
    return pivotIndex;
}

/**
 * 
 * @param {Array} arr 
 * @param {Number} l
 * @param {Number} r
 */
function reverseQuickSort(arr, l, r) {
    if (l === undefined || r === undefined) {
        l = 0;
        r = arr.length-1;
    }
    if (l < r) {
        var pi = partition4R(arr, l, r);
        reverseQuickSort(arr, l, pi-1);
        reverseQuickSort(arr, pi+1, r);
    }
}

/**
 * @param {Array} arr
 * @param {Number} l
 * @param {Number} r
 * @returns {Number}
 */
function partition4R(arr, l, r) {
    var pivot = arr[r];
    var pivotIndex = l;
    for (var i = l; i < r; ++i) {
        if (arr[i] > pivot) {
            swap(arr, i, pivotIndex);
            ++pivotIndex;
        }
    }
    swap(arr, pivotIndex, r);
    return pivotIndex;
}

module.exports = {
    quickSort,
    reverseQuickSort
}