LX = 1;
LY = 1;

r = 0.07;

x0 = LX * 1 / 2;
y0 = LY * 3 / 4;

x1 = LX * 1 / 4;
y1 = LY * 2 / 6;

x2 = LX * 3 / 4;
y2 = LY * 2 / 6;

x3 = LX * 1 / 2;
y3 = LY * 1 / 6;

x4 = LX * 3 / 4;
y4 = LY * 1 / 6;

p1 = LY / 60;
p2 = r / 20;

Point(1) = {0, 0, 0, p1};
Point(2) = {0, LY, 0, p1};
Point(3) = {LX, LY, 0, p1};
Point(4) = {LX, 0, 0, p1};

Point(101) = {0, LY / 2, 0, p1};
Point(102) = {LX, LY/ 2, 0, p1};

Point(5) = {x0, y0, 0, p2};

Point(6) = {x0, y0 + r, 0, p2};
Point(7) = {x0 + r, y0, 0, p2};
Point(8) = {x0, y0 - r, 0, p2};
Point(9) = {x0 - r, y0, 0, p2};

Point(10) = {x1, y1, 0, p2};

Point(11) = {x1, y1 + r, 0, p2};
Point(12) = {x1 + r, y1, 0, p2};
Point(13) = {x1, y1 - r, 0, p2};
Point(14) = {x1 - r, y1, 0, p2};

Point(15) = {x2, y2, 0, p2};

Point(16) = {x2, y2 + r, 0, p2};
Point(17) = {x2 + r, y2, 0, p2};
Point(18) = {x2, y2 - r, 0, p2};
Point(19) = {x2 - r, y2, 0, p2};

Point(20) = {x3, y3, 0, p2};

Point(21) = {x3, y3 + r, 0, p2};
Point(22) = {x3 + r, y3, 0, p2};
Point(23) = {x3, y3 - r, 0, p2};
Point(24) = {x3 - r, y3, 0, p2};

Point(25) = {x4, y4, 0, p2};

Point(26) = {x4, y4 + r, 0, p2};
Point(27) = {x4 + r, y4, 0, p2};
Point(28) = {x4, y4 - r, 0, p2};
Point(29) = {x4 - r, y4, 0, p2};



// Line(1) = {1, 2};
Line(2) = {2, 3};
// Line(3) = {3, 4};
Line(4) = {4, 1};

Line(101) = {101, 102};
Line(102) = {1, 101};
Line(103) = {101, 2};
Line(104) = {3, 102};
Line(105) = {102, 4};

Circle(5) = {6, 5, 7};
Circle(6) = {7, 5, 8};
Circle(7) = {8, 5, 9};
Circle(8) = {9, 5, 6};

Circle(9) = {11, 10, 12};
Circle(10) = {12, 10, 13};
Circle(11) = {13, 10, 14};
Circle(12) = {14, 10, 11};

Circle(13) = {16, 15, 17};
Circle(14) = {17, 15, 18};
Circle(15) = {18, 15, 19};
Circle(16) = {19, 15, 16};

Circle(17) = {21, 20, 22};
Circle(18) = {22, 20, 23};
Circle(19) = {23, 20, 24};
Circle(20) = {24, 20, 21};

Circle(21) = {26, 25, 27};
Circle(22) = {27, 25, 28};
Circle(23) = {28, 25, 29};
Circle(24) = {29, 25, 26};

// Line Loop(1) = {1, 2, 3, 4};

Line Loop(2) = {5, 6, 7, 8};
Line Loop(3) = {9, 10, 11, 12};
Line Loop(4) = {13, 14, 15, 16};
Line Loop(5) = {17, 18, 19, 20};
Line Loop(6) = {21, 22, 23, 24};

Line Loop(7) = {4, 102, 101, 105};
Line Loop(8) = {-101, 103, 2, 104};

// Plane Surface(1) = {1, 2, 3, 4, 5, 6};

Plane Surface(2) = {2};
Plane Surface(3) = {3};
Plane Surface(4) = {4};
Plane Surface(5) = {5};
Plane Surface(6) = {6};

Plane Surface(7) = {7, 2};
Plane Surface(8) = {8, 3, 4, 5, 6};

// Physical Surface(1) = {1};
Physical Surface(2) = {2};
Physical Surface(3) = {3};
Physical Surface(4) = {4};
Physical Surface(5) = {5};
Physical Surface(6) = {6};

Physical Surface(7) = {7};
Physical Surface(8) = {8};

Physical Line(1) = {102, 103};
Physical Line(2) = {104, 105};
Physical Line(3) = {2};
Physical Line(4) = {4};
