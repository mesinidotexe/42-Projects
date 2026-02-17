/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverses.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 18:13:53 by vmesini-          #+#    #+#             */
/*   Updated: 2025/12/30 18:13:54 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rra(t_stack *lista)
{
	int		temp;
	t_stack	*current;
	t_stack	*prev;

	if (!lista || !lista->next)
		return ;
	current = lista;
	while (current->next)
		current = current->next;
	temp = current->number;
	while (current != lista)
	{
		prev = lista;
		while (prev->next != current)
			prev = prev->next;
		current->number = prev->number;
		current = prev;
	}
	lista->number = temp;
	write(1, "rra\n", 4);
}

void	rrb(t_stack *lista)
{
	int		temp;
	t_stack	*current;
	t_stack	*prev;

	if (!lista || !lista->next)
		return ;
	current = lista;
	while (current->next)
		current = current->next;
	temp = current->number;
	while (current != lista)
	{
		prev = lista;
		while (prev->next != current)
			prev = prev->next;
		current->number = prev->number;
		current = prev;
	}
	lista->number = temp;
	write(1, "rrb\n", 4);
}
