#ifndef HEADER_H
# define HEADER_H

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include "parser/parse.h"

typedef struct s_variables
{
	int number_of_coders;
    int time_to_burnout;
    int time_to_compile;
    int time_to_debug;
    int time_to_refactor;
    int number_of_compiles_required;
    int dongle_cooldown;
    char *scheduler;
}	t_variables;


typedef struct s_coder
{
    int             id;
    pthread_t       thread;
    t_variables     *vars;
} t_coder;


void *routine(void *arg);

t_variables *init_variables(char **argv);
t_coder *init_coders_array(t_variables *variables);
void start_simulation(t_coder *coders);
#endif