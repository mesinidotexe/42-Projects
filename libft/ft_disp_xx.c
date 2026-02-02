/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_X.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 15:33:44 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/17 15:33:45 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_disp_xx(unsigned long nbr)
{
	char	*base;
	int		i;
	int		value;

	i = 0;
	base = "0123456789ABCDEF";
	if (nbr >= 16)
	{
		i += ft_disp_xx(nbr / 16);
	}
	value = base[nbr % 16];
	i += write(1, &value, 1);
	return (i);
}
