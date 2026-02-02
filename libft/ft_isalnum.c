/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 18:12:20 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/21 18:12:23 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isalnum(int c)
{
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0'
			&& c <= '9'))
	{
		return (1);
	}
	return (0);
}

/*int main()
{
	int test1 = 500;
	int test2 = 5;
	char test3 = 'K';
	char test4 = 't';
	char test5 = '5';
	printf("%d\n", ft_isalnum(test1));
	printf("%d\n", ft_isalnum(test2));
	printf("%d\n", ft_isalnum(test3));
	printf("%d\n", ft_isalnum(test4));
	printf("%d\n", ft_isalnum(test5));
	return 0;
}*/
