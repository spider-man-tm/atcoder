#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> G(10,vector<int>(10));
vector<vector<int>> memo(10,vector<int>(10));
int t_sum = 1;


void dfs(const vector<vector<int>> &G, int y, int x){
    memo[y][x] = 0;
    int up = y + 1;
    int down = y - 1;
    int right = x + 1;
    int left = x - 1;

    if(up < 10 and memo[up][x] == 1){
        t_sum += 1;
        dfs(memo,up,x);
    }
    if(down >= 0 and memo[down][x] == 1){
        t_sum += 1;
        dfs(memo,down,x);
    }
    if(right < 10 and memo[y][right] == 1){
        t_sum += 1;
        dfs(memo,y,right);
    }
    if(left >= 0 and memo[y][left] == 1){
        t_sum += 1;
        dfs(memo,y,left);
    }
}

int main(){
    int sum = 0;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            char s;
            cin >> s;
            if(s == 'x'){
                G[i][j] = 0;
                memo[i][j] = 0;
            } 
            if(s == 'o'){
                G[i][j] = 1;
                memo[i][j] = 1;
                sum += 1;
            }
        }
    }
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if(G[i][j] == 0){
                dfs(memo,i,j);
                if(t_sum == sum + 1){
                    cout << "YES" << endl;
                    return 0;
                }
                else{
                    t_sum = 1;
                    for(int i = 0; i < 10; i++){
                        for(int j = 0; j < 10; j++){
                            if(G[i][j] == 0){
                                memo[i][j] = 0;
                            }
                            if(G[i][j] == 1){
                                memo[i][j] = 1;
                            }
                        }
                    }
                }
            }
        }
    }
    cout << "NO" << endl;
    return 0;
}
