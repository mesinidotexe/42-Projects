/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 18:28:46 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/21 18:28:49 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	size_t			i;
	unsigned char	*u_dest;
	unsigned char	*u_src;

	u_dest = (unsigned char *)dest;
	u_src = (unsigned char *)src;
	i = 0;
	while (i < n)
	{
		u_dest[i] = u_src[i];
		i++;
	}
	return (dest);
}
/* int main()
{
	int a = 10;
	int b = 20;

	int *ptr_a = &a;
	int *ptr_b = &b;
	printf ("%d", *(int *)ft_memcpy(ptr_a, ptr_b, 2));
	return (0);
} */
