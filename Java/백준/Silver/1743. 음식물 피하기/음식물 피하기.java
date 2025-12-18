import java.util.*;
import java.io.*;

public class Main {
    static int R, C, N, ans;
    static int[][] G;
    static int[] dr = {0, 0, -1, 1};
    static int[] dc = {1, -1, 0, 0};

    static class Node {
        int r, c;
        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        int r, c;
        G = new int[R][C];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            r = Integer.parseInt(st.nextToken()) - 1;
            c = Integer.parseInt(st.nextToken()) - 1;
            
            G[r][c] = 1;
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (G[i][j] == 1) {
                    ans = Math.max(ans, bfs(i, j));
                }
            }
        }

        System.out.println(ans);

    }

    static boolean isValid(int r, int c) {
        return 0 <= r && r < R && 0 <= c && c < C && G[r][c] == 1;
    }

    static int bfs(int r, int c) {
        Queue<Node> queue = new ArrayDeque<>();
        queue.offer(new Node(r, c));
        int size = 0;
        while (!queue.isEmpty()) {
            Node cur = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];

                if (isValid(nr, nc)) {
                    G[nr][nc] = 0; // 방문처리
                    size++;
                    queue.offer(new Node(nr, nc));
                }
            }
        }
        return size;
    }
}