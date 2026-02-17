/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_general.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 15:12:43 by vmesini-          #+#    #+#             */
/*   Updated: 2026/02/09 15:12:44 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	bits_needed(int n)
{
	int	bits;

	bits = 0;
	while (n > 0)
	{
		n >>= 1;
		bits++;
	}
	return (bits);
}

void	general(t_stack **a, t_stack **b)
{
	int	i;
	int	bits;
	int	size;

	if (!a || !*a)
		return ;
	i = 0;
	indexing(*a);
	bits = bits_needed(find_max_index(*a));
	while (bits > 0)
	{
		size = ps_lstsize(*a);
		while (size > 0)
		{
			if (((*a)->index >> i) & 1)
				ra(*a);
			else
				pb(b, a);
			size--;
		}
		i++;
		while (pa(a, b))
			;
		bits--;
	}
}
