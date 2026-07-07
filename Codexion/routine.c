#include "header.h"

void *routine(void *arg)
{
    t_coder *coder;

    coder = (t_coder *)arg;
    usleep(coder->vars->dongle_cooldown);
    printf("Coder %d\n", coder->id);
    printf("Number of coders %d\n", coder->vars->number_of_coders);
    printf("Time to burnout %d\n", coder->vars->time_to_burnout);
    printf("Time to compile %d\n", coder->vars->time_to_compile);
    printf("Time to debug %d\n", coder->vars->time_to_debug);
    printf("Time to refactor %d\n", coder->vars->time_to_refactor);
    printf("Number of compiles required %d\n", coder->vars->number_of_compiles_required);
    printf("Dongle cooldown %d\n", coder->vars->dongle_cooldown);
    printf("scheduler %s\n", coder->vars->scheduler);
    
    printf("Ending thread\n");

    return(NULL);
}