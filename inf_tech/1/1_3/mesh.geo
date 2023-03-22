LX = 1;
LY = 1;

r = 0.2;

x0 = LX / 2;
y0 = LY / 2;

p1 = LY / 60;
p2 = r / 20;

Point(1) = {0, 0, 0, p1};
Point(2) = {0, LY, 0, p1};
Point(3) = {LX, LY, 0, p1};
Point(4) = {LX, 0, 0, p1};

Point(5) = {x0, y0, 0, p2};

Point(6) = {x0, y0 + r, 0, p2};
Point(7) = {x0 + r, y0, 0, p2};
Point(8) = {x0, y0 - r, 0, p2};
Point(9) = {x0 - r, y0, 0, p2};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Circle(5) = {6, 5, 7};
Circle(6) = {7, 5, 8};
Circle(7) = {8, 5, 9};
Circle(8) = {9, 5, 6};

Line Loop(1) = {1, 2, 3, 4};
Line Loop(2) = {5, 6, 7, 8};

Plane Surface(1) = {1, 2};
Plane Surface(2) = {2};

Physical Surface(1) = {2};
Physical Surface(2) = {1};

Physical Line(1) = {1};
Physical Line(2) = {3};
Physical Line(3) = {2};
Physical Line(4) = {4};
