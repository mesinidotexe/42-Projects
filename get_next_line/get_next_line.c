/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vmesini- <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 23:32:51 by vmesini-          #+#    #+#             */
/*   Updated: 2025/11/17 23:32:53 by vmesini-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*get_next_line(int fd)
{
	static char	buffer[BUFFER_SIZE + 1];
	char		*line;
	int			bytes_read;

	line = NULL;
	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	while (!line_chr(line))
	{
		if (buffer[0] == 0)
		{
			bytes_read = read(fd, buffer, BUFFER_SIZE);
			if (bytes_read < 0)
				return (free(line), NULL);
			if (bytes_read == 0)
				return (line);
		}
		line = gnl_join(line, buffer);
		if (!line)
			return (NULL);
		cleanbuff(buffer);
	}
	return (line);
}

/* int	main(void)
{
	int		fd;
	char	*line;

	fd = open("teste.txt", O_RDONLY);
	line = get_next_line(fd);
	printf(">%s<", line);
	free(line);
	line = get_next_line(fd);
	printf(">%s<", line);
	free(line);
	line = get_next_line(fd);
	printf(">%s<", line);
	free(line);
	line = get_next_line(fd);
	printf(">%s<", line);
	free(line);
	return (0);
} */
