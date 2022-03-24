clc
clear s   % This closes the device from the prior run
s = serialport("/dev/cu.usbmodem2101", 9600, "Timeout", 3);
s.flush()
% pause(1.0);
% fprintf("Sending --> Hello");
% writeline(s, "Hello");
% pause(1.0);
% readline(s)
fprintf("Ready\n")

