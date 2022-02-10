/**
 * 
 * @param {Array} arr 
 * @param {Number} key 
 * @returns {Number}
 */
module.exports = function(arr, key) {
    for (var i = 0; i < arr.length; ++i) {
        if (arr[i] == key) {
            return i;
        }
    }
    return -1;
}