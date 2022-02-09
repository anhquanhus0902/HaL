/**
 * 
 * @param {Array} arr
 */
function insertionSort(arr) {
    for (var i = 1; i < arr.length; ++i) {
        var j = i;
        var val = arr[j];
        while (j >= 0 && val < arr[j-1]) {
            arr[j] = arr[j-1];
            --j;
        }
        arr[j] = val;
    }
}

/**
 * 
 * @param {Array} arr
 */
function reverseInsertionSort(arr) {
    for (var i = 1; i < arr.length; ++i) {
        var j = i;
        var val = arr[j];
        while (j >= 0 && val > arr[j-1]) {
            arr[j] = arr[j-1];
            --j;
        }
        arr[j] = val;
    }
}

module.exports = {
    insertionSort,
    reverseInsertionSort
}