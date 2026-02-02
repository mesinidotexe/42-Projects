/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pushes.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 18:11:33 by vmesini-          #+#    #+#             */
/*   Updated: 2025/12/30 18:11:36 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	pa(t_stack **listaA, t_stack **listaB)
{
	t_stack	*temp;

	if (!listaB || !*listaB)
		return ;
	temp = *listaB;
	*listaB = (*listaB)->next;
	temp->next = *listaA;
	*listaA = temp;
	write(1, "pa\n", 3);
}

void	pb(t_stack **listaB, t_stack **listaA)
{
	t_stack	*temp;

	if (!listaA || !*listaA)
		return ;
	temp = *listaA;
	*listaA = (*listaA)->next;
	temp->next = *listaB;
	*listaB = temp;
	write(1, "pb\n", 3);
}
