#include<iostream>

using namespace std;

int main(){
	float a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, d, dx, dy, dz, x, y, z;
	cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3 >> c1 >> c2 >> c3 >> d1 >> d2 >> d3;
	d = a1*b2*c3 + b1*c2*a3 + a2*b3*c1 - c1*b2*a3 - b1*a2*c3 - a1*b3*c2;
	dx = d1*b2*c3 + b1*c2*d3 + d2*b3*c1 - c1*b2*d3 - b1*d2*c3 - c2*b3*d1;
	dy = a1*d2*c3 + d1*c2*a3 + a2*d3*c1 - c1*d2*a3 - d1*a2*c3 - c2*d3*a1;
	dz = a1*b2*d3 + b1*d2*a3 + a2*b3*d1 - d1*b2*a3 - b1*a2*d3 - d2*b3*a1;
	if (d == 0){
		if (dx == 0 && dy == 0 && dz == 0){
			cout << "Vo so nghiem";
		}
		else{
			cout << "Vo nghiem";
		}
	}
	else{
		x = dx/d;
		y = dy/d;
		z = dz/d;
		cout << "x = " << x << ", y = " << y << ", z = " << z;
	}
	return 0;
}
