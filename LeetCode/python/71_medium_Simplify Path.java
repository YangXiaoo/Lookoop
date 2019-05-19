class Solution {
    public String simplifyPath(String path) {
        String[] splitPath = path.split("/");
        // System.out.println(Arrays.toString(splitPath));
        Stack<String> stack = new Stack<>();
        for (String dir : splitPath) {
            switch (dir) {
                case ".":
                    break;
                case "":
                    break;
                case "..":
                    if (!stack.isEmpty()) {
                        stack.pop();
                    }
                    break;
                default:
                    stack.push(dir);
            }
        }
        if (stack.isEmpty()) return "/";
        
        String ret = "";
        for (String dir : stack) {
            ret += "/" + dir;
        }
        
        return ret;
    }
}