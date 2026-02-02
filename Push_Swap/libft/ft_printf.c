/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 22:04:22 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/11 22:04:28 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	check_cases(char s, va_list *args)
{
	if (s == 'c')
		return (ft_disp_char(va_arg(*args, int)));
	if ((s == 'd' || s == 'i'))
		return (ft_disp_int(va_arg(*args, int)));
	if (s == 's')
		return (ft_disp_string(va_arg(*args, char *)));
	if (s == 'u')
		return (ft_disp_unsigned(va_arg(*args, unsigned int)));
	if (s == 'p')
		return (ft_disp_pointer(va_arg(*args, void *)));
	if (s == 'x')
		return (ft_disp_x(va_arg(*args, unsigned int)));
	if (s == 'X')
		return (ft_disp_xx(va_arg(*args, unsigned int)));
	if (s == '%')
		return (write(1, "%%", 1));
	return (0);
}

int	ft_printf(const char *s, ...)
{
	va_list	args;
	int		count;
	int		i;

	count = 0;
	va_start(args, s);
	i = 0;
	while (s[i])
	{
		if (s[i] == '%')
		{
			count += check_cases(s[++i], &args);
			i++;
		}
		else
		{
			write(1, &s[i], 1);
			count++;
			i++;
		}
	}
	return (count);
}
