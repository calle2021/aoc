#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() 
{
    ifstream file("input.txt");
    string line;
    vector<int> left;
    vector<int> right;
    
    while(getline(file, line))
    {
        istringstream ss(line);
        int x, y;
        ss >> x >> y;
        left.emplace_back(x);
        right.emplace_back(y);
    }
    sort(left.begin(), left.end());
    sort(right.begin(), right.end());
    int diff = 0;
    int sim = 0;
    for (int i = 0; i < left.size(); i++)
    {
        diff += abs(left[i] - right[i]);
        sim += left[i] * count(right.begin(), right.end(), left[i]);
    }
    cout << diff << endl;
    cout << sim << endl;

    file.close();
}
