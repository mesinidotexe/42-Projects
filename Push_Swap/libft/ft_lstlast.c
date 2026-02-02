/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 20:56:14 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/04 20:56:15 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next)
	{
		lst = lst->next;
	}
	return (lst);
}

/*iint man()
{
	t_list *head = ft_lstnew((void *)10);
	t_list *second = ft_lstnew((void *)20);
	t_list *third = ft_lstnew((void *) 30);
    
	head->next = second;
	second->next = third;
    printf("%d\n", (int *)head->content);
    head = ft_lstlast(head);
    printf("%d", (int *)head->content);
    return 0;
}*/
