import java.io.*;
import java.util.*;

public class Solution {
    static StringBuilder sb = new StringBuilder();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int T = nextInt();
        
        for (int t = 1; t <= T; t++) {
            int N = nextInt();
            int[][] arr = new int[N][N]; 

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    arr[i][j] = nextInt();
                }
            }

            sb.append("#").append(t).append("\n");

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    sb.append(arr[N - 1 - j][i]);
                } sb.append(" ");
                for (int j = 0; j < N; j++) {
                    sb.append(arr[N - 1 - i][N - 1 - j]);
                } sb.append(" ");
                for (int j = 0; j < N; j++) {
                    sb.append(arr[j][N - 1 - i]);
                } sb.append("\n");
            }
        }
        System.out.print(sb);
    }

    static String next() throws IOException {
        while (st == null || !st.hasMoreTokens()) {
            String line = br.readLine();
            if (line == null) return null;
            st = new StringTokenizer(line);
        } return st.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }
}