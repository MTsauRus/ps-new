import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        int r, c, k, count;

        public Node(int k, int r, int c, int count) {
            this.k = k;
            this.r = r;
            this.c = c;
            this.count = count;
        }
    }

    static int[] dr = {-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2};
    static int[] dc = {0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1};

    static int K, C, R;
    static int[][] map;
    static boolean[][][] visited; // k, r, c

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        K = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        C = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        
        map = new int[R][C];
        visited = new boolean[K+1][R][C]; // 기본값 False

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        bfs();
    }

    static void bfs() {
        Queue<Node> queue = new ArrayDeque<>();

        queue.offer(new Node(0, 0, 0, 0)); // offer: 실패 시 False. add: 실패 시 exception
        visited[0][0][0] = true;

        while (!queue.isEmpty()) {
            Node cur = queue.poll(); // poll: 실패 시 false. remove: 실패 시 exception

            // 목표 도달 시 리턴
            if (cur.r == R-1 && cur.c == C-1) {
                System.out.println(cur.count);
                return;
            }

            // 상하좌우
            for (int i = 0; i < 4; i++) {
                int nr = cur.r + dr[i];
                int nc = cur.c + dc[i];

                if (check(nr, nc) && !visited[cur.k][nr][nc]) {
                    visited[cur.k][nr][nc] = true;
                    queue.offer(new Node(cur.k, nr, nc, cur.count+1));
                }
            }
            if (cur.k < K) {
                for (int i = 4; i < 12; i++) {
                    int nr = cur.r + dr[i];
                    int nc = cur.c + dc[i];

                    if (check(nr, nc) && !visited[cur.k+1][nr][nc]) {
                        visited[cur.k+1][nr][nc] = true;
                        queue.offer(new Node(cur.k+1, nr, nc, cur.count+1));
                    }
                }
            }
        }
        System.out.println(-1);
    }

    static boolean check(int r, int c) {
        return 0 <= r && r < R && 0 <= c && c < C && map[r][c] != 1;
    }
}