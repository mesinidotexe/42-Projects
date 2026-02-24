/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   data_order.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 19:02:49 by vmesini-          #+#    #+#             */
/*   Updated: 2026/01/12 19:02:51 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	inorder(t_stack *lista)
{
	if (!lista)
		return (false);
	while (lista->next)
	{
		if (lista->number > lista->next->number)
			return (false);
		lista = lista->next;
	}
	return (true);
}

t_stack	*arg_to_stack(t_stack *a, char *argv[])
{
	t_stack	*new_node;
	int		i;

	i = 0;
	while (argv[i])
	{
		new_node = ps_lstnew(ft_atoi(argv[i]));
		if (!new_node)
		{
			ps_lstclear(&new_node);
			error();
		}
		ps_lstadd_back(&a, new_node);
		i++;
	}
	return (a);
}
