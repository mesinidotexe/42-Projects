/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swaps.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 18:11:43 by vmesini-          #+#    #+#             */
/*   Updated: 2025/12/30 18:11:44 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sa(t_stack *lista)
{
	int	swap;

	if (!lista || !lista->next)
		return ;
	swap = lista->number;
	lista->number = lista->next->number;
	lista->next->number = swap;
	write(1, "sa\n", 3);
}

void	sb(t_stack *lista)
{
	int	swap;

	if (!lista || !lista->next)
		return ;
	swap = lista->number;
	lista->number = lista->next->number;
	lista->next->number = swap;
	write(1, "sb\n", 3);
}

void	ss(t_stack *listaA, t_stack *listaB)
{
	int	swapa;
	int	swapb;

	if (!listaA || !listaA->next)
		return ;
	if (!listaB || !listaB->next)
		return ;
	swapa = listaA->number;
	listaA->number = listaA->next->number;
	listaA->next->number = swapa;
	swapb = listaB->number;
	listaB->number = listaB->next->number;
	listaB->next->number = swapb;
	write(1, "ss\n", 3);
}
