def loadInstructions(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            inst, arg = line.split(' ')
            yield inst, int(arg)

def run(prog):
    idx = 0
    acc = 0
    instructions = {
        'nop': lambda arg, idx, acc: (idx + 1,   acc),
        'jmp': lambda arg, idx, acc: (idx + arg, acc),
        'acc': lambda arg, idx, acc: (idx + 1,   acc + arg),
    }

    hist = set()
    while idx < len(prog):
        if idx in hist:
            return acc, False

        hist.add(idx)
        inst, arg = prog[idx]
        idx, acc = instructions[inst](arg, idx, acc)

    return acc, True


def repair(prog):
    swap = 'nop', 'jmp'
    for idx in range(len(prog)):
        inst, arg = prog[idx]
        if inst in swap:
            prog[idx] = (swap[1 - swap.index(inst)], arg)
            acc, succ = run(prog)
            if succ:
                return acc, prog
            
            # Rollback
            prog[idx] = (inst, arg)


if __name__ == "__main__":
    prog = list(loadInstructions('data/day8.txt'))
    print(run(prog)[0])
    print(repair(prog)[0])