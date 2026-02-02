/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_striteri.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 19:09:55 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/29 19:09:56 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char *))
{
	unsigned int	i;

	if (!s || !f)
		return ;
	i = 0;
	while (s[i])
	{
		f(i, &s[i]);
		i++;
	}
}

/* void	ft_weird(unsigned int i, char *c)
{
	(void) i;
	if (*c >= 65 && *c <= 90)
		*c = *c + 32;
}
int main()
{
	char s[] = "LALAlalaLALAlala";
	ft_striteri(s, ft_weird);
	printf("%s", s);
	return (0);
} */
