from chart_transpose import LyricChordChart


def main():
    chart = LyricChordChart('chart.txt')
    chart.transpose(-1)
    chart.save('transposed.txt')


if __name__ == '__main__':
    main()
