from chart_transpose import LyricChordChart


def main():
    chart = LyricChordChart('examples/chart.txt')
    chart.transpose(-1)
    chart.save('examples/transposed.txt')


if __name__ == '__main__':
    main()
