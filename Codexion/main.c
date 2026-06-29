#include "header.h"


t_variables *init_variables(int argc, char **argv)
{
    t_variables *variables;

    variables = malloc(sizeof(t_variables) * (argc - 1));
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



void *routine(void *number_of_thread)
{
    long id = (long)number_of_thread;
    printf("Test from thread %ld\n", id);
    sleep(3);
    printf("Ending thread %ld\n", id);
    return(NULL);
}



pthread_t *init_coders_array(int number_of_coders)
{
    pthread_t *coders;
    int i;
    int j;

    coders = malloc(sizeof(pthread_t) * number_of_coders);
    if (!coders)
        return (NULL);
    i = 0;
    j = 0;

    while (i < number_of_coders)
    {
        pthread_create(&coders[i], NULL, &routine, (void *)(long) i + 1);
        i++;
    }

    while (j < number_of_coders)
    {
        pthread_join(coders[j++], NULL);
    }
    
    return (coders);
}


int main(int argc, char **argv)
{
    t_variables *variables;
    pthread_t *coders_arr;
    if (!main_parser(argc, argv))
        return 1;
    variables = init_variables(argc, argv);
    if (!variables)
        return (1);


    // Variable Tester ===========================
    printf("%d\n", variables->number_of_coders);
    printf("%d\n", variables->time_to_burnout);
    printf("%d\n", variables->time_to_compile);
    printf("%d\n", variables->time_to_debug);
    printf("%d\n", variables->time_to_refactor);
    printf("%d\n", variables->number_of_compiles_required);
    printf("%d\n", variables->dongle_cooldown);
    printf("%s\n", variables->scheduler);
    // ===========================================


    // Threads Tester ============================
    coders_arr = init_coders_array(variables->number_of_coders);
    // ===========================================

    free(coders_arr);
    free(variables);
    return 0;
}