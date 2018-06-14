#include <iostream>
#include <queue>
#include <list>

using namespace std;

struct Node {
    int x, y;
    Node(int x, int y):x(x),y(y){}
    Node(){}
};

void printNode(Node a) {
    cout <<a.x << " " << a.y << endl;
}

int main() {
    int maze[5][5] = {
        {0, 1, 0, 1, 0},
        {0, 1, 0, 1, 0},
        {0, 0, 0, 0, 0},
        {0, 1, 1, 1, 0},
        {0, 0, 0, 1, 0},
    };
    int visited[5][5] = {0};
    list<Node> queue;

    queue.push_back(Node(0, 0));
    visited[0][0] = 1;
    int dead = 0;
    while (!queue.empty()) {
        Node search  = queue.front();
        queue.pop_front();
        int flag = 0;

        //up
        if ((search.y > 0) && (maze[search.x][search.y-1] == 0)) {
            if (visited[search.x][search.y-1] == 0) {
                queue.push_back(Node(search.x, search.y-1));
                visited[search.x][search.y-1] = 1;
            }
        } else {
            flag++;
        }

        //down
        if ((search.y < 4) && (maze[search.x][search.y+1] == 0)) {
            if (visited[search.x][search.y+1] == 0) {
                queue.push_back(Node(search.x, search.y+1));
                visited[search.x][search.y+1] = 1;
            }
        } else {
            flag++;
        }

        //left
        if ((search.x > 0) && (maze[search.x-1][search.y] == 0)) {
            if (visited[search.x-1][search.y] == 0) {
                queue.push_back(Node(search.x-1, search.y));
                visited[search.x-1][search.y] = 1;
            }
        } else {
            flag++;
        }

        //right
        if ((search.x < 4) && (maze[search.x+1][search.y] == 0)) {
            if (visited[search.x+1][search.y] == 0) {
                queue.push_back(Node(search.x+1, search.y));
                visited[search.x+1][search.y] = 1;
            }
        } else {
            flag++;
        }

        if (flag > 2) { //dead road
            dead++;
        }
    }

    cout << dead;
    return 0;
}
