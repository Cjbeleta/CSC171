%% Grumpy was in front of Dopey.
%% Stumpy was behind Sneezy and Doc.
%% Doc was in front of Droopy and Happy.
%% Sleepy was behind Stumpy, Smelly and Happy.
%% Happy was in front of Sleepy, Smelly and Bashful.
%% Bashful was behind Smelly, Droopy and Sleepy.
%% Sneezy was in front of Dopey. 
%% Smelly was in front of Grumpy, Stumpy and Sneezy.
%% Dopey was in front of Droopy.
%% Sleepy was in front of Grumpy and Bashful.
%% Dopey was behind Sneezy, Doc and Sleepy.
%% Stumpy was in front of Dopey. 
%% Smelly was behind Doc.

%% What is the order of the dwarves?

%% Answer: Doc, Happy, Smelly, Sneezy, Stumpy, Sleepy, Grumpy, Dopey, Droopy, Bashful

% define start.
start() :- 
	% randomly initialized list will be sorted based on facts given.
	% first arg - list of dwarves, second arg - list for comparison, last arg - store
	order([grumpy, bashful, droopy, dopey, doc, happy, sneezy, smelly, sleepy, stumpy], [grumpy, bashful, droopy, dopey, doc, happy, sneezy, smelly, sleepy, stumpy], []).

% this function will check the placement of the dwarves.
order([Dwarf|Others], [First|Rest], Order) :-
	% if First is in front of Next, then the function will move to check the Rest.
	(front(Dwarf, Next) -> write(Order), nl, order([Dwarf|Others], Rest, [, Next])
			% if First is behind Next, the list will be rearranged.
		; write(Order), nl, order(List, Rest, )
	).