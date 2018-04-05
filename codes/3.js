<!DOCTYPE html>
<html>
<title>Web Page Design</title>
<script>
function removeElementsWithValue(arr, val) {
    var i = arr.length;
    while (i--) {
        if (arr[i] === val) {
            arr.splice(i, 1);
        }
    }
    return arr;
}

var data = [0, 1, 2, 'stop', 2, 0, 1, 'stop'];
removeElementsWithValue(data, 0);
document.write(data);
</script>
<body>
</body>
</html>
