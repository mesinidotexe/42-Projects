/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 17:38:30 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/23 17:38:33 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	size_t	len;

	len = ft_strlen(s);
	while (1)
	{
		if (s[len] == (char)c)
		{
			return ((char *)&s[len]);
		}
		if (len == 0)
			break ;
		len--;
	}
	return (NULL);
}

/* int	main(void)
{
	const char *str1 = "abcdeflghijklmnopqrstuvwxy";
	printf("%s \n", ft_strrchr(str1, '\0'));
	return (0);
} */