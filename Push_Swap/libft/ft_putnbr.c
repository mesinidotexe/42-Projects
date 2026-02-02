/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 15:51:09 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/17 15:51:10 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_putnbr(int n)
{
	int		counter;
	long	new_number;

	new_number = n;
	counter = 0;
	if (new_number < 0)
	{
		write(1, "-", 1);
		new_number = -new_number;
		counter++;
	}
	if (new_number >= 10)
	{
		counter += ft_putnbr(new_number / 10);
	}
	ft_putchar((new_number % 10) + '0');
	counter++;
	return (counter);
}
