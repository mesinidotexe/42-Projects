/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lst_function_2.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 19:10:07 by vmesini-          #+#    #+#             */
/*   Updated: 2026/01/12 19:10:08 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ps_lstdelone(t_stack *lst)
{
	if (!lst)
		return ;
	free(lst);
}

void	free_list(t_stack *a, t_stack *b)
{
	if (a)
		ps_lstclear(&a);
	if (b)
		ps_lstclear(&b);
}

void	ps_print_stack(t_stack *a)
{
	while (a)
	{
		ft_printf("%d\n", a->number);
		a = a->next;
	}
}

int	ps_lstsize(t_stack *lst)
{
	int	counter;

	if (!lst)
		return (0);
	counter = 0;
	while (lst)
	{
		counter++;
		lst = lst->next;
	}
	return (counter);
}