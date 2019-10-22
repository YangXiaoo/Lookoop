/**
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
*/

// 2018-7-22
// 130. Surrounded Regions
// https://blog.csdn.net/zdavb/article/details/47450743
// https://blog.csdn.net/mine_song/article/details/70208554
class 130_medium_Surrounded_Regions {
	class Node {
		int row;
		int col;
 
		Node(int x, int y) {
			row = x;
			col = y;
		}
	}
 
	public void solve(char[][] board) {
		if (board == null || board.length == 0)
			return;
		int m = board.length;
		int n = board[0].length;
		boolean[][] visited = new boolean[m][n];
		Queue<Character> q = new LinkedList<>();

		// 第一行和最后一行
		for (int i = 0; i < n; i++) {
			if (!visited[0][i] && board[0][i] == 'O')
				bfs(board, 0, i, m, n, visited);
			if (!visited[m - 1][i] && board[m - 1][i] == 'O')
				bfs(board, m - 1, i, m, n, visited);
 
		}
		// 第一列和最后一列
		for (int i = 0; i < m; i++) {
			if (!visited[i][0] && board[i][0] == 'O')
				bfs(board, i, 0, m, n, visited);
			if (!visited[i][n - 1] && board[i][n - 1] == 'O')
				bfs(board, i, n - 1, m, n, visited);
 
		}
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++) {
				if (!visited[i][j] && board[i][j] == 'O')
					board[i][j] = 'X';
			}
		for (int i = 0; i < m; i++)
			System.out.println(Arrays.toString(board[i]));
	}
 
	Queue<Node> q = new LinkedList<>();
 
	// 加入队列的时候设置visited该结点为true
	private void bfs(char[][] board, int row, int col, 
			int m, int n, boolean[][] visited) {
		q.offer(new Node(row, col));
		visited[row][col] = true;
		while (!q.isEmpty()) {
			Node tmp = q.poll();
			row = tmp.row;
			col = tmp.col;
			if (row - 1 >= 0 && !visited[row - 1][col] 
					&& board[row - 1][col] == 'O') {
				q.offer(new Node(row - 1, col));
				visited[row - 1][col] = true;
			}
			if (row + 1 < m && !visited[row + 1][col] 
					&& board[row + 1][col] == 'O') {
				q.offer(new Node(row + 1, col));
				visited[row + 1][col] = true;
			}
			if (col - 1 >= 0 && !visited[row][col - 1] 
					&& board[row][col - 1] == 'O') {
				q.offer(new Node(row, col - 1));
				visited[row][col - 1] = true;
			}
			if (col + 1 < n && !visited[row][col + 1] 
					&& board[row][col + 1] == 'O') {
				q.offer(new Node(row, col + 1));
				visited[row][col + 1] = true;
			}
 
		}
	}

}

class solution2 {
	public void solve(char[][] board) {
		if (board == null || board.length == 0) return;
		int row = board.length;
		int col = board[0].length;

		if (row < 3 || col < 3) return;

		for (int j = 0; j < row; j++) {
			dfs(board, j, 0);
			dfs(board, j, col - 1);
		}

		for (int i = 0; i < col; i++) {
			dfs(board, 0, i);
			dfs(board, row - 1, i);
		}
		for (int i = 0; i < row; i ++) {
			for (int j = 0; j < col; j++) {
				if (board[i][j] == 'O') {
					board[i][j] = 'X';
				}

				if (board[i][j] == 'v') {
					board[i][j] = 'O';
				}
			}
		}

	}

	public void dfs(char[][] board, int m, int n) {
		// 若先比较是否为'O' 会出现边界溢出现象
		if (m < 0 || m > board.length - 1 || n < 0 || n > board[0].length - 1 || board[m][n] != 'O') return;
		board[m][n] = 'v';
		dfs(board, m - 1, n);
		dfs(board, m + 1, n);
		dfs(board, m, n - 1);
		dfs(board, m, n + 1);
	}
}