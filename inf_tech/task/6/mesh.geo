p = 0.1;

a = 1;
b = 8;

Point(1) = {0, 0, 0, p};
Point(2) = {0, a, 0, p};
Point(3) = {a, a, 0, p};
Point(4) = {a, 0, 0, p};

Point(5) = {0, b + 0, 0, p};
Point(6) = {0, b + a, 0, p};
Point(7) = {a, b + a, 0, p};
Point(8) = {a, b + 0, 0, p};

Point(9) =  {b + 0, 0, 0, p};
Point(10) = {b + 0, a, 0, p};
Point(11) = {b + a, a, 0, p};
Point(12) = {b + a, 0, 0, p};

Point(13) = {b + 0, b + 0, 0, p};
Point(14) = {b + 0, b + a, 0, p};
Point(15) = {b + a, b + a, 0, p};
Point(16) = {b + a, b + 0, 0, p};

Point(17) = {0, 0, b, p};
Point(18) = {0, a, b, p};
Point(19) = {a, a, b, p};
Point(20) = {a, 0, b, p};

Point(21) = {0, b + 0, b, p};
Point(22) = {0, b + a, b, p};
Point(23) = {a, b + a, b, p};
Point(24) = {a, b + 0, b, p};

Point(25) = {b + 0, 0, b, p};
Point(26) = {b + 0, a, b, p};
Point(27) = {b + a, a, b, p};
Point(28) = {b + a, 0, b, p};

Point(29) = {b + 0, b + 0, b, p};
Point(30) = {b + 0, b + a, b, p};
Point(31) = {b + a, b + a, b, p};
Point(32) = {b + a, b + 0, b, p};

Point(33) = {0 + 0, 0 + 0, b + a, p};
Point(34) = {0 + 0, b + a, b + a, p};
Point(35) = {b + a, b + a, b + a, p};
Point(36) = {b + a, 0 + 0, b + a, p};

Point(37) = {b + 0, b + a, b + a, p};
Point(38) = {b + 0, 0 + 0, b + a, p};

Point(39) = {b + a, b + a, 2*b + a, p};
Point(40) = {b + a, 0 + 0, 2*b + a, p};
Point(41) = {b + 0, b + a, 2*b + a, p};
Point(42) = {b + 0, 0 + 0, 2*b + a, p};

//+
Line(1) = {17, 20};
//+
Line(2) = {20, 19};
//+
Line(3) = {19, 18};
//+
Line(4) = {18, 17};
//+
Line(5) = {17, 1};
//+
Line(6) = {1, 2};
//+
Line(7) = {2, 3};
//+
Line(8) = {3, 4};
//+
Line(9) = {4, 1};
//+
Line(10) = {4, 20};
//+
Line(11) = {19, 3};
//+
Line(12) = {2, 18};
//+
Line(13) = {5, 8};
//+
Line(14) = {8, 7};
//+
Line(15) = {7, 6};
//+
Line(16) = {6, 5};
//+
Line(17) = {5, 21};
//+
Line(18) = {21, 24};
//+
Line(19) = {24, 23};
//+
Line(20) = {23, 22};
//+
Line(21) = {22, 21};
//+
Line(22) = {23, 7};
//+
Line(23) = {6, 22};
//+
Line(24) = {24, 8};
//+
Line(25) = {17, 28};
//+
Line(26) = {28, 31};
//+
Line(27) = {31, 22};
//+
Line(28) = {22, 17};
//+
Line(29) = {17, 33};
//+
Line(30) = {33, 34};
//+
Line(31) = {34, 35};
//+
Line(32) = {35, 36};
//+
Line(33) = {36, 33};
//+
Line(34) = {36, 28};
//+
Line(35) = {35, 31};
//+
Line(36) = {34, 22};
//+
Line(37) = {26, 10};
//+
Line(38) = {11, 27};
//+
Line(39) = {28, 25};
//+
Line(40) = {25, 26};
//+
Line(41) = {26, 27};
//+
Line(42) = {27, 28};
//+
Line(43) = {28, 12};
//+
Line(44) = {25, 9};
//+
Line(45) = {9, 12};
//+
Line(46) = {12, 11};
//+
Line(47) = {11, 10};
//+
Line(48) = {10, 9};
//+
Line(49) = {29, 32};
//+
Line(50) = {32, 31};
//+
Line(51) = {31, 30};
//+
Line(52) = {30, 29};
//+
Line(53) = {29, 13};
//+
Line(54) = {16, 32};
//+
Line(55) = {31, 15};
//+
Line(56) = {14, 30};
//+
Line(57) = {15, 14};
//+
Line(58) = {14, 13};
//+
Line(59) = {13, 16};
//+
Line(60) = {16, 15};
//+
Line(61) = {38, 36};
//+
Line(62) = {38, 37};
//+
Line(63) = {37, 35};
//+
Line(64) = {35, 39};
//+
Line(65) = {39, 41};
//+
Line(66) = {41, 42};
//+
Line(67) = {42, 40};
//+
Line(68) = {40, 39};
//+
Line(69) = {40, 36};
//+
Line(70) = {38, 42};
//+
Line(71) = {37, 41};//+
Curve Loop(1) = {33, -29, 25, -34};

//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {32, 34, 26, -35};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {27, -36, 31, 35};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {28, 29, 30, 36};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {33, 30, 31, 32};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {28, 25, 26, 27};
//+
Plane Surface(6) = {6};

//+
Surface Loop(1) = {3, 6, 4, 1, 5, 2};
//+
Volume(1) = {1};

//+
Curve Loop(7) = {11, 8, 10, 2};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {3, 4, 1, 2};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {9, 6, 7, 8};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {12, -3, 11, -7};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {5, 6, 12, 4};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {10, -1, 5, -9};
//+
Plane Surface(12) = {12};

//+
Surface Loop(2) = {7, 8, 9, 10, 11, 12};
//+
Volume(2) = {2};

//+
Curve Loop(13) = {19, 20, 21, 18};
//+
Plane Surface(13) = {13};
//+
Curve Loop(14) = {15, 16, 13, 14};
//+
Plane Surface(14) = {14};
//+
Curve Loop(15) = {17, 18, 24, -13};
//+
Plane Surface(15) = {15};
//+
Curve Loop(16) = {14, -22, -19, 24};
//+
Plane Surface(16) = {16};
//+
Curve Loop(17) = {20, -23, -15, -22};
//+
Plane Surface(17) = {17};
//+
Curve Loop(18) = {16, 17, -21, -23};
//+
Plane Surface(18) = {18};

//+
Surface Loop(3) = {13, 14, 15, 16, 17, 18};
//+
Volume(3) = {3};

//+
Curve Loop(19) = {58, 59, 60, 57};
//+
Plane Surface(19) = {19};
//+
Curve Loop(20) = {49, -54, -59, -53};
//+
Plane Surface(20) = {20};
//+
Curve Loop(21) = {52, 53, -58, 56};
//+
Plane Surface(21) = {21};
//+
Curve Loop(22) = {55, -60, 54, 50};
//+
Plane Surface(22) = {22};
//+
Curve Loop(23) = {-56, -57, -55, 51};
//+
Plane Surface(23) = {23};
//+
Curve Loop(24) = {49, 50, 51, 52};
//+
Plane Surface(24) = {24};

//+
Surface Loop(4) = {19, 20, 21, 22, 23, 24};
//+
Volume(4) = {4};

//+
Curve Loop(25) = {46, 47, 48, 45};
//+
Plane Surface(25) = {25};
//+
Curve Loop(26) = {40, 37, 48, -44};
//+
Plane Surface(26) = {26};
//+
Curve Loop(27) = {38, -41, 37, -47};
//+
Plane Surface(27) = {27};
//+
Curve Loop(28) = {39, 42, 41, 40};
//+
Plane Surface(28) = {28};
//+
Curve Loop(29) = {-39, 43, -45, -44};
//+
Plane Surface(29) = {29};
//+
Curve Loop(30) = {-38, -46, -43, -42};
//+
Plane Surface(30) = {30};

//+
Surface Loop(5) = {25, 26, 27, 28, 29, 30};
//+
Volume(5) = {5};

//+
Curve Loop(31) = {62, 71, 66, -70};
//+
Plane Surface(31) = {31};
//+
Curve Loop(32) = {32, -69, 68, -64};
//+
Plane Surface(32) = {32};
//+
Curve Loop(33) = {68, 65, 66, 67};
//+
Plane Surface(33) = {33};
//+
Curve Loop(34) = {70, 67, 69, -61};
//+
Plane Surface(34) = {34};
//+
Curve Loop(35) = {64, 65, -71, 63};
//+
Plane Surface(35) = {35};
//+
Curve Loop(36) = {62, 63, 32, -61};
//+
Plane Surface(36) = {36};

//+
Surface Loop(6) = {31, 32, 33, 34, 35, 36};
//+
Volume(6) = {6};

Physical Volume(1) = {1, 2, 3, 4, 5, 6};
Physical Surface(1) = {5};
Physical Surface(2) = {31};
Physical Surface(3) = {14, 9, 25, 19};