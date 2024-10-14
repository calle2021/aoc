from aocd.models import Puzzle
import argparse
import subprocess
import re

class print_colors:
    SUCCESS = '\033[92m'
    FAIL = '\033[91m'
    RUNNING = '\033[96m'
    RESTORE = "\033[0m"

def run(data):
    res = subprocess.run(
        ["python3", args.solution],
        input=data,
        text=True,
        capture_output=True
    )
    print_output(res)
    ans = get_answers(res)
    return ans

def get_answers(msg):
    return re.findall(r"\[ANSWER\]=(.+?),", msg.stdout)

def print_output(msg):
    print(msg.stdout)

def run_example(i, example, part):
    print(f"{print_colors.RUNNING}########################## running example {i} ##########################\033[0m")
    res = run(example.input_data)
    ans = res[0] if part == "a" else res[1]
    example_ans = example.answer_a if part == "a" else example.answer_b
    if ans == example_ans:
        print(f"{print_colors.SUCCESS}example {i} succeeded\nexample answer {example.answer_a}\nyour answer {ans}\n\033[0m")
        print(f"{print_colors.FAIL}{example.input_data}{print_colors.RESTORE}")
        return True
    print(f"{print_colors.FAIL}example {i} failed\nexample answer {example.answer_a}\nyour answer {ans}\n{print_colors.RESTORE}")
    print(f"{print_colors.FAIL}{example.input_data}{print_colors.RESTORE}")
    return False

def run_examples(puzzle, part):
    results = []
    for i, example in enumerate(puzzle.examples):
        results.append(run_example(i, example, part))
    return all(results)

def run_input(puzzle):
    print("running input data...")
    result = run(puzzle.input_data)
    if not result:
        print(f"{print_colors.FAIL} no answers found.\033[0m")
    elif len(result) == 1:
        puzzle.answer_a = result[0]
    elif len(result) == 2:
        puzzle.answer_a = result[0]
        puzzle.answer_b = result[1]
    else:
        print(f"{print_colors.FAIL} Too many answers found.\033[0m")

def main():
    example_a_results = False
    example_b_results = False
    if args.run_examples:
        if args.run_part_1:
            example_a_results = run_examples(puzzle, "a")
        if args.run_part_2:
            example_b_results = run_examples(puzzle, "b")
    if args.run_input:
        if not example_a_results or not example_b_results:
            input(f"{print_colors.FAIL}warning submitting without running examples, continue?\033[0m")
        run_input(puzzle)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int, help="Puzzle day", required=True)
    parser.add_argument("-y", "--year", type=int, help="Puzzle year", required=True)
    parser.add_argument("-s", "--solution", type=str, help="Solution", required=True)
    parser.add_argument("-e", "--run-examples", action=argparse.BooleanOptionalAction, default=False, help="Run examples.")
    parser.add_argument("-i", "--run-input", action=argparse.BooleanOptionalAction, default=False, help="Run input.")
    parser.add_argument("-a", "--run-part-1", action=argparse.BooleanOptionalAction, default=False, help="Run part 1.")
    parser.add_argument("-b", "--run-part-2", action=argparse.BooleanOptionalAction, default=False, help="Run part 2.")
    parser.add_argument("-f", "--force-submit", action=argparse.BooleanOptionalAction, default=False, help="Force submit even if some examples not ran or has failed.")
    args = parser.parse_args()
    puzzle = Puzzle(day=args.day, year=args.year)
    main()