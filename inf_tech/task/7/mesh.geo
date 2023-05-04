p = 0.1;

a0 = 10;
a1 = 0.5;
a2 = 9;

b0 = a0;
b1 = a1;
b2 = a2;

Point(1) = {0, 0, 0, p};
Point(2) = {0, b0, 0, p};
Point(3) = {a1, b0, 0, p};
Point(4) = {a1, b0-b1, 0, p};
Point(5) = {a1+a2, b0-b1, 0, p};
Point(6) = {a1+a2, b0, 0, p};
Point(7) = {a0, b0, 0, p};
Point(8) = {a0, 0, 0, p};
Point(9) = {a1, b1, 0, p};
Point(10) = {a1+a2, b1, 0, p};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 7};
Line(7) = {7, 8};
Line(8) = {8, 1};
Line(9) = {5, 10};
Line(10) = {10, 9};
Line(11) = {9, 4};

Line Loop(1) = {1, 2, 3, -11, -10, -9, 5, 6, 7, 8};
Line Loop(2) = {4, 9, 10, 11};

Plane Surface(1) = {1};
Plane Surface(2) = {2};

Physical Surface(1) = {1};
Physical Surface(2) = {2};

Physical Line(1) = {8};
Physical Line(2) = {1, 2, 3, 5, 6, 7};