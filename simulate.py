import random
import collections
import time

start = time.time()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
numOfRuns = 10
time_range = 100
event_a_occurence = 10
event_b_occurence = 10
delta_after = 10
delta_before = 1
# Set this to False or True to supresse print debug outputs
DUBUG = True
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



print("I am running", numOfRuns, "trials...\n")

numOfEventsPerRun = []
event_a_positions = []
event_b_positions = []
for run in range(numOfRuns):
    if DUBUG:
        print(80*"=")
        print("Executing trial number =", run)
        print(80*"=")

    # Generate random events
    event_a_positions = []
    event_b_positions = []
    for i in range(event_a_occurence):
        random_num = random.randint(0,time_range-1)
        while random_num in event_a_positions:
            random_num = random.randint(0,time_range-1)
        event_a_positions.append(random_num)
    event_a_positions.sort()
    for i in range(event_b_occurence):
        random_num = random.randint(0,time_range-1)
        while random_num in event_b_positions:
            random_num = random.randint(0,time_range-1)
        event_b_positions.append(random_num)
    event_b_positions.sort()

    if DUBUG:
        print(18*"#")
        print("Event A positions:")
        print(18*"#")
        print(event_a_positions)
        print("\n")
        print(18*"#")
        print("Event B positions:")
        print(18*"#")
        print(event_b_positions)
        print("\n")


    num_of_events = 0
    # Check the correlation of events
    for i in range(len(event_a_positions)):
        for j in range(len(event_b_positions)):
            if event_b_positions[j] >= event_a_positions[i]-delta_before and\
               event_b_positions[j] <= event_a_positions[i]+delta_after:
                if DUBUG:
                    print(27*"-")
                    print("Detected event correlation:")
                    print(27*"-")
                    print("event_a_positions[", i, "] =", event_a_positions[i], "event_b_positions[", j,"] =", event_b_positions[j])
                    print("")
                num_of_events += 1
                break
    
    # Add number of detected event in the current run
    if num_of_events > 0:
        numOfEventsPerRun.append({"run_position": run, "num_of_events": num_of_events})

        
runStats = {}
for runEvent in numOfEventsPerRun:
    if runEvent["num_of_events"] not in runStats.keys():
        runStats[runEvent["num_of_events"]] = 0
    runStats[runEvent["num_of_events"]] = runStats[runEvent["num_of_events"]] + 1

runStats = collections.OrderedDict(sorted(runStats.items()))

print(43*"-")
print("Number of occurrences per number of events:")
print(43*"-")
for num_events, occurance in runStats.items():
    print("Number of events:", num_events, "\tOccurence:", occurance)

print()
print(12*"-")
print("Probability:")
print(12*"-")
for num_events, occurance in runStats.items():
    total_count = 0
    for num_events_nested, occurance_nested in runStats.items():
        if num_events_nested >= num_events:
            total_count += occurance_nested
    print("Num_events >= ", num_events, "\t Occurrence:", total_count, "\t\tProb:", float(total_count)/float(numOfRuns)*100, "%")
    print("Num_events = ", num_events, "\t Occurrence:", occurance, "\t\tProb:", float(occurance)/float(numOfRuns)*100, "%\n")

end = time.time()
print("Execution time: %.2f seconds" % float(end - start))

