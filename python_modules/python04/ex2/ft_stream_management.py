import sys


def main():
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===')
    sys.stdout.write('Input Stream active. Enter archivist ID: \n')
    id = sys.stdin.readline().strip()
    sys.stdout.write('Input Stream active. Enter status report: \n')
    report = sys.stdin.readline().strip()

    sys.stdout.write(f'[STANDARD] Archive status from {id}: {report}\n')
    sys.stderr.write('[ALERT] System diagnostic: '
                     'Communication channels verified\n')
    sys.stdout.write('[STANDARD] Data transmission complete\n')

    sys.stdout.write('Three-channel communication test successful.')


if __name__ == '__main__':
    main()
