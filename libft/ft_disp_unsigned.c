/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_disp_unsigned.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 21:34:25 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/13 21:34:29 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_check_digits(unsigned int n)
{
	int	digits;

	digits = 1;
	while (n >= 10)
	{
		n = n / 10;
		digits++;
	}
	return (digits);
}

int	ft_disp_unsigned(unsigned int n)
{
	int	return_value;

	return_value = ft_check_digits(n);
	if (n >= 10)
	{
		ft_disp_unsigned(n / 10);
	}
	ft_putchar((n % 10) + '0');
	return (return_value);
}
