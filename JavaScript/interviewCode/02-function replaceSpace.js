/*
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
*/
// 2019-11-28
function replaceSpace(str)
{
    var retStr = "";
    for (let i = 0; i < str.length; ++i) {
        if (str.charAt(i) !== " ") {
            retStr += str.charAt(i);
        } else {
            retStr += "%20";
        }
    }
    
    return retStr;
}