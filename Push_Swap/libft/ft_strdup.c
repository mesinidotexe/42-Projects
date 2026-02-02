/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 20:14:03 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/23 20:14:07 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	int		i;
	char	*nstr;

	i = 0;
	nstr = malloc((ft_strlen(s) + 1) * sizeof(char));
	if (!nstr)
		return (NULL);
	while (s[i])
	{
		nstr[i] = s[i];
		i++;
	}
	nstr[i] = '\0';
	return (nstr);
}

/* int main(int argc, char const *argv[])
{
	char *s = "hello";
	char *dup = ft_strdup(s);
	printf ("%s\n", dup);
	free (dup);
	return (0);
} */
