/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_disp_x.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 21:05:52 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/14 21:05:58 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_disp_x(unsigned long nbr)
{
	char	*base;
	int		i;
	int		value;

	i = 0;
	base = "0123456789abcdef";
	if (nbr >= 16)
	{
		i += ft_disp_x(nbr / 16);
	}
	value = base[nbr % 16];
	i += write(1, &value, 1);
	return (i);
}
