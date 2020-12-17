get_timetable([37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,457,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,431,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19]).

% No more buses to wait for, return wait time.
wait_for_buses([], _, WaitTime, WaitTime, _).

% Current bus is not applicable (x), ignore.
wait_for_buses([x|Buses], AllBuses, Result, WaitTime, Step) :-
    wait_for_buses(Buses, AllBuses, Result, WaitTime, Step).

% Current bus arrives as scheduled, look for next bus.
wait_for_buses([Bus|Buses],AllBuses, Result, WaitTime, Step) :-
    nth0(Mins, AllBuses, Bus),
    Offset is WaitTime+Mins,
    0 is Offset mod Bus,
    NewStep is Step * Bus,
    wait_for_buses(Buses, AllBuses, Result, WaitTime, NewStep), !.

% Current bus didn't arrive as scheduled, wait for the multiple of all previous buses (to preserve schedule)
wait_for_buses(Buses, AllBuses, Result, WaitTime, Step) :-
    NewWaitTime is WaitTime + Step,
    wait_for_buses(Buses, AllBuses, Result, NewWaitTime, Step).

solve(X) :-
    get_timetable(Buses),
    wait_for_buses(Buses, Buses, X, 0, 1).
