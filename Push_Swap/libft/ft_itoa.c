/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 00:33:06 by vmesini-          #+#    #+#             */
/*   Updated: 2025/10/28 00:33:08 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static char	*ft_check_max_min(int n)
{
	if (n == -2147483648)
		return (ft_strdup("-2147483648"));
	if (n == 2147483647)
		return (ft_strdup("2147483647"));
	return (NULL);
}

static int	ft_check_digits(int n)
{
	int	digits;

	digits = 1;
	if (n < 0)
		n = -n;
	while (n >= 10)
	{
		n = n / 10;
		digits++;
	}
	return (digits);
}

static char	*ft_write_number(int digits, int n, int neg, char *str)
{
	str[digits + neg] = '\0';
	if (n == 0)
		str[digits - 1] = '0';
	while (n > 0)
	{
		str[digits + neg - 1] = n % 10 + '0';
		digits--;
		n = n / 10;
	}
	if (neg != 0)
		str[0] = '-';
	return (str);
}

char	*ft_itoa(int n)
{
	char	*str;
	int		digits;
	int		neg;

	neg = 0;
	if (n == -2147483648 || n == 2147483647)
		return (str = ft_check_max_min(n));
	digits = ft_check_digits(n);
	if (n < 0)
	{
		neg = 1;
		n = -n;
	}
	str = malloc(sizeof(char) * (digits + neg + 1));
	if (!str)
		return (NULL);
	str = ft_write_number(digits, n, neg, str);
	return (str);
}

/*int main()
{
	char *str = ft_itoa(0);
	char *str = ft_itoa(420);
	char *str = ft_itoa(-420);
	char *str = ft_itoa(-2147483648);
	char *str = ft_itoa(2147483647);
	printf("%s", str);
	free (str);
	return (0);
}*/
