#include "header.h"


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
    return (variables);
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
        pthread_create(&coders[i], NULL, &routine, (void *)(long) i);
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
    int *variables;
    pthread_t *coders_info;
    
    variables = init_variables(argc, argv);
    if (!variables)
        return (1);


    // Variable Tester ===========================
    int i;
    i = 0;
    while (i < argc - 1)
        printf("%d\n", variables[i++]);
    // ===========================================


    // Threads Tester ============================
    coders_info = init_coders_array(variables[0]);
    // ===========================================

    free(coders_info);
    free(variables);
    return 0;
}