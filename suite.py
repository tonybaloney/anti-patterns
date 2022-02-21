"""
A benchmark suite for Performance Anti-Patterns
"""
import timeit
import pathlib
import sys
from statistics import fmean
from rich.console import Console
from rich.table import Table
from rich.text import Text
import cProfile

REPEAT = 5
TIMES = 5

if __name__ == "__main__":
    table = Table(title=f"Anti-Pattern Benchmark Suite, repeat={REPEAT}, number={TIMES}")

    table.add_column("Pattern", justify="right", style="cyan", no_wrap=True)
    table.add_column("Benchmark", justify="right", style="cyan", no_wrap=True)
    table.add_column("Repeat", style="magenta")
    table.add_column("Min", style="magenta", width=7)
    table.add_column("Max", style="magenta", width=7)
    table.add_column("Mean", style="magenta", width=7)
    table.add_column("Min (+)", style="blue", width=15)
    table.add_column("Max (+)", style="blue", width=15)
    table.add_column("Mean (+)", style="blue", width=15)

    profiles_out = pathlib.Path(__file__).parent / 'profiles'
    if not profiles_out.exists():
        profiles_out.mkdir()
    n = 0

    for f in pathlib.Path(__file__).parent.glob("bench_*.py"):
        if len(sys.argv) > 1 and f.stem != f"bench_{sys.argv[1]}":
            continue
        i = __import__(f.stem, globals(), locals(), )
        if hasattr(i, "__benchmarks__"):
            for benchmark in i.__benchmarks__:
                n += 1
                func1, func2, desc = benchmark
                with cProfile.Profile() as pr:
                    without_result = timeit.repeat(func1, repeat=REPEAT, number=TIMES)
                    with_result = timeit.repeat(func2, repeat=REPEAT, number=TIMES)

                delta_mean = (abs(fmean(with_result) - fmean(without_result)) / fmean(without_result)) * 100.0
                delta_min = (abs(min(with_result) - min(without_result)) / min(without_result)) * 100.0
                delta_max = (abs(max(with_result) - max(without_result)) / max(without_result)) * 100.0

                if min(with_result) < min(without_result):
                    fdelta_min = Text(f"{min(with_result):.3f} ({delta_min:.1f}%)", style="green")
                else:
                    fdelta_min = Text(f"{min(with_result):.3f} (-{delta_min:.1f}%)", style="red")

                if max(with_result) < max(without_result):
                    fdelta_max = Text(f"{max(with_result):.3f} ({delta_max:.1f}%)", style="green")
                else:
                    fdelta_max = Text(f"{max(with_result):.3f} (-{delta_max:.1f}%)", style="red")

                if fmean(with_result) < fmean(without_result):
                    fdelta_mean = Text(f"{fmean(with_result):.3f} ({delta_mean:.1f}%)", style="green")
                else:
                    fdelta_mean = Text(f"{fmean(with_result):.3f} (-{delta_mean:.1f}%)", style="red")

                table.add_row(str(n),
                              desc,
                              str(TIMES * REPEAT),
                              "{:.3f}".format(min(without_result)),
                              "{:.3f}".format(max(without_result)),
                              "{:.3f}".format(fmean(without_result)),
                              fdelta_min,
                              fdelta_max,
                              fdelta_mean,
                              )

    console = Console(width=150)
    console.print(table)
