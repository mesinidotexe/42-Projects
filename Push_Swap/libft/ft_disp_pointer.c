/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_disp_pointer.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 22:40:55 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/13 22:40:56 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_disp_pointer(void *ptr)
{
	int				counter;
	unsigned long	nbr;

	counter = 0;
	nbr = (unsigned long)ptr;
	if (!ptr)
	{
		counter += (write(1, "(nil)", 5));
		return (counter);
	}
	counter += write(1, "0x", 2);
	counter += ft_disp_x(nbr);
	return (counter);
}
