/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalpha.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 11:38:38 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/20 11:38:42 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_isalpha(int c)
{
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		return (1);
	return (0);
}

/*int main()
{
	int test1 = 500;
	int test2 = 5;
	char test3 = 'K';
	char test4 = 't';
	char test5 = '5';
	printf("%d\n", ft_isalpha(test1));
	printf("%d\n", ft_isalpha(test2));
	printf("%d\n", ft_isalpha(test3));
	printf("%d\n", ft_isalpha(test4));
	printf("%d\n", ft_isalpha(test5));
	return 0;
}*/