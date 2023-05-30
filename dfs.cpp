#include <iostream>
#include <map>
#include <list>
#include <queue>
using namespace std;


map<int, list<int>> m;

void addEdge(int x, int y){
    m[x].push_back(y);
    m[y].push_back(x);
}

//BFS Traversal
void bfs(int src){
    map<int, bool> visited;       
    queue<int> q;             

    q.push(src);
    visited[src]=true;

    while(!q.empty()){
        int front_ele = q.front();
        q.pop();
        cout<<front_ele<<" ";

        for(auto nbr : m[front_ele]){
            if(!visited[nbr]){
                q.push(nbr);
                visited[nbr]=true;
            }
        }
    }
}

//DFS Traversal
void dfs_helper(int src, map<int, bool> &visited){
    cout<<src<<" ";
    visited[src]=true;

    for(auto nbr : m[src]){
        if(!visited[nbr]){
            dfs_helper(nbr, visited);
        }
    }
}
void dfs(int src){
    map<int, bool> visited;
    dfs_helper(src, visited);
}


int main(){

    int edge, n1, n2, root;

    cout<<"Enter the root node: ";
    cin>>root;

    cout<<"\nEnter the no. of edges: ";
    cin>>edge;

    for(int i=0; i<edge; i++)
    {
        cout<<"Add edge: "; 
        cin>>n1; cin>>n2;
        addEdge(n1,n2);
        
    }

    cout<<"\nBFS: ";
    bfs(root);

    cout<<"\nDFS: ";
    dfs(root);
}


