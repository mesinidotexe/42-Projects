/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lst_functtions.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 19:03:20 by vmesini-          #+#    #+#             */
/*   Updated: 2026/01/12 19:03:21 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*ps_lstnew(int content)
{
	t_stack	*nextnode;

	nextnode = malloc(sizeof(struct s_stack));
	if (!nextnode)
		return (NULL);
	nextnode->number = content;
	nextnode->next = NULL;
	return (nextnode);
}

void	ps_lstclear(t_stack **lst)
{
	t_stack	*current;
	t_stack	*tmp_next;

	if (!lst)
		return ;
	current = *lst;
	tmp_next = *lst;
	while (current)
	{
		tmp_next = tmp_next->next;
		ps_lstdelone(current);
		current = tmp_next;
		if (!current)
			free(current);
	}
	*lst = NULL;
}

void	ps_lstadd_back(t_stack **lst, t_stack *new)
{
	t_stack	*ultimo;

	if (!lst || !new)
		return ;
	if (!*lst)
		*lst = new;
	else
	{
		ultimo = *lst;
		while (ultimo->next)
			ultimo = ultimo->next;
		ultimo->next = new;
	}
}

void	ps_lstadd_front(t_stack **lst, t_stack *new)
{
	if (!new || !lst)
		return ;
	new->next = *lst;
	*lst = new;
}

t_stack	*ps_lstlast(t_stack *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next)
	{
		lst = lst->next;
	}
	return (lst);
}
