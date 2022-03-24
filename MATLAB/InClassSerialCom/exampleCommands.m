clc
s.flush()
for counter = 1 : 100
    command = sprintf("counter = %d", counter);
    fprintf("Sending --> %s\n", command);
    writeline(s, command);
    pause(1.0)
    readline(s)
    pause(3)
end
