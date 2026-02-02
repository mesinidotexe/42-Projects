/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 15:09:13 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/06 15:09:15 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*newlist;
	t_list	*auxlist;

	if (!lst || !f || !del)
		return (NULL);
	newlist = NULL;
	while (lst)
	{
		auxlist = ft_lstnew(f(lst->content));
		if (!auxlist)
		{
			ft_lstclear(&auxlist, del);
			return (NULL);
		}
		ft_lstadd_back(&newlist, auxlist);
		lst = lst->next;
	}
	return (newlist);
}
