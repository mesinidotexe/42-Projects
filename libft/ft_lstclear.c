/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 21:09:56 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/04 21:09:58 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*current;
	t_list	*tmp_next;

	if (!lst || !del)
		return ;
	current = *lst;
	tmp_next = *lst;
	while (current)
	{
		tmp_next = tmp_next->next;
		ft_lstdelone(current, del);
		current = tmp_next;
		if (!current)
			free(current);
	}
	*lst = NULL;
}
/*void	del(void *content)
{
	free(content);
}*/

/*int	main(void)
{
	t_list	*head;
	int		*num;
	int		*num2;
	int		*num3;

	head = NULL;
	num = malloc(sizeof(int) * 1);
	*num = 70;
	num2 = malloc(4);
	*num2 = 80;
	num3 = malloc(4);
	*num3 = 90;
	head = ft_lstnew(num);
	ft_lstadd_back(&head, ft_lstnew(num2));
	ft_lstadd_back(&head, ft_lstnew(num3));
	ft_lstclear(&head->next, &del);
	printf("|||||%d|||||\n", *(int *)head->content);
	return (0);
}*/