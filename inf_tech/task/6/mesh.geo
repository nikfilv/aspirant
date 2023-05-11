p = 0.25;

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
Line(1) = {1, 4};
//+
Line(2) = {4, 3};
//+
Line(3) = {3, 2};
//+
Line(4) = {2, 1};
//+
Line(5) = {1, 17};
//+
Line(6) = {17, 18};
//+
Line(7) = {18, 2};
//+
Line(8) = {18, 19};
//+
Line(9) = {19, 20};
//+
Line(10) = {20, 17};
//+
Line(11) = {20, 4};
//+
Line(12) = {3, 19};
//+
Line(13) = {11, 12};
//+
Line(14) = {12, 9};
//+
Line(15) = {9, 10};
//+
Line(16) = {10, 11};
//+
Line(17) = {28, 25};
//+
Line(18) = {25, 26};
//+
Line(19) = {26, 27};
//+
Line(20) = {27, 28};
//+
Line(21) = {28, 12};
//+
Line(22) = {9, 25};
//+
Line(23) = {26, 10};
//+
Line(24) = {11, 27};
//+
Line(25) = {31, 15};
//+
Line(26) = {14, 30};
//+
Line(27) = {29, 13};
//+
Line(28) = {16, 32};
//+
Line(29) = {32, 31};
//+
Line(30) = {31, 30};
//+
Line(31) = {30, 29};
//+
Line(32) = {29, 32};
//+
Line(33) = {16, 13};
//+
Line(34) = {13, 14};
//+
Line(35) = {14, 15};
//+
Line(36) = {15, 16};
//+
Line(37) = {23, 24};
//+
Line(38) = {24, 21};
//+
Line(39) = {21, 22};
//+
Line(40) = {22, 23};
//+
Line(41) = {23, 7};
//+
Line(42) = {7, 8};
//+
Line(43) = {8, 5};
//+
Line(44) = {5, 6};
//+
Line(45) = {6, 7};
//+
Line(46) = {8, 24};
//+
Line(47) = {22, 6};
//+
Line(48) = {5, 21};
//+
Line(49) = {30, 23};
//+
Line(50) = {24, 29};
//+
Line(51) = {24, 19};
//+
Line(52) = {18, 21};
//+
Line(53) = {32, 27};
//+
Line(54) = {26, 29};
//+
Line(55) = {19, 26};
//+
Line(56) = {25, 20};
//+
Line(57) = {17, 33};
//+
Line(58) = {22, 34};
//+
Line(59) = {30, 37};
//+
Line(60) = {31, 35};
//+
Line(61) = {25, 38};
//+
Line(62) = {28, 36};
//+
Line(63) = {38, 33};
//+
Line(64) = {38, 36};
//+
Line(65) = {36, 35};
//+
Line(66) = {38, 37};
//+
Line(67) = {37, 34};
//+
Line(68) = {34, 33};
//+
Line(69) = {37, 35};
//+
Line(70) = {37, 41};
//+
Line(71) = {41, 39};
//+
Line(72) = {39, 35};
//+
Line(73) = {38, 42};
//+
Line(74) = {42, 40};
//+
Line(75) = {40, 36};
//+
Line(76) = {42, 41};
//+
Line(77) = {40, 39};

//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {11, -1, 5, -10};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {4, 5, 6, 7};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {3, -7, 8, -12};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {2, 12, 9, 11};
//+
Plane Surface(5) = {5};
//+
Curve Loop(6) = {6, 8, 9, 10};
//+
Plane Surface(6) = {6};
//+
Curve Loop(7) = {15, 16, 13, 14};
//+
Plane Surface(7) = {7};
//+
Curve Loop(8) = {18, 19, 20, 17};
//+
Plane Surface(8) = {8};
//+
Curve Loop(9) = {22, -17, 21, 14};
//+
Plane Surface(9) = {9};
//+
Curve Loop(10) = {16, 24, -19, 23};
//+
Plane Surface(10) = {10};
//+
Curve Loop(11) = {18, 23, -15, 22};
//+
Plane Surface(11) = {11};
//+
Curve Loop(12) = {13, -21, -20, -24};
//+
Plane Surface(12) = {12};
//+
Curve Loop(13) = {45, 42, 43, 44};
//+
Plane Surface(13) = {13};
//+
Curve Loop(14) = {40, 37, 38, 39};
//+
Plane Surface(14) = {14};
//+
Curve Loop(15) = {41, -45, -47, 40};
//+
Plane Surface(15) = {15};
//+
Curve Loop(16) = {44, -47, -39, -48};
//+
Plane Surface(16) = {16};
//+
Curve Loop(17) = {43, 48, -38, -46};
//+
Plane Surface(17) = {17};
//+
Curve Loop(18) = {46, -37, 41, 42};
//+
Plane Surface(18) = {18};
//+
Curve Loop(19) = {35, 36, 33, 34};
//+
Plane Surface(19) = {19};
//+
Curve Loop(20) = {30, 31, 32, 29};
//+
Plane Surface(20) = {20};
//+
Curve Loop(21) = {28, 29, 25, 36};
//+
Plane Surface(21) = {21};
//+
Curve Loop(22) = {30, -26, 35, -25};
//+
Plane Surface(22) = {22};
//+
Curve Loop(23) = {31, 27, 34, 26};
//+
Plane Surface(23) = {23};
//+
Curve Loop(24) = {33, -27, 32, -28};
//+
Plane Surface(24) = {24};
//+
Curve Loop(25) = {49, 37, 50, -31};
//+
Plane Surface(25) = {25};
//+
Curve Loop(26) = {50, -54, -55, -51};
//+
Plane Surface(26) = {26};
//+
Curve Loop(27) = {53, -19, 54, 32};
//+
Plane Surface(27) = {27};
//+
Curve Loop(28) = {18, -55, 9, -56};
//+
Plane Surface(28) = {28};
//+
Curve Loop(29) = {51, -8, 52, -38};
//+
Plane Surface(29) = {29};
//+
Curve Loop(30) = {62, -64, -61, -17};
//+
Plane Surface(30) = {30};
//+
Curve Loop(31) = {61, 63, -57, -10, -56};
//+
Plane Surface(31) = {31};
//+
Curve Loop(32) = {57, -68, -58, -39, -52, -6};
//+
Plane Surface(32) = {32};
//+
Curve Loop(33) = {58, -67, -59, 49, -40};
//+
Plane Surface(33) = {33};
//+
Curve Loop(34) = {59, 69, -60, 30};
//+
Plane Surface(34) = {34};
//+
Curve Loop(35) = {60, -65, -62, -20, -53, 29};
//+
Plane Surface(35) = {35};
//+
Curve Loop(36) = {61, 66, -59, 31, -54, -18};
//+
Plane Surface(36) = {36};
//+
Curve Loop(37) = {65, -69, -66, 64};
//+
Plane Surface(37) = {37};
//+
Curve Loop(38) = {66, 67, 68, -63};
//+
Plane Surface(38) = {38};
//+
Curve Loop(39) = {72, -69, 70, 71};
//+
Plane Surface(39) = {39};
//+
Curve Loop(40) = {72, -65, -75, 77};
//+
Plane Surface(40) = {40};
//+
Curve Loop(41) = {64, -75, -74, -73};
//+
Plane Surface(41) = {41};
//+
Curve Loop(42) = {73, 76, -70, -66};
//+
Plane Surface(42) = {42};
//+
Curve Loop(43) = {74, 77, -71, -76};
//+
Plane Surface(43) = {43};
//+
Surface Loop(1) = {1, 2, 5, 4, 3, 6};
//+
Volume(1) = {1};
//+
Surface Loop(2) = {17, 13, 15, 18, 16, 14};
//+
Volume(2) = {2};
//+
Surface Loop(3) = {7, 11, 10, 12, 9, 8};
//+
Volume(3) = {3};
//+
Surface Loop(4) = {19, 22, 23, 24, 21, 20};
//+
Volume(4) = {4};
//+
Surface Loop(5) = {26, 25, 33, 32, 31, 38, 28, 29, 6, 14, 36};
//+
Volume(5) = {5};
//+
Surface Loop(6) = {43, 41, 40, 39, 42, 37};
//+
Volume(6) = {6};
