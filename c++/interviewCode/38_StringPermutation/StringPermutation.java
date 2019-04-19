// 2019-4-19
//字符串的排序
// 输入字符串abc,输出字符串abc, acb, bca, cab, cba, bac

import java.util.*;

public class StringPermutation {
	public List<String> permutation(String seq) {
		// 先第一个与后面的交换，然后第二个与后面的交换
		List<String> ret = new ArrayList<>();
		ret.add(seq);
		int seqSize = seq.length();
		// System.out.println("string size: " + seqSize);

		for (int i = 0; i < seqSize; ++i) {
			List<String> tmp = new ArrayList<>();
			for (int j = 0; j < ret.size(); ++j) {
				String tmpSeq = ret.get(j);
				for (int idx = i + 1; idx < seqSize; ++idx) {
					// 交换顺序
					char[] charSeq = tmpSeq.toCharArray();
					char tmpChar = charSeq[i];
					charSeq[i] = charSeq[idx];
					charSeq[idx] = tmpChar;
					tmp.add(new String(charSeq));
					// System.out.println(new String(charSeq));
				}
			}
			ret.addAll(tmp);
		}

		return ret;
	}

	public void test(String testName, String seq) {
		List<String> ret = permutation(seq);
		System.out.println(testName + ", result: " + ret.toString() + ", size: " + ret.size());
	}

	public static void main(String[] args) {
		StringPermutation test = new StringPermutation();
		test.test("test1", "abc");
		test.test("test2", "abcde");
	}
}

// test1, result: [abc, bac, cba, acb, bca, cab], size: 6
// test2, result: [abcde, bacde, cbade, dbcae, ebcda, acbde, adcbe, aecdb, bcade, bdcae, becda, cabde, cdabe, ceadb, dcbae, dacbe, decab, ecbda, edcba, eacdb, abdce, abedc, badce, baedc, cbdae, cbeda, dbace, dbeac, ebdca, ebadc, acdbe, acedb, adbce, adebc, aedcb, aebdc, bcdae, bceda, bdace, bdeac, bedca, beadc, cadbe, caedb, cdbae, cdeba, cedab, cebda, dcabe, dceab, dabce, daebc, deacb, debac, ecdba, ecadb, edbca, edabc, eadcb, eabdc, abced, baced, cbaed, dbcea, ebcad, acbed, adceb, aecbd, bcaed, bdcea, becad, cabed, cdaeb, ceabd, dcbea, daceb, decba, ecbad, edcab, eacbd, abdec, abecd, badec, baecd, cbdea, cbead, dbaec, dbeca, ebdac, ebacd, acdeb, acebd, adbec, adecb, aedbc, aebcd, bcdea, bcead, bdaec, bdeca, bedac, beacd, cadeb, caebd, cdbea, cdeab, cedba, cebad, dcaeb, dceba, dabec, daecb, deabc, debca, ecdab, ecabd, edbac, edacb, eadbc, eabcd], size: 120