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
