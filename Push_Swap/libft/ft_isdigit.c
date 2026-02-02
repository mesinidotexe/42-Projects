/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isdigit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 11:44:22 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/20 11:44:25 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isdigit(int c)
{
	if (c >= '0' && c <= '9')
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
	printf("%d\n", ft_isdigit(test1));
	printf("%d\n", ft_isdigit(test2));
	printf("%d\n", ft_isdigit(test3));
	printf("%d\n", ft_isdigit(test4));
	printf("%d\n", ft_isdigit(test5));
	return 0;
}*/