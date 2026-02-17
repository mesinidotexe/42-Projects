/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 17:28:12 by vmesini-          #+#    #+#             */
/*   Updated: 2025/12/16 17:31:52 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"
# include <limits.h>
# include <stdarg.h>
# include <stdbool.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

typedef struct s_stack
{
	int				number;
	int				index;
	struct s_stack	*next;
}					t_stack;

// Args parsing
int					count_numbers(char **argv);
char				**split_all(char **argv, char **splitted);
int					validate_splitted(char **splitted, char *prog_name);

// Data validation
int					check_data(int argc, char *argv[]);
int					has_duplicates(int argc, char **argv);
int					overflow(int argc, char *argv[]);
int					args_are_int(int argc, char *argv[]);
int					empty_strings(int argc, char **argv);

// Utils
void				error(void);
int					find_min_index(t_stack *stack);
int					find_max_index(t_stack *a);
void				indexing(t_stack *a);

// Data Order
int					inorder(t_stack *Lista);
t_stack				*arg_to_stack(t_stack *a, char *argv[]);

// Lists/Stack
void				ps_print_stack(t_stack *a);
void				free_list(t_stack *a, t_stack *b);
t_stack				*ps_lstnew(int content);
void				ps_lstclear(t_stack **lst);
void				ps_lstadd_back(t_stack **lst, t_stack *new);
void				ps_lstadd_front(t_stack **lst, t_stack *new);
t_stack				*ps_lstlast(t_stack *lst);
void				ps_lstdelone(t_stack *lst);
int					ps_lstsize(t_stack *lst);

// Sorting
void				sorting(t_stack *a, t_stack *b);
void				general(t_stack **a, t_stack **b);

// operations
void				sa(t_stack *a);
void				sb(t_stack *b);
void				ss(t_stack *a, t_stack *b);
bool				pa(t_stack **a, t_stack **b);
void				pb(t_stack **b, t_stack **a);
void				ra(t_stack *a);
void				rb(t_stack *b);
void				rr(t_stack *a, t_stack *b);
void				rra(t_stack *a);
void				rrb(t_stack *b);

#endif