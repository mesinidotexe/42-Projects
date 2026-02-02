/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 20:17:07 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/29 20:17:08 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char			*news;
	unsigned int	i;
	unsigned int	j;

	i = 0;
	j = 0;
	if (!s || !f)
		return (NULL);
	while (s[j])
		j++;
	news = malloc(sizeof(char) * (j + 1));
	if (!news)
		return (NULL);
	while (s[i])
	{
		news[i] = f(i, s[i]);
		i++;
	}
	news[i] = '\0';
	return (news);
}
/* char	ft_weird(unsigned int i, char c)
{
	(void)i;
	if (c >= 65 && c <= 90)
		c = c + 32;
	return (c);
}
int	main(void)
{
	char	*result;

	result = ft_strmapi("LALALALAlalalalalaLALALALALlalalala", ft_weird);
	printf("%s", result);
	free(result);
	return (0);
} */
