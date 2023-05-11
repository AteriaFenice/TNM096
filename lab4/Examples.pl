:- use_module(library(clpfd)).

% Example 1
% ---------------------
generate(1).
generate(X) :- generate(Y), X is Y+1.
test(10000).
goal :- generate(X), test(X), write(X).

% Example 2
% ------------------------------------
generate2(X) :- X in 1 .. 40000.
goal2 :- generate2(X), test(X), write(X).
%  ?-goal2.



% Example 3
% ------------------------------------
t(X) :- X  in 10..19.
s(Y) :- Y  in 19..30.
%  ?-t(A),s(A).



% Example 4
% ------------------------------------
maxValue(X,Y,X) :- X >= Y.
maxValue(X,Y,Y) :- X < Y.

maxValue2(X,Y,X) :- X #>= Y.
maxValue2(X,Y,Y) :- X #< Y.

%  ?-maxValue(7,5,W).
%  ?-maxValue(A,5,W).

%  ?-maxValue2(7,5,W).
%  ?-maxValue2(A,5,W).



% Example 5
% ------------------------------------
adder(X,Y,Z) :- X+Y #= Z.
%  ?-X in 1..4, Y in 2..5, Z in 1..4\/ 19, adder(X,Y,Z).



% Example 6
% ------------------------------------
factorial(0, 1).
factorial(N, F) :-
        N #> 0,
        N1 #= N - 1,
        F #= N * F1,
        factorial(N1, F1).

%  ?-factorial(47, F).
%  ?-factorial(N, 6).
%  ?-factorial(N, H).
