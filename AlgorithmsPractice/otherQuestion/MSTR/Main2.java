public class Main2 {
   static List<String> braces(List<String> values) {
    	Map<Character, Character> map = new HashMap<>();
    	map.put('}', '{');
    	map.put(']', '[');
    	map.put(')', '(');
    	List<String> ret = new ArrayList<>();
    	for (String str : values) {
    		Stack<Character> stack = new Stack<>();
    		for (int i = 0; i < str.length(); ++i) {
    			Character c = str.charAt(i);
    			if (!map.containsKey(c)) {
    				stack.push(c);
    			} else {
    				if (!stack.empty() && stack.peek() == c) {
    					stack.pop();
    				} else {
    					stack.push(c);
    				}
    			}
    		}

    		if (stack.empty()) {
    			ret.add("YES");
    		} else {
    			ret.add("NO");
    		}
    	}

    	return ret;
    }

    public static void main(String[] args) {
        // 待写
    }
}