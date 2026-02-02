/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 19:35:25 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/27 19:35:27 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_count_word(char const *s, char c)
{
	int			i;
	int	word;

	i = 0;
	word = 0;
	while (s[i])
	{
		while (s[i] == c)
			i++;
		if (s[i] != c && s[i] != '\0')
			word++;
		while (s[i] != c && s[i] != '\0')
			i++;
	}
	return (word);
}

static size_t	ft_str_char_len(const char *s, char c)
{
	size_t	i;

	i = 0;
	if (s[i] == '\0')
		return (0);
	while (s[i] != '\0' && s[i] != c)
		i++;
	return (i);
}

static char	*ft_write_words(const char *s, char c)
{
	int		i;
	char	*arr;

	arr = ft_calloc(sizeof(char), (ft_str_char_len(s, c) + 1));
	if (!arr)
		return (NULL);
	i = 0;
	while (s[i] && s[i] != c)
	{
		arr[i] = s[i];
		i++;
	}
	return (arr);
}

char	**ft_split(char const *s, char c)
{
	int		i;
	int		j;
	char	**array;

	if (!s)
		return (NULL);
	array = ft_calloc(sizeof(char *), ft_count_word(s, c) + 1);
	if (!array)
		return (NULL);
	i = 0;
	j = 0;
	while (i < ft_count_word(s, c))
	{
		while (s[j] == c && s[j] != '\0')
			j++;
		array[i] = ft_write_words(s + j, c);
		if (!array[i])
			return(free_array(array), NULL);
		j = j + ft_str_char_len(&s[j], c);
		i++;
	}
	return (array);
}
/*int	main(void)
{
	char	*string;
	char	**arrays;
	int		i;

	string = "             >Hello World f 123 Bye :)<   ";
	arrays = ft_split(string, ' ');
	i = 0;
	while (arrays[i] != NULL)
	{
		printf("%s\n", arrays[i]);
		i++;
	}
	printf("%s\n", arrays[i]);
	return (0);
} */
