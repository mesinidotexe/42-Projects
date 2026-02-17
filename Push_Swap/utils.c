/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/23 20:14:47 by vmesini-          #+#    #+#             */
/*   Updated: 2025/12/23 20:15:02 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	error(void)
{
	write(2, "Error\n", 6);
	exit(-1);
}

int	find_min_index(t_stack *stack)
{
	int		min;
	int		index;
	int		min_index;
	t_stack	*current;

	if (!stack)
		return (0);
	min = stack->number;
	min_index = 0;
	index = 0;
	current = stack;
	while (current)
	{
		if (current->number < min)
		{
			min = current->number;
			min_index = index;
		}
		current = current->next;
		index++;
	}
	return (min_index);
}

int	find_max_index(t_stack *a)
{
	int		max;
	t_stack	*node;

	if (!a)
		return (0);
	max = a->index;
	node = a->next;
	while (node)
	{
		if (node->index > max)
			max = node->index;
		node = node->next;
	}
	return (max);
}

void	indexing(t_stack *a)
{
	t_stack	*current;
	t_stack	*runner;
	int		index;

	current = a;
	while (current)
	{
		index = 0;
		runner = a;
		while (runner)
		{
			if (runner->number < current->number)
				index++;
			runner = runner->next;
		}
		current->index = index;
		current = current->next;
	}
}
