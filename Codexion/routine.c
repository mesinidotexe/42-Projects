#include "header.h"

void *routine(void *arg)
{
    t_coder *coder;

    coder = (t_coder *)arg;
    usleep(coder->vars->dongle_cooldown);
    printf("Coder %d\n", coder->id);
    
    printf("Ending thread\n");

    return(NULL);
}