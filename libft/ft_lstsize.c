/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/04 20:56:49 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/04 20:56:50 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	counter;

	if (!lst)
		return (0);
	counter = 0;
	while (lst)
	{
		counter++;
		lst = lst->next;
	}
	return (counter);
}

/* int main()
{
    t_list *head;

    head = ft_lstnew((int *)10);
    head->next = ft_lstnew((int *)20);
    head->next->next = ft_lstnew((int *)30);
    head->next->next->next = ft_lstnew((int *)40);
    printf("%d\n", ft_lstsize(head));

	printf ("%d", *(int *)&head->content);

    return 0;
} */
