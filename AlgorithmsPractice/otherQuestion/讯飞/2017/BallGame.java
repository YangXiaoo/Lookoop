
import java.util.*;
/*
大学生足协决定举办全国性的大学生足球赛，由每个学校派遣一支队伍代表该校参赛。比赛分区分为几个赛区进行，最终的总决赛中，将有不超过n支队伍参加。经过激烈的角逐，有机会参与总决赛的队伍已经决出。
协会对比赛的规则进行了调整，以便使得比赛更具有观赏性。

1. 总决赛的参赛队伍为n支，n为偶数；
2. 进入前1/2的队伍才有资格进入淘汰赛；
3. 队伍按积分排名，具体规则为：胜一场积3分；平一场积1分；负一场积0分。队伍首先按积分降序排列，积分相同按净胜球数降序排列，仍然相同的按进球数降序排列。
4. 基于上述规则，尚未出现有排名歧义的情况发生。

随着赛程的进行，目前各个队伍对战的结果已经确定了，小B负责确定进入淘汰赛的名单，她向你求助，你能帮她吗？

输入
测试数据有多组，每组测试数据的第一行为一个整数n（1=< n <=50），为参与总决赛的球队数，随后的n行为球队的名字，由不超过30个的大小写拉丁字母构成。随后的n*(n-1)/2行为赛事的开展情况，每行的格式为name1-name2 num1:num2，表示两支队伍的比分情况（1=<num1, num2<=100）。确保不会有两支队伍同名，也不会出现队伍自己通自己比赛的情况，且每场比赛仅出现一次。

输出

对每组测试数据，输出n/2行，为按字母序排列的进入淘汰赛的n/2支队伍的名单，每个名字在单独的行中输出。

 
样例输入

4

A

B

C

D

A-B 1:1

A-C 2:2

A-D 1:0

B-C 1:0

B-D 0:3

C-D 0:3

2

a

A

a-A 2:1

样例输出

A

D

a
*/
class Team {
	public String tName;
	private int grade;
	private int winScore;
	private int inScore;

	public void setGrade(int grade) {
		this.grade = grade;
	}

	public int getGrade() {
		return this.grade;
	}

	public void setWinScore(int winScore) {
		this.winScore = winScore;
	}

	public int getWinScore() {
		return this.winScore;
	}

	public void setInScore(int inScore) {
		this.inScore = inScore;
	}

	public int getInScore() {
		return this.inScore;
	}

	public Team(String tName, int grade, int winScore, int inScore) {
		this.tName = tName;
		this.grade = grade;
		this.winScore = winScore;
		this.inScore = inScore;
	}

}
public class BallGame {

	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			String nS = cin.nextLine();
			int n = Integer.valueOf(nS);
			TreeMap<String, Team> map = new TreeMap<>();
			for (int i = 0; i < n; ++i) {
				String tName = cin.nextLine();
				Team curTeam = new Team(tName, 0, 0, 0);
				map.put(tName, curTeam);
			}

			int gameCount = n * (n - 2) >> 2;
			Team[] record = new Team[n];
			for(int i = 0; i < gameCount; ++i) {
				String[] curRecord = cin.nextLine().split(" ");
				String[] teamRecord = curRecord[0].split("-");
				String[] scoreRecord = curRecord[1].split(":");

				// 设置一个队与第二个队的分数
				int team1InScore = Integer.valueOf(scoreRecord[0]);
				int team2InScore = Integer.valueOf(scoreRecord[1]);

				int team1WinScore = 0, team2WinScore = 0;
				int team1Grade = 0, team2Grade = 0;
				int gap = team1InScore - team2InScore;
				if (gap > 0) {
					team1Grade = 3;
					team1WinScore = gap;
				} else if (gap == 0) {
					team1Grade = 1;
					team2Grade = 1;
				} else {
					team2Grade = 3;
					team2WinScore = gap;
				}

				Team team1 = map.get(teamRecord[0]);
				team1.setGrade(team1.getGrade() + team1Grade);
				team1.setWinScore(team1.getWinScore() + team1WinScore);
				team1.setInScore(team1.getInScore() + team1InScore);
				map.put(teamRecord[0], team1);

				Team team2 = map.get(teamRecord[1]);
				team2.setGrade(team2.getGrade() + team2Grade);
				team2.setWinScore(team2.getWinScore() + team2WinScore);
				team2.setInScore(team2.getInScore() + team2InScore);
				map.put(teamRecord[1], team2);	
			}

			int i = 0;
			for (String tName : map.keySet()) {
				record[i++] = map.get(tName);
			}

			Arrays.sort(record, new Comparator<Team>() {
				public int compare(Team o1, Team o2) {
					int grade = o1.getGrade() - o2.getGrade();
					int winScore = o1.getWinScore() - o2.getWinScore();
					int inScore  = o1.getInScore() - o2.getInScore();

					if (grade != 0) {
						return grade;
					} else if (winScore != 0) {
						return winScore;
					} else {
						return inScore;
					}
				}
			});

			String[] out = new String[n>>2];
			for (int j = 0; j < (n >> 2); ++j) {
				out[j] = record[j].tName;
			}

			Arrays.sort(out);
			for (String name : out) {
				System.out.println(name);
			}
		}
	}
}