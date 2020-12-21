from functools import reduce

def getGroupAnswers(filename):
    with open(filename) as f:
        answers = []
        for line in f:
            line = line.strip()
            if line == '':
                yield answers
                answers = []
            else:
                answers.append(set(line))

        yield answers


if __name__ == "__main__":
    answers = list(getGroupAnswers('data/day6.txt'))
    print(sum(len(set.union(*ans)) for ans in answers))
    print(sum(len(set.intersection(*ans)) for ans in answers))