/*
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
*/
// 2019-11-29
function minNumberInSequence(arr, left, right) {
    var minNumber = arr[left];
    for (var i = left; i <= right; ++i) {
        if (arr[i] < minNumber) {
            minNumber = arr[i];
        }
    }

    return minNumber;
}
function minNumberInRotateArray(rotateArray)
{
    var left = 0, right = rotateArray.length - 1;
    if (right < 0) return 0;
    while (left <= right) {
        var mid = (right + left) >> 1;
        if (right - left === 1) {   // 因为旋转了，右边的数为最小数
            return rotateArray[right];
        }
        if (rotateArray[left] === rotateArray[right] && rotateArray[left] === rotateArray[mid]) {
            return minNumberInSequence(rotateArray, left, right);
        }
        // 两种情况
        if (rotateArray[mid] > rotateArray[left]) {
            left = mid;
        } else if (rotateArray[mid] <= rotateArray[right]) {
            right = mid;
        }
    }
}

function test() {
    var arr = [3, 4, 5, 1, 2];
    var ret = minNumberInRotateArray(arr);
    console.log(ret);
}

test();