/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 17:09:06 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/17 17:09:09 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int	ft_printf(const char *s, ...);
int	ft_putstr(char *s);
int	ft_putnbr(int n);
int	ft_putchar(char c);
int	ft_disp_char(int c);
int	ft_disp_int(int nbr);
int	ft_disp_string(char *str);
int	ft_disp_unsigned(unsigned int nbr);
int	ft_disp_pointer(void *ptr);
int	ft_disp_x(unsigned long nbr);
int	ft_disp_xx(unsigned long nbr);

#endif