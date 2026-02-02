/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 21:42:36 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/23 21:42:40 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*vetor;

	if (nmemb == 0 || size == 0)
	{
		return (malloc(0));
	}
	if (nmemb > __SIZE_MAX__ / size)
	{
		return (malloc(0));
	}
	vetor = malloc(nmemb * size);
	if (!vetor)
	{
		return (NULL);
	}
	ft_bzero(vetor, nmemb * size);
	return (vetor);
}
/* int main()
{
	char *palavra = NULL;
	palavra = ft_calloc(1000000, 1);
	//printf("|%c|", *palavra);
	free (palavra);
	// printf ("->%lu\n", __SIZE_MAX__ + 1);
	printf ("%p\n", palavra);
	free (palavra);
	printf ("%p", palavra);
	return 0;
} */