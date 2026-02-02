/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 12:41:51 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/24 12:42:08 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*destination;
	unsigned char	*source;

	destination = (unsigned char *)dest;
	source = (unsigned char *)src;
	if (destination < source)
		ft_memcpy(dest, src, n);
	else
	{
		while (n > 0)
		{
			destination[n - 1] = source[n - 1];
			n--;
		}
	}
	return (dest);
}

/* int	main(void)
{
	char	str[100] = "You wanna guess the color of my underwaer";

	char *first, *second;
	first = str;
	second = str;
	printf("Original string :%s\n\n ", str);
	// when overlap happens then it just ignore it
	memcpy(first + 8, first, 10);
	printf("memcpy overlap : %s\n ", str);
	// when overlap it start from first position
	memmove(second + 8, first, 10);
	printf("memmove overlap : %s\n ", str);
	ft_memmove(second + 8, first, 10);
	printf("ft_memmove overlap : %s\n ", str);
	return (0);
} */
