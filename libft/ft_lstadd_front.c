/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 20:55:22 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/04 20:55:24 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!new || !lst)
		return ;
	new->next = *lst;
	*lst = new;
}
/* int main()
{
    t_list *head;
    t_list *new;
    
    int head_value = 50;
    head = ft_lstnew(&head_value);
    int new_value = 36;
    new = ft_lstnew(&new_value);
    ft_lstadd_front(&head, new);
    printf("%d", *(int *)head->content);
    return 0;
} */
