/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 20:55:08 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/04 20:55:10 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*ultimo;

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
/*int main()
{
    t_list *head;
    t_list *new;
    
    int head_value = 50;
    head = ft_lstnew(&head_value);
    int new_value = 36;
    new = ft_lstnew(&new_value);
    ft_lstadd_back(&head, new);
    printf("%d", *(int *)head->content);
    return 0;
}*/
