#include "header.h"


int main(int argc, char **argv)
{
    t_variables *variables;
    t_coder *coders_arr;

    if (!main_parser(argc, argv))
        return 1;

    variables = init_variables(argv);
    if (!variables)
        return (1);

    // Array Tester ============================
    coders_arr = init_coders_array(variables);
    // ===========================================

    start_simulation(coders_arr);

    free(coders_arr);
    free(variables);
    return 0;
}