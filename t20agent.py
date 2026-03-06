from tools import show_batting_stats
from tools import show_bowling_stats
from tools import show_matches
from llm_config import generate_analysis
from helpers import print_line


def main():

    print_line()
    print("T20 WORLD CUP 2026 AGENTIC AI ANALYSIS")
    print_line()

    show_batting_stats()
    print_line()

    show_bowling_stats()
    print_line()

    show_matches()
    print_line()

    generate_analysis()
    print_line()


if __name__ == "__main__":
    main()
