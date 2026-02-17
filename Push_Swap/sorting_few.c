/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_few.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/09 15:13:00 by vmesini-          #+#    #+#             */
/*   Updated: 2026/02/09 15:13:01 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sorting_three(t_stack *a)
{
	int	first;
	int	second;
	int	third;

	first = a->number;
	second = a->next->number;
	third = a->next->next->number;
	if (first > second && second > third)
	{
		ra(a);
		sa(a);
	}
	else if (first > second && first > third && second < third)
		ra(a);
	else if (first < second && second > third && first < third)
	{
		rra(a);
		sa(a);
	}
	else if (first > second && first < third)
		sa(a);
	else if (first < second && second > third && first > third)
		rra(a);
}

void	sorting_four(t_stack **a, t_stack **b)
{
	int	min_index;

	if (!a || !*a)
		return ;
	min_index = find_min_index(*a);
	if (min_index == 1)
		ra(*a);
	else if (min_index == 2)
	{
		ra(*a);
		ra(*a);
	}
	else if (min_index == 3)
		rra(*a);
	pb(b, a);
	sorting_three(*a);
	pa(a, b);
}

void	sorting_five(t_stack **a, t_stack **b)
{
	int	min_index;

	if (!a || !*a)
		return ;
	min_index = find_min_index(*a);
	if (min_index == 1)
		ra(*a);
	else if (min_index == 2)
	{
		ra(*a);
		ra(*a);
	}
	else if (min_index == 3)
	{
		rra(*a);
		rra(*a);
	}
	else if (min_index == 4)
		rra(*a);
	pb(b, a);
	sorting_four(a, b);
	pa(a, b);
}

void	sorting(t_stack *a, t_stack *b)
{
	if (ps_lstsize(a) == 2)
		sa(a);
	else if (ps_lstsize(a) == 3)
		sorting_three(a);
	else if (ps_lstsize(a) == 4)
		sorting_four(&a, &b);
	else if (ps_lstsize(a) == 5)
		sorting_five(&a, &b);
	else if (ps_lstsize(a) >= 6)
		general(&a, &b);
}
