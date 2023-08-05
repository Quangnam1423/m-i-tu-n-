#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int , int> > Move;

int x_index[8] = {-2 , -2 , -1 , -1 , 1 , 1 , 2 , 2};
int y_index[8] = {-1 , 1 , -1 , 2 , -2 , 2 , -1 , 1};
int dem = 0;
bool ok = true , visited[8][8] = {0};

void diChuyen(int x , int y)
{
	dem++;
	Move.push_back({x , y});
	visited[x][y] = true;
	if(dem == 64)
	{
		ok = false;
	}
	for (int i = 0 ; i < 8 ; i++ )
	{
		if (!ok) return;
		int u = x + x_index[i];
		int v = y + y_index[i];
		if (u >= 0 && u < 8 && v >= 0 && v < 8 && !visited[u][v])
		{
			diChuyen(u , v);
		}
	}
	dem--;
	visited[x][y] = false;
}

int main()
{
	diChuyen(0 , 0);
	for (int i = 0 ; i < 64 ; i++ )
	{
		std::cout << Move[i].first << " " << Move[i].second << endl;
	}
	return 0;	
} 
