/*
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
*/
// 2019-11-28
function Find(target, array)
{
    var r = 0;
    var c = array[0].length - 1;
    var isExist = false;
    while (r < array.length && c >= 0) {
        if (target === array[r][c]) {
            isExist = true;
            break;
        } else if (target < array[r][c]) {
            --c;
        } else if (target > array[r][c]) {
            ++r;
        }
    }
    return isExist;
}

var array = [[1,2,3], [4,5,6], [7,8,9]];
var target = 7;

console.log(Find(target, array))