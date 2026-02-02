/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isprint.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 11:48:28 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/20 11:48:41 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_isprint(int c)
{
	if (c >= 32 && c <= 126)
		return (1);
	return (0);
}
/*int main()
{
	int test1 = 9;
	int test2 = 126;
	char test3 = 'K';
	char test4 = 't';
	char test5 = '5';
	printf("%d\n", ft_isprint(test1));
	printf("%d\n", ft_isprint(test2));
	printf("%d\n", ft_isprint(test3));
	printf("%d\n", ft_isprint(test4));
	printf("%d\n", ft_isprint(test5));
	return 0;
}*/
