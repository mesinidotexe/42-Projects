#include "parse.h"

bool all_digits(char **argv)
{
    int i;

    i = 1;
    while (argv[i] && argv[i + 1])
    {
        if (!ft_isdigit(argv[i++][0]))
            return false;
    }
    return true;
}


bool fifo_edf(char **argv)
{
     if (strcmp(argv[8], "fifo") == 0 || strcmp(argv[8], "FIFO") == 0
        || strcmp(argv[8], "edf") == 0 || strcmp(argv[8], "EDF") == 0)
        return true;
    return false;
}


bool main_parser(int argc, char **argv)
{
    if (argc != 9)
    {
        printf("The number of arguments do not match the expected\n");
        return false;
    }
    if (!all_digits(argv))
    {
        printf("Arguments do not match the expected input\n");
        return false;
    }
    if (!fifo_edf(argv))
    {
        printf("Last argument must be 'fifo/FIFO' or 'edf/EDF'\n");
        return false;
    }
    return true;
}