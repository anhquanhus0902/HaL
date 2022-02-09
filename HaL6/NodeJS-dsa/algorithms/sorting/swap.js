module.exports = function(arr, u, v) {
    var tmp = arr[u];
    arr[u] = arr[v];
    arr[v] = tmp;
}