/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isascii.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 11:27:04 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/20 11:27:06 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isascii(int c)
{
	if (c < 0 || c > 127)
		return (0);
	return (1);
}
/*int main()
{
	int test1 = 500;
	int test2 = 5;
	char test3 = 'K';
	char test4 = 't';
	char test5 = '5';
	printf("%d\n", ft_isascii(test1));
	printf("%d\n", ft_isascii(test2));
	printf("%d\n", ft_isascii(test3));
	printf("%d\n", ft_isascii(test4));
	printf("%d\n", ft_isascii(test5));
	return 0;
}*/