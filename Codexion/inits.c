#include "header.h"


t_variables *init_variables(char **argv)
{
    t_variables *variables;
    variables = malloc(sizeof(t_variables));
    if (!variables)
        return (NULL);
    variables->number_of_coders = atoi(argv[1]);
    variables->time_to_burnout = atoi(argv[2]);
    variables->time_to_compile = atoi(argv[3]);
    variables->time_to_debug = atoi(argv[4]);
    variables->time_to_refactor = atoi(argv[5]);
    variables->number_of_compiles_required= atoi(argv[6]);
    variables->dongle_cooldown = atoi(argv[7]);
    variables->scheduler = argv[8];
    return variables;
}

t_coder *init_coders_array(t_variables *variables)
{
    t_coder *coders;
    int i;

    i = 0;
    coders = malloc(sizeof(t_coder) * variables->number_of_coders);
    if (!coders)
        return (NULL);
    
    while (i < variables->number_of_coders)
    {
        coders[i].id = i + 1;
        coders[i].vars = variables;
        i++;
    }

    return (coders);
}


void start_simulation(t_coder *coders)
{
    int i;
    int j;

    i = 0;
    j = 0;

    while (i < coders[0].vars->number_of_coders)
    {
        pthread_create(&coders[i].thread, NULL, &routine, (void *) &coders[i]);
        i++;
    }

    while (j < coders[0].vars->number_of_coders)
    {
        pthread_join(coders[j].thread, NULL);
        j++;
    }
}
