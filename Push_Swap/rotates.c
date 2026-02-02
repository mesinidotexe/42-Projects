/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotates.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 18:13:30 by vmesini-          #+#    #+#             */
/*   Updated: 2025/12/30 18:13:31 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ra(t_stack *lista)
{
	int	temp;

	temp = lista->number;
	while (lista->next)
	{
		lista->number = lista->next->number;
		lista = lista->next;
	}
	lista->number = temp;
	write(1, "ra\n", 3);
}

void	rb(t_stack *lista)
{
	int	temp;

	temp = lista->number;
	while (lista->next)
	{
		lista->number = lista->next->number;
		lista = lista->next;
	}
	lista->number = temp;
	write(1, "rb\n", 3);
}

void	rr(t_stack *listaA, t_stack *listaB)
{
	int	tempa;
	int	tempb;

	tempa = listaA->number;
	while (listaA->next)
	{
		listaA->number = listaA->next->number;
		listaA = listaA->next;
	}
	listaA->number = tempa;
	tempb = listaB->number;
	while (listaB->next)
	{
		listaB->number = listaB->next->number;
		listaB = listaB->next;
	}
	listaB->number = tempb;
	write(1, "rr\n", 3);
}
