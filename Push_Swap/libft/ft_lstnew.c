/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 20:56:35 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/04 20:56:36 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*nextnode;

	nextnode = malloc(sizeof(struct s_list));
	if (!nextnode)
		return (NULL);
	nextnode->content = content;
	nextnode->next = NULL;
	return (nextnode);
}

/* int main()
{
    t_list *head;
    int test = 36;
    head = ft_lstnew(&test);
    printf ("%d", *(int *)head->content);
    return 0;
} */