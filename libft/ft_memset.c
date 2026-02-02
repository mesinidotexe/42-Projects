/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 20:21:27 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/21 20:21:33 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	size_t		i;

	i = 0;
	while (i < n)
	{
		((unsigned char *)s)[i] = c;
		i++;
	}
	return (s);
}

/* int main(void)
{
    char buffer[20] = "Hello, world!";
    printf("Antes: %s\n", buffer);
    ft_memset(buffer, '-', 5);
    printf("Depois: %s\n", buffer);
    return 0;
} */
