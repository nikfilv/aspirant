LX = 1.0;
LY = 2.0;

r = 0.5;
p = LX /30;

Point (1) = { 0, 0, 0, p};
Point (2) = { 0, LY , 0, p};
Point (3) = { LX , LY , 0, p};
Point (4) = { LX , 0, 0, p};

Point (5) = {0, LY/2, 0, p};
Point (6) = {0, LY /2+r, 0, p};
Point (7) = {0, LY/2-r, 0, p};
Point (8) = {r, LY/2, 0, p};

Circle (1) = {6, 5, 8};
Circle (2) = {8, 5, 7};

Line (3) = {6, 2};
Line (4) = {2, 3};
Line (5) = {3, 4};
Line (6) = {4, 1};
Line (7) = {1, 7};

Line Loop (8) = {3, 4, 5, 6, 7, -2, -1};

Plane Surface (9) = {8};

Physical Surface (1) = {9};

Physical Line (1) = {4};
Physical Line (2) = {3, 7};
Physical Line (3) = {6};
Physical Line (4) = {1, 2, 5};