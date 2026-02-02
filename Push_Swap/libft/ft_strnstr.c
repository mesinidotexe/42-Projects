/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                          :+:      :+:    :+:*/
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 20:33:51 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/20 20:33:56 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <string.h>

char	*ft_strnstr(char *big, char *little, size_t len)
{
	size_t	i;
	size_t	j;
	size_t	strsize;

	i = 0;
	strsize = ft_strlen(little);
	if (strsize == 0)
		return (&big[i]);
	while ((i < len) && (big[i]))
	{
		j = 0;
		while ((j + i < len) && (big[i + j] == little[j]))
		{
			j++;
			if (little[j] == '\0')
				return (&big[i]);
		}
		i++;
	}
	return (NULL);
}

/* int	main(void)
{
	char *s1 = "AAAAAAAAAAAAA";
 	size_t max = strlen(s1);

 	char *i2 = ft_strnstr(s1, s1, max);
	printf ("%s", i2);
	return (0);I
} */
