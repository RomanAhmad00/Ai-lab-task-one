# Lab 2 - Intelligent Agents and the PEAS Framework
# All Lab 2 code in one file.
# Part 1: Reflex agent (lab2_percepts.py)
# Part 2: Stateful agent (lab2_model.py)
# Part 3: Check trace (lab2_check.py)
#
# Run: python lab2_all.py


# ---------------- Part 1: Reflex agent ----------------

class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"


# ---------------- Part 2: Stateful agent ----------------

class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        should_send = target != self.previous_mode
        self.previous_mode = target
        return target, should_send


# ---------------- Main: run both parts ----------------

def main():
    print("Part 1: Reflex agent")
    agent = ClassroomAgent()
    percepts = [(29, True), (29, True), (20, True),
                (26, True), (19, True), (29, False)]
    for step, percept in enumerate(percepts, 1):
        print(step, percept, "target mode", agent.act(*percept))

    print()
    print("Part 3: Stateful agent check")
    agent = StatefulClassroomAgent()
    percepts = [
        (29, True),
        (29, True),
        (26, True),
        (20, True),
        (19, True),
        (29, False),
        (29, False),
    ]

    print("step | previous mode | percept | target | command")
    for step, percept in enumerate(percepts, 1):
        previous = agent.previous_mode
        target, should_send = agent.act(*percept)
        command = "Send" if should_send else "No command"
        print(step, previous, percept, target, command, sep=" | ")


if __name__ == "__main__":
    main()
