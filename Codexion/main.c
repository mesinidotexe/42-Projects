#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>



int *init_variables(int argc, char **argv)
{
    int *variables;
    int i;

    variables = malloc(sizeof(int) * (argc - 1));
    if (!variables)
        return (NULL);
    i = 0;
    while(i < argc - 1)
    {
        variables[i] = atoi(argv[i + 1]);
        i++;
    }
    if (variables)
    return (variables);
}



int main(int argc, char **argv)
{
    int *variables;
    int i;

    variables = init_variables(argc, argv);
    i = 0;
    if (!variables)
        return (1);
    // Tester
    while (variables[i])
        printf("%d\n", variables[i++]);

    free(variables);
    return 0;
}