"""
The goal of the Tower of Hanoi puzzle is moving all the disks to the last rod. To do that, you must follow three simple rules:
    You can move only top-most disks.
    You can move only one disk at a time.
    You cannot place larger disks on top of smaller ones.
"""
def hanoi_solver(n):
    A = list(range(n, 0, -1))
    B = []
    C = []
    
    towers = [A, B, C]
    states = []

    def record():
        states.append(f"{towers[0]} {towers[1]} {towers[2]}")

    record()

    def move(k, source, helper, target):
        if k == 0:
            return
        
        move(k - 1, source, target, helper)
        
        disk = towers[source].pop()
        towers[target].append(disk)
        record()
        
        move(k - 1, helper, source, target)

    move(n, 0, 1, 2)

    return "\n".join(states)

if __name__ == "__main__":
    print(hanoi_solver(3))