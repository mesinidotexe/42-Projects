/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   data_validation.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 19:03:06 by vmesini-          #+#    #+#             */
/*   Updated: 2026/01/12 19:03:08 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	empty_strings(int argc, char **argv)
{
	int	i;

	i = 1;
	while (i < argc)
	{
		if (!argv[i][0])
			return (1);
		i++;
	}
	return (0);
}

int	args_are_int(int argc, char *argv[])
{
	int	i;
	int	j;

	i = 1;
	while (i < argc)
	{
		j = 0;
		if (argv[i][j] == '-' || argv[i][j] == '+')
			j++;
		if (!argv[i][j])
			return (0);
		while (argv[i][j])
		{
			if (!ft_isdigit(argv[i][j]))
				return (0);
			j++;
		}
		i++;
	}
	return (1);
}

int	overflow(int argc, char *argv[])
{
	long	max_min;
	int		i;

	i = 1;
	while (i < argc)
	{
		max_min = ft_atol(argv[i]);
		if (max_min < INT_MIN || max_min > INT_MAX)
			return (1);
		i++;
	}
	return (0);
}

int	has_duplicates(int argc, char **argv)
{
	int		i;
	int		j;
	long	num_i;
	long	num_j;

	i = 1;
	while (i < argc)
	{
		num_i = ft_atol(argv[i]);
		j = i + 1;
		while (j < argc)
		{
			num_j = ft_atol(argv[j]);
			if (num_i == num_j)
				return (1);
			j++;
		}
		i++;
	}
	return (0);
}

int	check_data(int argc, char *argv[])
{
	if (empty_strings(argc, argv))
		return (0);
	if (!args_are_int(argc, argv))
		return (0);
	if (overflow(argc, argv))
		return (0);
	if (has_duplicates(argc, argv))
		return (0);
	return (1);
}
