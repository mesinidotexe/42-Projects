/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   args_parser.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 19:02:49 by vmesini-          #+#    #+#             */
/*   Updated: 2026/01/12 19:02:51 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	count_numbers(char **argv)
{
	int		i;
	int		j;
	int		count;
	char	**tmp;

	i = 1;
	count = 0;
	while (argv[i])
	{
		tmp = ft_split(argv[i], ' ');
		if (!tmp)
			return (-1);
		j = 0;
		while (tmp[j])
		{
			count++;
			j++;
		}
		free_array(tmp);
		i++;
	}
	return (count);
}

char	**split_all(char **argv, char **splitted)
{
	int		i;
	int		j;
	int		k;
	char	**tmp;

	i = 1;
	k = 0;
	while (argv[i])
	{
		tmp = ft_split(argv[i++], ' ');
		if (!tmp)
			return (NULL);
		j = 0;
		while (tmp[j])
		{
			splitted[k++] = ft_strdup(tmp[j]);
			if (!splitted)
				return (free_array(splitted), free_array(tmp), NULL);
			j++;
		}
		free_array(tmp);
	}
	splitted[k] = NULL;
	return (splitted);
}

int	validate_splitted(char **splitted, char *argv0)
{
	char	**tmp_argv;
	int		count;
	int		i;

	count = 0;
	while (splitted[count])
		count++;
	tmp_argv = malloc(sizeof(char *) * (count + 2));
	if (!tmp_argv)
		return (0);
	tmp_argv[0] = argv0;
	i = -1;
	while (++i < count)
		tmp_argv[i + 1] = splitted[i];
	tmp_argv[count + 1] = NULL;
	if (!check_data(count + 1, tmp_argv))
		return (free(tmp_argv), 0);
	free(tmp_argv);
	return (1);
}
