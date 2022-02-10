/**
 * 
 * @param {Array} arr 
 * @param {Number} n 
 * @returns {Boolean}
 */
function Sorted(arr, n) {
	if (n === 0 || n === 1) {
		return true;
	}
	if (arr[n-1] < arr[n-2]) {
		return false;
	}
	return Sorted(arr, n-1);
}

/**
 * 
 * @param {Array} arr 
 * @param {Number} key
 * @returns {Number} 
 */
module.exports = function(arr, key) {
    if (!Sorted(arr, arr.length)) {
        return -2;
    }
    var l = 0;
    var r = arr.length-1;
    while (l <= r) {
        var mid = Math.floor((l+r)/2);
        if (arr[mid] < key) {
            l = mid+1;
        }
        else if (arr[mid] > key) {
            r = mid-1;
        }
        else {
            return mid;
        }
    }
    return -1;
} 